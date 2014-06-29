# -*- coding: utf-8 -*-
#==============================================================================#
#                                                                              #
#    Offline KI                                                                #
#                                                                              #
#    Copyright (C) 2004-2011  The Offline KI contributors                      #
#    See the file AUTHORS for more info about the contributors (including      #
#    contact information)                                                      #
#                                                                              #
#    This program is free software: you can redistribute it and/or modify      #
#    it under the terms of the GNU General Public License as published by      #
#    the Free Software Foundation, either version 3 of the License, or         #
#    (at your option) any later version, with or (at your option) without      #
#    the Uru exception (see below).                                            #
#                                                                              #
#    This program is distributed in the hope that it will be useful,           #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#    GNU General Public License for more details.                              #
#                                                                              #
#    Please see the file COPYING for the full GPLv3 license, or see            #
#    <http://www.gnu.org/licenses/>                                            #
#                                                                              #
#    Uru exception: In addition, this file may be used in combination with     #
#    (non-GPL) code within the context of Uru.                                 #
#                                                                              #
#==============================================================================#
import string
import os
from Plasma import *
from PlasmaTypes import *
from PlasmaKITypes import *
from PlasmaVaultConstants import *
from PlasmaNetConstants import *
from xPsnlVaultSDL import *
import xUserKI
import xUserKIConfig

# Global info variables and configuration
gGotoPlaces = {
    'city': {
        'ferry': [-216, -591, 9],
        'gallery': [168, -490, 163],
        'library': [792, -597, 260],
        'takotah': [0, -97, 221],
        'rooftop': [-60, -195, 275]
    },
    'Ercana': {
        'brokentrail': [-528, -964, -57],
        'factory': [0, -146, -13],
        'start': [-497, -588, -45],
        'trailend': [-886, -728, -48],
        'pellets': [0, 750, 80]
    },
    'Kadish': {
        'gallerylink': [48, 181, 15],
        'pyramid': [736, -121, 3],
        'vault': [1182, 210, 9]
    },
    'Minkata': {
        'cage': [-37, 1018, 14],
        'cave1': [106, 1402, -13],
        'cave2': [1515, 655, -13],
        'cave3': [-1021, 1864, -13],
        'cave4': [-885, -546, -13],
        'cave5': [-1452, 1069, -13]
    }
}
gColorNames = ['black', 'blue', 'brown', 'cyan', 'darkbrown', 'darkgreen', 'darkpurple', 'gray', 'green', 'magenta', 'maroon', 'navyblue', 'orange', 'pink', 'red', 'slateblue', 'steelblue', 'tan', 'white', 'yellow']

# Global helper variables
gLastSpawnPos = []
gCommandList = []

# Helper functions
def StrToColor(str):
    color = None
    exec('color = ptColor().%s()' % str.lower())
    return color


def FilterFilename(filename):
    filename = string.replace(filename, '<', '')
    filename = string.replace(filename, '>', '')
    filename = string.replace(filename, '/', '')
    filename = string.replace(filename, '\\', '')
    filename = string.replace(filename, '*', '')
    filename = string.replace(filename, '?', '')
    return filename


def ExportFile(ki, dirname, element):
    datatype = element.getType()
    # text notes
    if datatype == PtVaultNodeTypes.kTextNoteNode:
        element = element.upcastToTextNoteNode()
        if type(element) != type(None):
            filename = FilterFilename(str(element.getID()) + ' - ' + element.getTitle() + '.txt')
            saveFile = open((dirname + '\\' + filename), 'w')
            saveFile.write(element.getText())
            saveFile.close()
            ki.AddChatLine(None, 'KI Text saved as %s' % filename, 0)
            return
    # images
    elif datatype == PtVaultNodeTypes.kImageNode:
        element = element.upcastToImageNode()
        if type(element) != type(None):
            filename = FilterFilename(str(element.getID()) + ' - ' + element.getTitle() + '.jpg')
            element.imageGetImage().saveAsJPEG((dirname + '\\' + filename), 80)
            ki.AddChatLine(None, 'Image saved as %s' % filename, 0)
            return
    # unknown type
    ki.DisplayErrorMessage('This KI element can not be exported - only marker missions, pictures and text notes are supported')


# Callback functions
def OnTimer(ki, id):
    if id == xUserKI.kEnableTimer:
        PtForceCursorShown()
        PtSendKIMessage(kEnableKIandBB, 0)
        return True
    return False


def OnDefaultKey(ki, isShift, isCtrl, keycode):
    # Don't use Scroll Lock here, for some reason it gets send twice as often as it should
    # Scripted commands
    if isCtrl and not isShift and keycode == 19: # Pause
        global gCommandList
        if len(gCommandList):
            ki.SendMessage(gCommandList[0], silent=True)
            gCommandList.remove(gCommandList[0])
            # don't tell user about last command... it would show the KI
        return

def OnLinkingOut(ki):
    global gLastSpawnPos
    # reset spawn position
    gLastSpawnPos = []


def OnAvatarSpawn(ki):
    global gLastSpawnPos
    pos = PtGetLocalAvatar().position()
    gLastSpawnPos = [pos.getX(), pos.getY(), pos.getZ()]


# Main function
def OnCommand(ki, arg, cmnd, args, playerList, silent):
    # base commands
    if cmnd == 'export':
        element = xUserKI.KIManager.BKCurrentContent
        if type(element) != type(None): element = xUserKI.KIManager.BKCurrentContent.getChild()
        if type(element) == type(None):
            ki.DisplayErrorMessage('You must have a KI element selected to use this command')
            return True
        dirname = 'export'
        if not os.path.exists(dirname): os.mkdir(dirname)
        ExportFile(ki, dirname, element)
        return True
    if cmnd == 'kilight':
        (valid, time) = xUserKI.GetArg(ki, cmnd, args, 'time in seconds (default: 60)',
          lambda args: len(args) == 1, lambda args: int(args[0]),
          lambda args: len(args) == 0, lambda args: int(60))
        if not valid: return True
        xUserKI.KIManager.DoKILight(1, 1, time)
        if not silent: ki.AddChatLine(None, 'You KI will light for %i seconds' % time, 0)
        return True
    if (cmnd == 'clearcam'):
        PtClearCameraStack()
        if not silent: ki.AddChatLine(None, 'Successfully cleared the camera stack', 0)
        return True
    if (cmnd == 'enablefp'):
        cam = ptCamera()
        cam.enableFirstPersonOverride()
        if not silent: ki.AddChatLine(None, '1st person switching enabled', 0)
        return True
    # link commands
    if (cmnd == 'hood'):
        gender = PtGetLocalAvatar().avatar.getAvatarClothingGroup()
        if (gender == 0): hisher = 'his'
        elif (gender == 1): hisher = 'her'
        else: hisher = 'the'
        if not silent: ki.DisplayStatusMessage('%s is linking to %s neighborhood' % (PtGetClientName(), hisher), 1)
        linkMgr = ptNetLinkingMgr()
        linkMgr.linkToMyNeighborhoodAge()
        return True
    if (cmnd == 'nexus'):
        gender = PtGetLocalAvatar().avatar.getAvatarClothingGroup()
        if (gender == 0): hisher = 'his'
        elif (gender == 1): hisher = 'her'
        else: hisher = 'the'
        if not silent: ki.DisplayStatusMessage('%s is linking to %s Nexus' % (PtGetClientName(), hisher), 1)
        PtLinkToAge("Nexus")
        return True
    # avatar movement
    if (cmnd == 'jump'):
        (valid, height) = xUserKI.GetArg(ki, cmnd, args, 'number of D\'ni feet',
          lambda args: len(args) == 1, lambda args: int(args[0]))
        if not valid: return True
        if xUserKIConfig.IsLockedAge():
            ki.DisplayErrorMessage("You are in a locked age, some KI commands are disabled here")
            return True
        if (height == 0):
            ki.DisplayErrorMessage('How do you want to jump 0 feet?!?')
            return True
        avatar = PtGetLocalAvatar()
        xUserKI.WarpObjectRelative(avatar, 0, 0, height, localAxes = True)
        if silent: return True
        if (height > 0):
            if (height == 1): ki.AddChatLine(None, 'You jump one foot into the air', 0)
            else: ki.AddChatLine(None, 'You jump %s feet into the air' % height, 0)
        else:
            if (height == -1): ki.AddChatLine(None, 'You jump one foot down', 0)
            else: ki.AddChatLine(None, 'You jump %s feet down' % (-height), 0)
        return True
    if (cmnd in ['respawn', 'sav', 'a']):
        if not len(gLastSpawnPos):
            ki.DisplayErrorMessage('I\'m sorry, I was unable to save your spawn point, so I can\'t bring you back there.')
        else:
            avatar = PtGetLocalAvatar()
            avatar.netForce(1)
            avatar.avatar.exitSubWorld() # for ages like Relativity
            newMat = ptMatrix44()
            newMat.translate(ptVector3(gLastSpawnPos[0], gLastSpawnPos[1], gLastSpawnPos[2])) # warp to that position, reset rotation etc. in case we come from a... strange subworld
            avatar.physics.warp(newMat)
            if not silent: ki.DisplayStatusMessage('%s re-spawns to the starting point' % PtGetClientName(), 1)
        return True
    if (cmnd == 'spawn'):
        if xUserKIConfig.IsLockedAge():
            ki.DisplayErrorMessage("You are in a locked age, some KI commands are disabled here")
            return True
        (valid, n) = xUserKI.GetArg(ki, cmnd, args, '[number of spawns]',
          lambda args: len(args) == 0, lambda args: 1,
          lambda args: len(args) == 1, lambda args: int(args[0]))
        if not valid: return True
        if (n < 1): n = 1
        i = 0
        while i < n:
            PtAvatarSpawnNext()
            i = i+1
        return True
    if (cmnd == 'goto'):
        (valid, target) = xUserKI.GetArg(ki, cmnd, args, 'goto place',
          lambda args: len(args) == 1, lambda args: args[0].lower())
        if not valid: return True
        if xUserKIConfig.IsLockedAge():
            ki.DisplayErrorMessage("You are in a locked age, some KI commands are disabled here")
            return True
        # get the place
        if target == 'listall':
            ki.AddChatLine(None, 'The following goto places are available: %s' % xUserKI.JoinListRec(gGotoPlaces), 0)
            return True
        age = PtGetAgeName()
        if not age in gGotoPlaces:
            ki.DisplayErrorMessage('There is no goto place in this age. goto places are available in: %s' % xUserKI.JoinList(gGotoPlaces))
            return True
        places = gGotoPlaces[age]
        if target == 'list':
            ki.AddChatLine(None, 'The following goto places are available in this age: %s' % xUserKI.JoinList(places), 0)
            return True
        if not target in places:
            ki.DisplayErrorMessage('There is no goto place called \'%s\' in this age. Use one of the following: %s' % (target, xUserKI.JoinList(places)))
            return True
        place = places[target]
        # warp to the place
        xUserKI.WarpObjectToPos(PtGetLocalAvatar(), place[0], place[1], place[2])
        if not silent: ki.DisplayStatusMessage('%s warps to \'%s\'' % (PtGetClientName(), target), 1)
        return True
    if (cmnd in ['float', 'nofloat']):
        if xUserKIConfig.IsLockedAge():
            ki.DisplayErrorMessage("You are in a locked age, some KI commands are disabled here")
            return True
        if 0 == 1:
            (valid, objects) = xUserKI.GetArg(ki, cmnd, args, '[list of objects]',
                lambda args: len(args) == 0, lambda args: xUserKI.GetObjects(ki, ['me'], playerList),
                lambda args: len(args) >= 1, lambda args: xUserKI.GetObjects(ki, args, playerList))
            if not valid or not objects: return True
        else:
            objects = [PtGetLocalAvatar()]
        # (un)float them
        for object in objects:
            object.netForce(1)
            object.physics.disable() # in order for kickables to correctly re-gain physics, it has to be disabled and enabled again
            if (cmnd == 'float'):
                if not silent: ki.AddChatLine(None, 'Disabled physics for %s' % xUserKI.GetObjectName(object), 0)
            else:
                object.physics.enable()
                if not silent: ki.AddChatLine(None, 'Enabled physics for %s' % xUserKI.GetObjectName(object), 0)
        return True
    # avatar animations/appearance
    if (cmnd == 'hug'):
        PtAvatarEnterLookingAtKI()
        return True
    if (cmnd == 'unhug'):
        PtAvatarExitLookingAtKI()
        return True
    if (cmnd == 'suitup'):
        clothing = ['03_MLHand_Suit',
         '03_MRHand_Suit',
         '03_MTorso_Suit',
         '03_MLegs_Suit',
         '03_MLFoot_Suit',
         '03_MRFoot_Suit',
         '03_MHAcc_SuitHelmet',
         '03_FLHand_Suit',
         '03_FRHand_Suit',
         '03_FTorso_Suit',
         '03_FLegs_Suit',
         '03_FLFoot_Suit',
         '03_FRFoot_Suit',
         '03_FHair_SuitHelmet']
        avatar = PtGetLocalAvatar()
        avatar.netForce(1)
        for item in clothing[0:]:
            avatar.avatar.wearClothingItem(item, 0)
            avatar.avatar.tintClothingItem(item, ptColor().white(), 0)
            avatar.avatar.tintClothingItemLayer(item, ptColor().white(), 2, 1)
        avatar.avatar.saveClothing()
        if not silent: ki.AddChatLine(None, 'Got you a maintainer suit', 0)
        return True
    # commands regarding colors (fog, hair, skin, text)
    if (cmnd in ['fcol', 'fogcolor', 'skincolor', 'haircolor', 'eyecolor']):
        # data[0] is the name of the color, data[1] either nonexistant (if the color has to be determined by name)
        # or an array with the r, g and b values
        if xUserKIConfig.IsLockedAge() or (PtGetAgeName() == "cityofdimensions" and not xUserKIConfig.IsAdmin()):
            ki.DisplayErrorMessage("You are in a locked age, some KI commands are disabled here")
            return True
        (valid, data) = xUserKI.GetArg(ki, cmnd, args, 'color name>|<red> <green> <blue',
          lambda args: len(args) == 3, lambda args: (float(args[0]), float(args[1]), float(args[2])),
          lambda args: len(args) == 1, lambda args: (args[0], ))
        if not valid: return True
        colorName = arg.lower()
        color = 0
        if (len(data) == 1):
            if data[0].lower() in gColorNames:
                color = StrToColor(data[0])
            else:
                ki.DisplayErrorMessage('\'%s\' is no known color. Choose one of the following: %s' % (data[0], xUserKI.JoinList(gColorNames)))
                return True
        else:
            (r, g, b) = data
            if r > 1: r = 1
            elif r < 0: r = 0
            if g > 1: g = 1
            elif g < 0: g = 0
            if b > 1: b = 1
            elif b < 0: b = 0
            color = ptColor(r, g, b)
        # use it
        avatar = PtGetLocalAvatar()
        avatar.netForce(1)
        if cmnd in ['fcol', 'fogcolor']:
            PtConsoleNet('Graphics.Renderer.Fog.SetDefColor %f %f %f' % (color.getRed(), color.getGreen(), color.getBlue()), 1)
            if not silent: ki.DisplayStatusMessage('%s turns the fog %s' % (PtGetClientName(), colorName), 1)
        elif cmnd == 'skincolor':
            avatar.avatar.tintSkin(color)
            avatar.avatar.saveClothing()
            if not silent: ki.AddChatLine(None, 'Changed your skin color to %s' % colorName, 0)
        elif cmnd == 'haircolor':
            worn = avatar.avatar.getAvatarClothingList()
            for item in worn:
                if (item[1] == kHairClothingItem):
                    avatar.avatar.tintClothingItem(item[0], color)
                    avatar.avatar.saveClothing()
                    if not silent: ki.AddChatLine(None, 'Changed your hair color to %s' % colorName, 0)
                    return True
            ki.DisplayErrorMessage('Sorry, I can\'t find your hair.')
        elif cmnd == 'eyecolor':
            worn = avatar.avatar.getAvatarClothingList()
            for item in worn:
                if (item[1] == kFaceClothingItem):
                    avatar.avatar.tintClothingItem(item[0], color, 0)
                    avatar.avatar.tintClothingItemLayer(item[0], color, 2)
                    avatar.avatar.saveClothing()
                    if not silent: ki.AddChatLine(None, 'Changed your eye color to %s' % colorName, 0)
                    return True
            ki.DisplayErrorMessage('Sorry, I can\'t find your face.')
        return True
    # fog density
    if (cmnd in ['fogdensity', 'fdens']):
        if xUserKIConfig.IsLockedAge() or (PtGetAgeName() == "cityofdimensions" and not xUserKIConfig.IsAdmin()):
            ki.DisplayErrorMessage("You are in a locked age, some KI commands are disabled here")
            return True
        (valid, data) = xUserKI.GetArg(ki, cmnd, args, 'start distance> <end distance> <density',
          lambda args: len(args) == 3, lambda args: (float(args[0]), float(args[1]), float(args[2])))
        if not valid: return True
        (start, end, density) = data
        PtConsoleNet('Graphics.Renderer.Fog.SetDefLinear %f %f %f' % (start, end, density), 1)
        if not silent: ki.DisplayStatusMessage('%s changes the fog density (%1.2f %1.2f %1.2f)' % (PtGetClientName(), start, end, density), 1)
        return True
    # camera control
    if (cmnd == 'stopcam'):
        PtConsole('Camera.SetGlobalAccel 0')
        PtConsole('Camera.SetGlobalVelocity 0')
        if not silent: ki.AddChatLine(None, 'Your camera won\'t move anymore (sometimes it\'ll still follow the direction of the avatar, but it won\'t constantly show your back)', 0)
        return True
    if (cmnd == 'gocam'):
        PtConsole('Camera.SetGlobalAccel 40')
        PtConsole('Camera.SetGlobalVelocity 40')
        if not silent: ki.AddChatLine(None, 'Your camera should now move (almost) as usual', 0)
        return True
    # Age-specific commands
    if (cmnd == 'call'):
        age = PtGetAgeName()
        if (age == 'Negilahn'):
            (valid, what) = xUserKI.GetArg(ki, cmnd, args, 'Urwin|Monkey',
            lambda args: len(args) == 1, lambda args: args[0])
            if not valid: return True
            if what == 'Urwin':
                xUserKI.SetSDL('UrwinSpawnTimes', 0, PtGetDniTime()+2)
                if not silent: ki.DisplayStatusMessage('%s called the Urwin' % PtGetClientName(), 1)
            elif what == 'Monkey':
                xUserKI.SetSDL('MonkeySpawnTimes', 0, PtGetDniTime()+2)
                if not silent: ki.DisplayStatusMessage('%s called the Monkey' % PtGetClientName(), 1)
            else:
                ki.DisplayErrorMessage('You have to call either \'Urwin\' or \'Monkey\' (this is case sensitive!)')
        elif (age == 'Payiferen'):
            xUserKI.SetSDL('UrwinSpawnTimes', 0, PtGetDniTime()+2)
            if not silent: ki.DisplayStatusMessage('%s called the Urwin' % PtGetClientName(), 1)
        else:
            ki.DisplayErrorMessage('This command can only be used in Negilahn and Payiferen')
        return True
    if (cmnd == 'getfissure'): # this is NOT a cheat as (a) you can't link with it and (b) there usually is no way to get it more than once
        if (PtGetAgeName() == 'Personal'):
            (valid, stage) = xUserKI.GetArg(ki, cmnd, args, 'fissure stage (1-4)',
            lambda args: len(args) == 1 and args[0] in ['1', '2', '3', '4'], lambda args: args[0])
            if not valid: return True
            objectsAndResponders = {
                '1': ['FissureCarvDummy01', 'RespFissureStage01'],
                '2': ['FissureCarvDummy02', 'RespFissureStage02'],
                '3': ['FissureCarvDummy03', 'RespFissureStage03'],
                '4': ['FissureAnimRegion', 'RespFissureStage04'] }
            (objectName, responderName) = objectsAndResponders[stage]
            obj = PtFindSceneobject(objectName, 'Personal')
            resplist = obj.getResponders()
            for resp in resplist:
                if (resp.getName() == responderName):
                    atResp = ptAttribResponder(999)
                    atResp.__setvalue__(resp)
                    atResp.run(ki.key)
                    if not silent: ki.DisplayStatusMessage('%s created a fissure at stage %s' % (PtGetClientName(), stage), 1)
                    return True
            ki.DisplayErrorMessage('Error creating fissure: I could not find the correct responder')
        else:
            ki.DisplayErrorMessage('This command can only be used in Relto')
        return True
    if (cmnd in ['reltostars', 'noreltostars']):
        if PtGetAgeName() != 'Personal':
            ki.DisplayErrorMessage('This can only be done in your Relto')
            return True
        # Hide/show some objects
        for name in ['skyhigh', 'sunglow', 'sunround', 'cameraclouds']:
            object = PtFindSceneobject(name, 'Personal')
            object.netForce(1)
            if cmnd == 'reltostars': object.draw.disable()
            else: object.draw.enable()
        # Disable fog and change clear color, apply object positions
        if cmnd == 'reltostars':
            PtConsoleNet('Graphics.Renderer.Fog.SetDefLinear 0 0 0', 1)
            PtConsoleNet('Graphics.Renderer.SetClearColor .5 .5 .5', 1)
            xUserKI.ApplyStruct('reltostars2')
            if not silent: ki.AddChatLine(None, 'Decorated your Relto with some stars', 0)
        else:
            PtConsoleNet('Graphics.Renderer.Fog.SetDefLinear 1 900 2', 1)
            PtConsoleNet('Graphics.Renderer.SetClearColor .4 .4 .5', 1)
            xUserKI.ApplyStruct('noreltostars')
            if not silent: ki.AddChatLine(None, 'Removed the stars from your Relto', 0)
        return True
    # Dusitin special: Quit command
    if (cmnd == 'quit'):
        PtConsole('app.quit')
        return True
    # Disabling the KI
    if (cmnd == 'hideki'):
        (valid, time) = xUserKI.GetArg(ki, cmnd, args, 'time the KI will be disabled',
            lambda args: len(args) == 1, lambda args: int(args[0]))
        if not valid: return True
        PtForceCursorHidden()
        PtSendKIMessage(kDisableKIandBB, 0)
        PtAtTimeCallback(ki.key, time, xUserKI.kEnableTimer)
        return True
    # scripting commands
    if (cmnd == 'loadscript'):
        global gCommandList
        (valid, filename) = xUserKI.GetArg(ki, cmnd, args, 'name of scriptfile',
            lambda args: len(args) == 1, lambda args: args[0])
        if not valid: return True
        if not os.path.exists(filename):
            ki.DisplayErrorMessage('There is no file called %s in your Uru folder!' % filename)
            return True
        file = open(filename, 'r')
        gCommandList = []
        for line in file:
            line = line.replace("\n", "").replace("\r", "")
            if line.startswith('/'): gCommandList.append(line)
        if not silent: ki.AddChatLine(None, 'Successfully loaded %d scripted commands. You can now use Ctrl+Pause or Ctrl+Num (depending on your keyboard layout) to run them one after the other.' % len(gCommandList), 0)
        return True
    if (cmnd == 'wtf'):
        player = PtGetLocalPlayer()
        playerKey = PtGetAvatarKeyFromClientID(player.getPlayerID())
        avatar = playerKey.getSceneObject()
        avatar.avatar.netForce(1)
        avatar.avatar.oneShot(playerKey, 1, 1, "WTFAnim", 0, 0)
        avatarName = PtGetClientName()
        ki.DisplayStatusMessage("%s feels like WHAHOOOOKA! KAZHOOOOOOM! DOKRAAAAAH! WHAKCHAAAAAAAAAAA!" % avatarName, 1)
        return True
    if (cmnd == 'crazy'):
        player = PtGetLocalPlayer()
        playerKey = PtGetAvatarKeyFromClientID(player.getPlayerID())
        avatar = playerKey.getSceneObject()
        avatar.avatar.netForce(1)
        avatar.avatar.oneShot(playerKey, 1, 1, "Crazy", 0, 0)
        avatarName = PtGetClientName()
        ki.DisplayStatusMessage("%s feels... uhm... crazy!" % avatarName, 1)
        return True
    if (cmnd == 'wave2'):
        player = PtGetLocalPlayer()
        playerKey = PtGetAvatarKeyFromClientID(player.getPlayerID())
        avatar = playerKey.getSceneObject()
        gender = PtGetLocalAvatar().avatar.getAvatarClothingGroup()
        avatar.avatar.netForce(1)
        if (gender == 1):
            avatar.avatar.oneShot(playerKey, 1, 1, "FemaleWaveChr", 0, 0)
        else:
            avatar.avatar.oneShot(playerKey, 1, 1, "MaleWaveChr", 0, 0)
        return True
    if cmnd == 'crawl':
        PtAvatarEnterAnimMode("MaleKriech")
        name = PtGetClientName()
        ki.DisplayStatusMessage('%s starts to... crawl... somehow...' % name, 1)
        return True
    if cmnd == 'swim':
        gender = PtGetLocalAvatar().avatar.getAvatarClothingGroup()
        if gender == 1:
            anim = "FemaleSwimSlow"
        else:
            anim = "MaleSwimSlow"
        PtAvatarEnterAnimMode(anim)
        name = PtGetClientName()
        ki.DisplayStatusMessage('%s starts to swim' % name, 1)
        return True
    if cmnd == 'swimfast':
        gender = PtGetLocalAvatar().avatar.getAvatarClothingGroup()
        if gender == 1:
            anim = "FemaleSwimFast"
        else:
            anim = "MaleSwimFast"
        PtAvatarEnterAnimMode(anim)
        name = PtGetClientName()
        ki.DisplayStatusMessage('%s starts to swim' % name, 1)
        return True
    if cmnd == 'aeroplane':
        gender = PtGetLocalAvatar().avatar.getAvatarClothingGroup()
        if gender == 1:
            anim = "FemaleAeroplane"
        else:
            anim = "MaleAeroplane"
        PtAvatarEnterAnimMode(anim)
        name = PtGetClientName()
        ki.DisplayStatusMessage('%s starts to fly like an aeroplane' % name, 1)
        return True
    if cmnd == 'cod':
        ageLink = ptAgeLinkStruct()
        ageInfo = ptAgeInfoStruct()
        spawnInfo = ptSpawnPointInfo()
        ageInfo.setAgeFilename("cityofdimensions")
        spawnInfo.setName("LinkInPointGreatTree")
        ageLink.setAgeInfo(ageInfo)
        ageLink.setLinkingRules(PtLinkingRules.kOriginalBook)
        ageLink.setSpawnPoint(spawnInfo)
        ptNetLinkingMgr().linkToAge(ageLink)
        return True
    if cmnd == 'greenscreen':
        if os.path.isfile("dat/ScreenAge.age"):
            ki.AddChatLine(None, "Linking you to your greenscreen age!", 0)
            PtLinkToAge("ScreenAge")
        else:
            ki.DisplayErrorMessage("You do not have the greenscreen age!")
        return True
    return False
