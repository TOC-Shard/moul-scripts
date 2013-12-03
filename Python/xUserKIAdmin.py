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
import math
from Plasma import *
from PlasmaTypes import *
from PlasmaKITypes import *
from PlasmaVaultConstants import *
from PlasmaNetConstants import *
from xPsnlVaultSDL import *
import xUserKI
import xUserKIConfig

try:
    import xUserKIData
except ImportError:
    xUserKIData = None

# tour variables
tourName = ''
tourInterval = 0
tourStep = 0
tourCam = {}
tourTimerActive = False

kLinkOutAnimName = "MaleLink"
kLinkInAnimName = "MaleLinkInChr"

# /set data
setData = {
    'city': {
        'journeys': ['islmJourneyCloth01Vis', 'islmJourneyCloth02Vis', 'islmJourneyCloth03Vis', 'islmJourneyCloth04Vis', 'islmJourneyCloth05Vis'],
        'bahro': ['islmS1FinaleBahro'],
        'guildhall': ['islmGuildHallConstructionVis', 'islmExplosionRun'],
        'meeting': ['islmTokotahMeetingsVis'],
        'harborlights': ['islmUnderwaterHarborLightsRun'],
        'menorah': ['islmMinorahVis', 'islmMinorahNight01Vis', 'islmMinorahNight02Vis', 'islmMinorahNight03Vis', 'islmMinorahNight04Vis', 'islmMinorahNight05Vis', 'islmMinorahNight06Vis', 'islmMinorahNight07Vis', 'islmMinorahNight08Vis'],
        'lakemeter': ['islmLakeLightMeterVis'],
        'tickers': ['islmCourtyardTickerVis', 'islmLibraryTickerVis'],
        'mystvbooks': ['islmReleeshanBookVis', 'islmTodelmerBookVis'],
        'librarybooks': ['islmLibraryBannersVis', 'islmLibraryBooksVis'],
        'hoodstones': ['guildHoodStoneVis', 'seretHoodStoneVis'],
        'stage': []
    },
    'Neighborhood': {
        'webcam': ['nb01WebCamVis'],
        'thanksgiving': ['nb01ThanksgivingVis'],
        'newyear': ['nb01HappyNewYearVis', 'nb01FireworksOnFountain', 'nb01FireworksOnBanner', 'nb01FireworksOnBalcony'],
        'darkshape': ['nb01DarkShapeSwimsRun', 'nb01DarkShapeSwimsEnabled'],
        'boats': ['nb01BahroBoatsRun', 'nb01BahroBoatsEnabled'],
        'ticker': ['nb01TickerVis'],
        'gzglass': [],
        'delinglass': [],
        'tsogalglass': [],
        'heek': []
    },
    'EderDelin': {
        'winter': ['dlnWinterVis']
    },
    'GreatZero': {
        'active': ['grtzGZActive']
    },
    'GreatTreePub': {
        'bahro': ['grtpDeadBahroVis']
    },
    'BaronCityOffice': {
        'tree': ['bcoChristmasVis']
    },
}

# loop variables
loopInterval = 0
loopCount = -1
loopCmd = ''
loopTimerActive = False


# Helper functions
def ExecPython(arg):
    exec arg


def GetCamera(ki, cameraName):
    age = PtGetAgeName()
    camera = []
    # if no name was specified, use the default one if available
    if not len(cameraName) or cameraName == 'default':
        if xUserKIData != None and age in xUserKIData.CameraShortcuts and len(xUserKIData.CameraShortcuts[age]) == 1:
            for name in xUserKIData.CameraShortcuts[age]:
                camera = xUserKIData.CameraShortcuts[age][name] # there will be only one camera
                break
        else:
            ki.DisplayErrorMessage('Can not choose default camera for this age - use "/list cameras" to see which ones are available, and specify it manually')
            return []
    # check if we got a shortcut or the camera name
    elif xUserKIData != None and age in xUserKIData.CameraShortcuts:
        if cameraName in xUserKIData.CameraShortcuts[age]:
            camera = xUserKIData.CameraShortcuts[age][cameraName]
    if not len(camera):
        camera = [cameraName, cameraName+".Target"]
    # now check if that camera is valid
    try:
        PtFindSceneobject(camera[0], age)
        PtFindSceneobject(camera[1], age)
        # we are done :)
        return camera
    except:
        # one of them does not exist
        ki.DisplayErrorMessage('Either %s or %s does not exist, so this is not a valid camera - use "/list cameras" to see which ones are available' % (camera[0], camera[1]))
        return []


def SetCamera(camera, pos):
    cameraSO = PtFindSceneobject(camera[0], PtGetAgeName())
    targetSO = PtFindSceneobject(camera[1], PtGetAgeName())
    cameraSO.netForce(1)
    cameraSO.physics.warp(ptPoint3(pos[0][0],pos[0][1],pos[0][2]))
    targetSO.netForce(1)
    targetSO.physics.warp(ptPoint3(pos[1][0],pos[1][1],pos[1][2]))


def GetObservePos(object, cameraHeight, cameraBehindAvi, targetHeight):
    avatarPos = object.position()

    # This crazy magic calculates a position which is 3+cameraBehindAvi units behind the avatar and 5.5+cameraHeight units above his feet
    # I tried doing the same doing matrix multiplication, but that's WAY slower - so I sticked with this code taken from the old AdminKI
    MatZero = -(object.right().getX())
    MatOne = -(object.view().getX())
    MatTwo = object.up().getX()
    MatFour = -(object.right().getY())
    MatFive = -(object.view().getY())
    MatSix = object.up().getY()
    MatTen = object.up().getZ()
    Yaxis = math.asin(MatTwo)
    CosY = math.cos(Yaxis)
    if (math.fabs(CosY) > 0.005):
        xpt = MatZero / CosY
        ypt = -(MatOne) / CosY
    else:
        xpt = MatFive
        ypt = MatFour
    RotZ = -(math.atan2(ypt,xpt))
    rotateMatrix = ptMatrix44()
    rotateMatrix.makeRotateMat(2,RotZ)
    zmoveMatrix = ptMatrix44()
    zmoveMatrix.makeTranslateMat(ptVector3(0,3+cameraBehindAvi,0))
    zmoveMatrix.rotate(2,RotZ)
    moveVec = zmoveMatrix.getTranslate(ptVector3(0,0,0))
    X = avatarPos.getX() + moveVec.getX()
    Y = avatarPos.getY() + moveVec.getY()
    Z = avatarPos.getZ() + moveVec.getZ() + 5.5 + cameraHeight
    posvec = ptVector3(X,Y,Z)
    rotateMatrix.translate(posvec)
    cameraPos = rotateMatrix.getTranslate(ptVector3(0,0,0))

    # the target position is just 5.5+cameraHeight+targetHeight above the avatar's feet
    targetPos = ptPoint3(avatarPos.getX(), avatarPos.getY(), avatarPos.getZ() + 5.5 + cameraHeight + targetHeight)

    # we're done :)
    return (cameraPos, targetPos)


# Callback functions
def OnLinkingOut(ki): # called by xUserKI
    # stop when linking
    global loopCmd, tourName
    loopCmd = ''
    tourName = ''


def OnTimer(ki, id): # called by xUserKI
    global loopInterval, loopCount, loopCmd, loopTimerActive # loop variables
    global tourName, tourInterval, tourStep, tourCam, tourTimerActive # tour variables
    if id == xUserKI.kLoopTimer:
        loopTimerActive = False
        if not len(loopCmd):
            ki.AddChatLine(None, 'Loop stopped', 0)
            return
        if (ki.SendMessage(str(loopCmd.strip()), silent=True) != None):
            ki.DisplayErrorMessage("'%s' does not seem to be a KI command" % loopCmd.strip())
        if loopCount > 0:
            loopCount = loopCount-1
        if loopCount == 0:
            ki.AddChatLine(None, 'Loop count reached, stopped it', 0)
            return
        PtAtTimeCallback(ki.key, loopInterval, xUserKI.kLoopTimer); loopTimerActive = True
        return True
    if id == xUserKI.kLinkOutAnimTimer:
        linkMgr = ptNetLinkingMgr()
        linkMgr.setEnabled(1)
        linkMgr.linkToAge(gLinkOutAnim)
        return True
    if id == xUserKI.kLinkOutAnimTimer2:
        linkMgr = ptNetLinkingMgr()
        linkMgr.setEnabled(1)
        linkMgr.linkToPlayersAge(gLinkOutAnim)
        return True
    if id == xUserKI.kTourTimer:
        tourTimerActive = False
        if not len(tourName): return
        # preparation
        age = PtGetAgeName()
        try:
            tourList = xUserKIData.CameraTours[age][tourName]
        except:
            tourName = '' # tour not found, or data module missing
            ki.DisplayErrorMessage('Specified tour not found')
            return
        # let's go
        if tourStep >= len(tourList):
            ki.AddChatLine(None, 'Tour %s has completed!' % tourName , 0)
            tourName = ''
        else:
            try:
                SetCamera(tourCam, tourList[tourStep])
                tourStep = tourStep+1
                PtAtTimeCallback(ki.key, tourInterval, xUserKI.kTourTimer); tourTimerActive = True
            except:
                ki.DisplayErrorMessage('Could not continue tour')
                tourName = ''
        return True
    return False


def OnNewAgeLoaded(ki, firstAge):
    AgeName = PtGetAgeName()
    vault = ptVault()
    if type(vault) != type(None):
        entry = vault.findChronicleEntry("DestinyLinkAnim")
        if type(entry) == type(None):
            pass
        else:
            DestinyLinkAnim = entry.chronicleGetValue()
            if (DestinyLinkAnim == '1'):
                if (not AgeName in ['StartUp',
                    'AvatarCustomization',
                    'GUI',
                    'GlobalAnimations',
                    'GlobalClothing',
                    'GlobalAvatars',
                    'GlobalMarkers',
                    'Nexus']):
                    player = PtGetLocalPlayer()
                    playerKey = PtGetAvatarKeyFromClientID(player.getPlayerID())
                    avatar = playerKey.getSceneObject()
                    avatar.avatar.netForce(1)
                    avatar.avatar.oneShot(playerKey, 1, 1, kLinkInAnimName, 0, 0)


# Main function
def OnCommand(ki, arg, cmnd, args, playerList, silent):
    global loopInterval, loopCount, loopCmd, loopTimerActive # loop variables
    global tourName, tourInterval, tourStep, tourCam, tourTimerActive # tour variables
# loop commands
    if (cmnd == 'loopstart'):
        loopCmd = ''
        (valid, data) = xUserKI.GetArg(ki, cmnd, args, 'interval> <command>|<interval> <count> <command',
          lambda args: xUserKI.IsFloat(args[0]) and (args[1].startswith('/') or ( xUserKI.IsInt(args[1]) and args[2].startswith('/') )) )
        if not valid: return True
        # get data
        loopInterval = float(args[0])
        loopCount = -1
        loopCmd = string.join(args[1:], " ")
        if not args[1].startswith('/'): # due to the GetArg args[1] must be an int in this case
            loopCount = int(args[1])
            loopCmd = string.join(args[2:], " ")
        # start timer
        OnTimer(ki, xUserKI.kLoopTimer)
        return True
    if (cmnd == 'loopstop'):
        loopCmd = ''
        return True
    if (cmnd == 'm'):
        (valid, data) = xUserKI.GetArg(ki, cmnd, args, 'command 1> & <command 2> & ... & <command n',
          lambda args: args[0].startswith('/') and string.join(args).find('&') >= 0)
        if not valid: return True
        commands = arg.split('&')
        for command in commands:
            if (ki.SendMessage(str(command.strip()), silent) != None):
                ki.DisplayErrorMessage("'%s' does not seem to be a KI command" % command.strip())
        return True
# Avatar commands
    if (cmnd == 'anim'):
        if xUserKIConfig.IsLockedAge():
            ki.DisplayErrorMessage('You are in a locked age, some KI commands are disabled here')
            return True
        targets = ['me']
        if xUserKIConfig.IsAdmin():
            targets = args[1:]
        (valid, data) = xUserKI.GetArg(ki, cmnd, args, 'animation',
            lambda args: len(args) == 1, lambda args: (args[0], xUserKI.GetPlayers(ki, targets, playerList, thisAgeOnly=True)))
        if not valid or not data[1]: return True
        if data[0] == 'list':
            if xUserKIData == None:
                ki.DisplayErrorMessage('The Offline KI data module is missing, so there are no named animations available')
            else:
                ki.AddChatLine(None, 'There are the following pre-defined animation sequences available: %s' % xUserKI.JoinList(xUserKIData.AnimLists), 0)
            return True
        if xUserKIData != None and data[0] in xUserKIData.AnimLists:
            animLists = xUserKIData.AnimLists[data[0]]
        else:
            animLists = ([data[0]], [data[0]])
        for player in data[1]:
            objKey = PtGetAvatarKeyFromClientID(player.getPlayerID())
            object = objKey.getSceneObject()
            if not silent: ki.AddChatLine(None, 'Trying to run %s on %s' % (data[0], xUserKI.GetObjectName(object)), 0)
            gender = object.avatar.getAvatarClothingGroup()
            if gender == 1: # female
                animList = animLists[1]
            else: # male and special characters
                animList = animLists[0]
            object.avatar.netForce(1)
            for anim in animList:
                object.avatar.oneShot(objKey, 1, 1, anim, 0, 0)
        return True
# object struct commands
    if (cmnd == 'printstruct'):
        (valid, objects) = xUserKI.GetArg(ki, cmnd, args, 'list of objects',
          lambda args: len(args) >= 1, lambda args: xUserKI.GetObjects(ki, args, playerList))
        if not valid or not objects: return True
        if silent: return True
        for object in objects:
            view = ('%f,%f,%f' % (object.view().getX(), object.view().getY(), object.view().getZ()))
            up = ('%f,%f,%f' % (object.up().getX(), object.up().getY(), object.up().getZ()))
            pos = ('%f,%f,%f' % (object.position().getX(),object.position().getY(),object.position().getZ()))
            ki.AddChatLine(None, '[[\'%s\'],[%s],[%s],[%s]],' % (xUserKI.GetObjectName(object), view, up, pos), 0)
        return True
    if (cmnd == 'struct'):
        if xUserKIConfig.IsLockedAge():
            ki.DisplayErrorMessage('You are in a locked age, some KI commands are disabled here')
            return True
        (valid, data) = xUserKI.GetArg(ki, cmnd, args, 'name of a struct> <[struct mode]',
            lambda args: len(args) == 1, lambda args: (args[0], 'normal'),
            lambda args: len(args) == 2, lambda args: (args[0], args[1]))
        if not valid: return True
        if not data[1] in ['normal', 'here']:
            ki.DisplayErrorMessage('There following modes are available: normal, here')
            return True
        if xUserKI.ApplyStruct(data[0], mode=data[1]):
            if not silent: ki.AddChatLine(None, 'Built struct %s' % data[0], 0)
        else:
            ki.DisplayErrorMessage('I could not find a struct called %s in this age - use "/list structs" to see which ones are available' % data[0])
        return True
# camera control commands
    if (cmnd == 'observe'):
        if xUserKIConfig.IsLockedAge():
            ki.DisplayErrorMessage('You are in a locked age, some KI commands are disabled here')
            return True
        # get data
        (valid, object) = xUserKI.GetArg(ki, cmnd, args, '[object]> <[camera name]> <[offset for camera behind avatar]> <[camera height offset]> <[target height offset]',
          lambda args: len(args) == 0, lambda args: xUserKI.GetObject(ki, 'me', playerList),
          lambda args: len(args) <= 5 and (len(args) <= 4 or xUserKI.IsFloat(args[4])) and (len(args) <= 3 or xUserKI.IsFloat(args[3])) and (len(args) <= 2 or xUserKI.IsFloat(args[2])), lambda args: xUserKI.GetObject(ki, args[0], playerList))
        if not valid or not object: return True
        cameraBehindAvi = 0.0
        cameraHeight = 0.0
        targetHeight = 0.0
        cameraName = ''
        if len(args) > 1: cameraName = args[1]
        if len(args) > 2: cameraBehindAvi = float(args[2])
        if len(args) > 3: cameraHeight = float(args[3])
        if len(args) > 4: targetHeight = float(args[4])
        camera = GetCamera(ki, cameraName)
        if not len(camera): return True

        # get and set positions
        (cameraPos, targetPos) = GetObservePos(object, cameraHeight, cameraBehindAvi, targetHeight)
        SetCamera(camera, ((cameraPos.getX(), cameraPos.getY(), cameraPos.getZ()), (targetPos.getX(), targetPos.getY(), targetPos.getZ())) )

        # do the output
        if not silent: ki.AddChatLine(None, 'The camera now observes %s' % xUserKI.GetObjectName(object), 0)
        return True
    if (cmnd == 'tour'):
        if xUserKIConfig.IsLockedAge():
            ki.DisplayErrorMessage('You are in a locked age, some KI commands are disabled here')
            return True
        tourName = ''
        (valid, tour) = xUserKI.GetArg(ki, cmnd, args, 'tour name> <[camera name]> <[interval]',
          lambda args: len(args) >= 1 and len(args) <= 3 and (len(args) <= 2 or xUserKI.IsFloat(args[2])), lambda args: args[0])
        if not valid: return True
        interval = 5.0
        cameraName = ''
        if len(args) > 1: cameraName = args[1]
        if len(args) > 2: interval = float(args[2])
        camera = GetCamera(ki, cameraName)
        if not len(camera): return True
        # get tour data
        try:
            tourList = xUserKIData.CameraTours[PtGetAgeName()][tour]
        except: # no such tour, or module missing
            ki.DisplayErrorMessage('I could not find a tour called %s in this age - use "/list tours" to see which ones are available' % tour)
            return True
        # start tour
        try:
            SetCamera(camera, tourList[0])
        except:
            ki.DisplayErrorMessage('Tour camera object not found')
            return True
        tourName = tour
        tourInterval = interval
        tourCam = camera
        tourStep = 1
        if not tourTimerActive:
            PtAtTimeCallback(ki.key, 5, xUserKI.kTourTimer); tourTimerActive = True # a five second delay to allow you to get to camera
        if not silent: ki.AddChatLine(None, 'Starting tour %s with a %1.1f sec dwell time.' % (tourName, tourInterval), 0)
        return True
    if (cmnd == 'tourstop'):
        if xUserKIConfig.IsLockedAge():
            ki.DisplayErrorMessage('You are in a locked age, some KI commands are disabled here')
            return True
        if not silent:
            if len(tourName):
                ki.AddChatLine(None, 'Stopped the currently running tour %s' % tourName, 0)
            else:
                ki.AddChatLine(None, 'There is no tour running', 0)
        tourName = ''
        return True
    if (cmnd == 'printcam'):
        (valid, cameraName) = xUserKI.GetArg(ki, cmnd, args, '[camera name]',
          lambda args: len(args) == 0, lambda args: 'default',
          lambda args: len(args) == 1, lambda args: args[0])
        if not valid: return True
        camera = GetCamera(ki, cameraName)
        if not len(camera): return True
        if silent: return True
        cameraSO = PtFindSceneobject(camera[0], PtGetAgeName())
        cameraPos = cameraSO.position()
        targetSO = PtFindSceneobject(camera[1], PtGetAgeName())
        targetPos = targetSO.position()
        # print the data string to make it easy to create tour variables with a cut and paste from chatlog
        cameraStr = ('%f,%f,%f' % (cameraPos.getX(), cameraPos.getY(), cameraPos.getZ()))
        targetStr = ('%f,%f,%f' % (targetPos.getX(), targetPos.getY(), targetPos.getZ()))
        ki.AddChatLine(None, '[(%s),(%s)],' % (cameraStr, targetStr), 0)
        return True
    if (cmnd in ['entercam', 'leavecam']):
        if xUserKIConfig.IsLockedAge():
            ki.DisplayErrorMessage('You are in a locked age, some KI commands are disabled here')
            return True
        targets = ['me']
        if xUserKIConfig.IsAdmin():
            targets = args[1:]
        (valid, data) = xUserKI.GetArg(ki, cmnd, args, 'camera name',
          lambda args: len(args) == 1, lambda args: (args[0], xUserKI.GetPlayers(ki, targets, playerList, thisAgeOnly=True)))
        if not valid or not data[1]: return True
        (cameraName, objects) = data
        camera = GetCamera(ki, cameraName)
        if not len(camera): return True
        cameraSO = PtFindSceneobject(camera[0], PtGetAgeName())
        if (cmnd == 'entercam'):
            ptCamera().undoFirstPerson()
            cameraSO.pushCutsceneCamera(0, PtGetLocalAvatar().getKey())
        else:
            cameraSO.popCutsceneCamera(PtGetLocalAvatar().getKey())
        return True

    # Admin only part
    if not xUserKIConfig.IsAdmin(): return False
    if (cmnd == 'loadpage'):
        (valid, null) = xUserKI.GetArg(ki, cmnd, args, 'page name',
          lambda args: len(args) > 0)
        if not valid: return True
        PtPageInNode(arg)
        if not silent: ki.AddChatLine(None, 'Loaded page %s' % arg, 0)
        return True
    if (cmnd == 'exec'):
        (valid, null) = xUserKI.GetArg(ki, cmnd, args, 'Python command',
          lambda args: len(args) > 0)
        if not valid: return True
        ExecPython(arg)
        return True
    if (cmnd == 'getchron'):
        (valid, name) = xUserKI.GetArg(ki, cmnd, args, 'chronicle name',
          lambda args: len(args) == 1, lambda args: args[0])
        if not valid: return True
        value = xUserKI.GetChronicle(name)
        if (value != None):
            if not silent: ki.AddChatLine(None, '%s = %s' % (name, value), 0)
        else:
            ki.DisplayErrorMessage("Chronicle '%s' doesn't exist." % name)
        return True
    if (cmnd in ['link', 'linksp']):
        if cmnd == 'link':
            (valid, data) = xUserKI.GetArg(ki, cmnd, args, 'age filename> <[list of players]',
              lambda args: len(args) >= 1, lambda args: ((args[0], 'LinkInPointDefault'), xUserKI.GetPlayers(ki, args[1:], playerList)))
        else:
            (valid, data) = xUserKI.GetArg(ki, cmnd, args, 'age filename> <spawn point name> <[list of players]',
              lambda args: len(args) >= 2, lambda args: ((args[0], args[1]), xUserKI.GetPlayers(ki, args[2:], playerList)))
        if not valid or not data[1]: return True
        # find out where to link
        onlyMe = len(data[1]) == 1 and data[1][0].getPlayerID() == PtGetLocalClientID()
        als = ptAgeLinkStruct()
        ainfo = ptAgeInfoStruct()
        ainfo.setAgeFilename(data[0][0])
        als.setAgeInfo(ainfo)
        vault = ptVault()
        vinfo = ptAgeInfoStruct()
        vinfo.setAgeFilename(data[0][0])
        vinfo = vault.getOwnedAgeLink(vinfo)
        if not onlyMe:
            if vinfo == None: return True
            als = vinfo.asAgeLinkStruct()
        als.setLinkingRules(PtLinkingRules.kOriginalBook)
        spawnInfo = ptSpawnPointInfo()
        spawnInfo.setName(data[0][1])
        als.setSpawnPoint(spawnInfo)
        if type(als) == type(None): return True
        # link the players
        linkMgr = ptNetLinkingMgr()
        linkMgr.setEnabled(1)
        for player in data[1]:
            if not silent:
                ki.AddChatLine(None, ('Linking %s to %s' % (player.getPlayerName(), data[0][0])), 0)
            if onlyMe:
                gLinkOutAnim = als               
                AgeName = PtGetAgeName()
                vault = ptVault()
                if type(vault) != type(None):
                    entry = vault.findChronicleEntry("DestinyLinkAnim")
                    if type(entry) == type(None):
                        linkMgr = ptNetLinkingMgr()
                        linkMgr.setEnabled(1)
                        linkMgr.linkToAge(als)
                    else:
                        DestinyLinkAnim = entry.chronicleGetValue()
                        if (DestinyLinkAnim == '1'):
                            if (not AgeName in ['StartUp',
                                'AvatarCustomization',
                                'GUI',
                                'GlobalAnimations',
                                'GlobalClothing',
                                'GlobalAvatars',
                                'GlobalMarkers',
                                'Nexus']):
                                player = PtGetLocalPlayer()
                                playerKey = PtGetAvatarKeyFromClientID(player.getPlayerID())
                                avatar = playerKey.getSceneObject()
                                avatar.avatar.netForce(1)
                                avatar.avatar.oneShot(playerKey, 1, 1, kLinkOutAnimName, 0, 0)
                                PtAtTimeCallback(ki.key, 5, xUserKI.kLinkOutAnimTimer)
                        else:
                            linkMgr = ptNetLinkingMgr()
                            linkMgr.setEnabled(1)
                            linkMgr.linkToAge(als)
                else:
                    linkMgr = ptNetLinkingMgr()
                    linkMgr.setEnabled(1)
                    linkMgr.linkToAge(als)
            else:
                linkMgr.linkPlayerToAge(als, player.getPlayerID())
        return True
    if (cmnd == 'linkto'):
        (valid, player) = xUserKI.GetArg(ki, cmnd, args, 'player',
          lambda args: len(args) == 1, lambda args: xUserKI.GetPlayer(ki, args[0], playerList))
        if not valid or not player: return True
        gLinkOutAnim = player.getPlayerID()
        AgeName = PtGetAgeName()
        vault = ptVault()
        if type(vault) != type(None):
            entry = vault.findChronicleEntry("DestinyLinkAnim")
            if type(entry) == type(None):
                linkMgr = ptNetLinkingMgr()
                linkMgr.setEnabled(1)
                linkMgr.linkToPlayersAge(player.getPlayerID())
            else:
                DestinyLinkAnim = entry.chronicleGetValue()
                if (DestinyLinkAnim == '1'):
                    if (not AgeName in ['StartUp',
                        'AvatarCustomization',
                        'GUI',
                        'GlobalAnimations',
                        'GlobalClothing',
                        'GlobalAvatars',
                        'GlobalMarkers',
                        'Nexus']):
                        player = PtGetLocalPlayer()
                        playerKey = PtGetAvatarKeyFromClientID(player.getPlayerID())
                        avatar = playerKey.getSceneObject()
                        avatar.avatar.netForce(1)
                        avatar.avatar.oneShot(playerKey, 1, 1, kLinkOutAnimName, 0, 0)
                        PtAtTimeCallback(ki.key, 5, xUserKI.kLinkOutAnimTimer2)
                else:
                    linkMgr = ptNetLinkingMgr()
                    linkMgr.setEnabled(1)
                    linkMgr.linkToPlayersAge(player.getPlayerID())
        else:
            linkMgr = ptNetLinkingMgr()
            linkMgr.setEnabled(1)
            linkMgr.linkToPlayersAge(player.getPlayerID())
        if not silent:
            ki.AddChatLine(None, ('Linking you to %s' % player.getPlayerName()), 0)
        return True
    if (cmnd == 'linkhere'):
        (valid, players) = xUserKI.GetArg(ki, cmnd, args, 'list of players',
          lambda args: len(args) >= 1, lambda args: xUserKI.GetPlayers(ki, args, playerList))
        if not valid or not players: return True
        # link the players
        linkMgr = ptNetLinkingMgr()
        linkMgr.setEnabled(1)
        for player in players:
            linkMgr.linkPlayerHere(player.getPlayerID()) # thanks to DarkFalkon for this line
            if not silent: ki.AddChatLine(None, 'Linking %s to you' % player.getPlayerName(), 0)
        return True
    # SDL manipulation
    if (cmnd == 'set'):
        (valid, data) = xUserKI.GetArg(ki, cmnd, args, 'option to be set> <value',
          lambda args: len(args) == 2, lambda args: (args[0], int(args[1])),
          lambda args: len(args) == 1 and args[0] in ['list', 'listall'], lambda args: (args[0], -1))
        if not valid: return True
        (option, value) = data
        # get the option data
        if option == 'listall':
            ki.AddChatLine(None, 'The following options are available: %s' % xUserKI.JoinListRec(setData), 0)
            return True
        age = PtGetAgeName()
        if not age in setData:
            ki.DisplayErrorMessage('There\'s nothing to be set in this age. Options are available in: %s' % xUserKI.JoinList(setData))
            return True
        ageData = setData[age]
        if option == 'list':
            ki.AddChatLine(None, 'The following options are available in this age: %s' % xUserKI.JoinList(ageData), 0)
            return True
        if not option in ageData:
            ki.DisplayErrorMessage('There is no option called \'%s\' in this age. Use one of the following: %s' % (option, xUserKI.JoinList(ageData)))
            return True
        # apply option
        if len(ageData[option]):
            # it's a stanard boolean option
            if value not in [0, 1]:
                ki.DisplayErrorMessage('Invalid value, allowed values are 0 and 1')
                return True
            for sdl in ageData[option]: xUserKI.SetSDL(sdl, 0, value)
        else:
            # one of the special options
            if age == 'city' and option == 'stage':
                if value not in [0, 1, 2]:
                    ki.DisplayErrorMessage('Invalid value %d - must be 0 to 2' % value)
                    return True
                xUserKI.SetSDL('islmDRCStageState', 0, value)
            elif age == 'Neighborhood' and option in ['gzglass', 'delinglass', 'tsogalglass']:
                if value not in [1, 2, 3]:
                    ki.DisplayErrorMessage('Invalid value %d - must be 1 to 3' % value)
                    return True
                values = [0, 0, 0]
                values[value-1] = 1 # everything is 0 except for the one we are speaking about
                # these are the prefices
                prefices = {'gzglass': 'nb01GZStainGlass0',
                    'delinglass': 'nb01EderDelinStainedGlass0',
                    'tsogalglass': 'nb01EderTsogalGlass0' }
                # set values
                for i in range(1, 4):
                    SDLName = '%s%dVis' % (prefices[option], i)
                    xUserKI.SetSDL(SDLName, 0, values[i-1])
            elif age == 'Neighborhood' and option == 'heek':
                if value not in [0, 1, 2, 3]:
                    ki.DisplayErrorMessage('Invalid value %d - must be 0 to 3' % value)
                    return True
                xUserKI.SetSDL('nb01Ayhoheek5Man1State', 0, value)
            else:
                ki.DisplayErrorMessage('Unexpected error - unknown special option %s' % option)
                return True
        if not silent: ki.AddChatLine(None, 'Set %s to %d' % (option, value), 0)
        return True
    if (cmnd == 'listsdl'):
        (valid, grep) = xUserKI.GetArg(ki, cmnd, args, '[filter]',
          lambda args: len(args) == 0, lambda args: (''),
          lambda args: len(args) == 1, lambda args: (args[0].lower()))
        if not valid: return True
        sdl = ptAgeVault().getAgeSDL()
        vars = sdl.getVarList()
        if len(grep): vars = filter(lambda s: s.lower().find(grep) >= 0, vars)
        if len(vars) == 0:
            ki.AddChatLine(None, 'No SDL Variable found', 0)
        else:
            ki.AddChatLine(None, '%d SDL Variable(s) found:' % len(vars), 0)
            line = ''
            for var in vars:
                if len(line): line += ', '
                line += var
            ki.AddChatLine(None, line, 0)
        return True
    if (cmnd == 'setsdl'):
        (valid, data) = xUserKI.GetArg(ki, cmnd, args, 'SDL var name> <integer value',
          lambda args: len(args) == 2, lambda args: (args[0], int(args[1])))
        if not valid: return True
        try:
            oldval = xUserKI.GetSDL(data[0], 0)
            xUserKI.SetSDL(data[0], 0, data[1])
            if not silent: ki.AddChatLine(None, 'Set SDL var %s to %d (old value: %s)' % (data[0], data[1], oldval), 0)
        except Exception, detail:
            ki.DisplayErrorMessage('Unable to set SDL var %s: %s' % (data[0], detail))
        return True
    if (cmnd == 'getsdl'):
        (valid, name) = xUserKI.GetArg(ki, cmnd, args, 'SDL var name',
          lambda args: len(args) == 1, lambda args: args[0])
        if not valid: return True
        try:
            val = xUserKI.GetSDL(name, 0)
            if not silent: ki.AddChatLine(None, 'SDL var %s has a value of %s' % (name, val), 0)
        except Exception, detail:
            ki.DisplayErrorMessage('Unable to get SDL var %s: %s' % (name, detail))
        return True
    if (cmnd == 'setpsnlsdl'):
        (valid, data) = xUserKI.GetArg(ki, cmnd, args, 'SDL var name> <integer value',
          lambda args: len(args) == 2, lambda args: (args[0], int(args[1])))
        if not valid: return True
        try:
            import xPsnlVaultSDL
            psnlSDL = xPsnlVaultSDL.xPsnlVaultSDL()
            oldval = psnlSDL[data[0]][0]
            psnlSDL[data[0]] = (data[1],)
            if not silent: ki.AddChatLine(None, 'Set Personal SDL var %s to %d (old value: %d)' % (data[0], data[1], oldval), 0)
        except Exception, detail:
            ki.DisplayErrorMessage('Unable to set Set Personal SDL var %s: %s' % (data[0], detail))
        return True
    if (cmnd == 'getpsnlsdl'):
        (valid, name) = xUserKI.GetArg(ki, cmnd, args, 'SDL var name',
          lambda args: len(args) == 1, lambda args: args[0])
        if not valid: return True
        try:
            import xPsnlVaultSDL
            psnlSDL = xPsnlVaultSDL.xPsnlVaultSDL()
            val = psnlSDL[name][0]
            if not silent: ki.AddChatLine(None, 'Personal SDL var %s has a value of %d' % (name, val), 0)
        except Exception, detail:
            ki.DisplayErrorMessage('Unable to get Set Personal SDL var %s: %s' % (name, detail))
        return True
    # Bahro control
    if (cmnd == 'bahro'):
        (valid, name) = xUserKI.GetArg(ki, cmnd, args, 'bahro name',
          lambda args: len(args) == 1, lambda args: args[0])
        if not valid: return True
        SDLVarNames = {
            'Neighborhood': { 'shouter': 'nb01BahroPedestalShoutRun' },
            'NeighborhoodMOUL': { 'shouter': 'nb01BahroPedestalShoutRun' },
            'city': {
                '1': 'islmS1FinaleBahroCity1',
                '2': 'islmS1FinaleBahroCity2',
                '3': 'islmS1FinaleBahroCity3',
                '4': 'islmS1FinaleBahroCity4',
                '5': 'islmS1FinaleBahroCity5',
                '6': 'islmS1FinaleBahroCity6',
                'ferry': 'islmBahroShoutFerryRun',
                'library': 'islmBahroShoutLibraryRun',
                'palace': 'islmBahroShoutPalaceRun' }
        }
        age = PtGetAgeName()
        if not age in SDLVarNames:
            ki.DisplayErrorMessage('There is no Bahro to run in this age - try the hood, Seret or the city')
            return True
        if not name in SDLVarNames[age]:
            ki.DisplayErrorMessage('There is no such Bahro in this age. Try one of the following: %s' % xUserKI.JoinList(SDLVarNames[age]))
            return True
        xUserKI.SetSDL(SDLVarNames[age][name], 0, 1)
        if not silent: ki.AddChatLine(None, 'Started Bahro %s' % name, 0)
        return True
    # Avatar commands
    if (cmnd == 'name'):
        (valid, null) = xUserKI.GetArg(ki, cmnd, args, 'new avatar name',
          lambda args: len(args) > 0)
        if not valid: return True
        PtChangePlayerName(arg)
        if not silent: ki.AddChatLine(None, 'You are now called %s' % arg, 0)
        return True
    if (cmnd == 'avatar'):
        (valid, avType) = xUserKI.GetArg(ki, cmnd, args, 'new avatar type',
          lambda args: len(args) == 1, lambda args: args[0])
        if not valid: return True
        if (avType.lower() not in ['female', 'male', 'drwatson', 'engberg', 'kodama', 'randmiller', 'sutherland', 'victor', 'yeesha', 'yeeshanoglow', 'zandi', 'cate', 'blake', 'bahro1', 'krabba', 'dragon', 'theluggage']):
            ki.DisplayErrorMessage('%s is not a valid avatar type. Choose one of the following: Female, Male, DrWatson, Engberg, Kodama, RandMiller, Sutherland, Victor, Yeesha, YeeshaNoGlow, Zandi, Cate, Blake, Bahro1, Krabba, Dragon, TheLuggage' % avType)
        else:
            PtChangeAvatar(avType)
            if not silent:
                ki.AddChatLine(None, 'Your new avatar type is %s. Please note that your first person camera might act strange until you restart the game.' % avType, 0)
        return True
    # Cheats
    if (cmnd == 'getjourneys'):
        if (PtGetAgeName() in ['Gira', 'Garden', 'Teledahn', 'Garrison', 'Kadish', 'Cleft']):
            import xCheat
            xCheat.GetAgeJourneyCloths(0)
            if not silent: ki.AddChatLine(None, 'Collected all the journey cloths for the current age.', 0)
        else:
            ki.DisplayErrorMessage('Can\'t collect journey cloths for your current age.')
        return True
    if (cmnd == 'growtree' or cmnd == 'shrinktree'):
        vault = ptVault()
        psnlSDL = vault.getPsnlAgeSDL()
        treePage = psnlSDL.findVar("YeeshaPage10")
        size = treePage.getInt()
        if (cmnd == 'growtree'):
            if (size >= 100):
                ki.AddChatLine(None, 'Your Relto tree already has it\'s maximal size', 0)
                return True
            treePage.setInt(size+10)
            verb = "Grew"
        if (cmnd == 'shrinktree'):
            if (size < 10):
                ki.AddChatLine(None, 'Your Relto tree already has it\'s minimal size', 0)
                return True
            treePage.setInt(size-10)
            verb = "Shrunk"
        vault.updatePsnlAgeSDL(psnlSDL)
        if not silent:
            if (PtGetAgeName() == 'Personal'): ki.AddChatLine(None, '%s your Relto tree. You may have to re-link to see the changes.' % verb, 0)
            else: ki.AddChatLine(None, '%s your Relto tree.' % verb, 0)
        return True
    if (cmnd == 'getyeeshapages'):
        import xCheat
        xCheat.GetAllYeeshaPages(0)
        if not silent:
            if (PtGetAgeName() == 'Personal'): ki.AddChatLine(None, 'Enabled all the Yeesha pages. Please re-link to see the changes.', 0)
            else: ki.AddChatLine(None, 'Enabled all the Yeesha pages.', 0)
        return True
    if (cmnd == 'getsparklies'):
        vault = ptVault()
        psnlSDL = vault.getPsnlAgeSDL()
        for n in range(1,13): # numbers 1 to 12
            name = 'psnlCalendarStone%02d' % n
            psnlSDL.findVar(name).setBool(True)
        vault.updatePsnlAgeSDL(psnlSDL)
        if not silent:
            if (PtGetAgeName() == 'Personal'): ki.AddChatLine(None, 'Enabled all the Sparklies. Please re-link to see the changes.', 0)
            else: ki.AddChatLine(None, 'Enabled all the Sparklies.', 0)
        return True
    if (cmnd == 'getzandoni'):
        import xSndLogTracks
        xSndLogTracks.SetLogMode()
        if not silent: ki.AddChatLine(None, 'Got you the Zandoni!', 0)
        return True
    if (cmnd == 'getfirstweek'):
        if (PtGetAgeName() == 'Personal'):
            xUserKI.SetSDL('FirstWeekClothing', 0, 1)
            if not silent: ki.AddChatLine(None, 'Got you the frst week clothing!', 0)
        else:
            ki.DisplayErrorMessage('You have to call this command in your Relto')
        return True
    return False
