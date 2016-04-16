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
import xUserKIConfig

try:
    import xUserKIData
except ImportError:
    xUserKIData = None

# Global info variables and configuration
gUserKIVersion = '3.8'
gUserKIExtensionModuleNames = ['xUserKIBase', 'xUserKIHelp', 'xUserKIPet', 'xUserKIAdmin', 'xUserKIFlymode', 'xUserKIMystler']
# Some commands are overwritten, so their order must be the one in which they are mentioned below:
#  /link is in xUserKIAdmin and xUserKIBase

# helper variables
gFirstAge = True
gAgeInitialized = False

# Timer IDs (range 3000-3999)
# 3000-3049 is reserved for xUserKIBase
kEnableTimer = 3000
# 3050-3099 is reserved for xUserKIFlymode
kReposTimer = 3050
kFlyModeTimer = 3055
# 3100-3149 is reserved for xUserKIAdmin
kLoopTimer = 3100
kTourTimer = 3102
# Mystler's stuff
kLinkOutAnimTimer = 3116
kLinkOutAnimTimer2 = 3118

# load extension modules
gUserKIExtensionModules = []
for name in gUserKIExtensionModuleNames:
    try: gUserKIExtensionModules.append(__import__(name))
    except ImportError: pass


# Global helper functions
def RunUserKIExtensions(name, call, everyone = True):
    # check for the function in all modules
    for module in gUserKIExtensionModules:
        try: f = getattr(module, name)
        except AttributeError: continue
        if call(f) and not everyone: return True
    return False


def GetArg(ki, cmnd, args, usage, condition1, callback1 = 0, condition2 = 0, callback2 = 0):
    if len(args) == 1 and args[0] == 'help':
        ki.DisplayStatusMessage('Usage: /%s <%s>' % (cmnd, usage), 0)
        return (False, 0)
    try:
        if (condition1(args)):
            if callback1 == 0:
                return (True, 0)
            else:
                return (True, callback1(args))
        if condition2 != 0 and callback2 != 0:
            if (condition2(args)):
                return (True, callback2(args))
    except Exception, detail:
        #PtPrintToScreen('Error: %s' % detail)
        pass
    ki.DisplayErrorMessage('Usage: /%s <%s>' % (cmnd, usage))
    return (False, 0)


def GetObject(ki, name, playerList, mustHaveCoord = True):
    # check for avatar
    player = GetPlayer(ki, name, playerList, showError=False)
    if player and xUserKIConfig.IsAdmin():
        try: return PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject() # the player might be in a different age
        except: pass
    # check for scene object
    objectExists = False
    try:
        object = PtFindSceneobject(name, PtGetAgeName())
        if object == None: raise Exception('Object not found')
        objectExists = True
        if mustHaveCoord: testPos = object.position()
        return object
    except: pass
    if objectExists:
        ki.DisplayErrorMessage('Object %s does not have a coordinate interface' % name)
    else:
        ki.DisplayErrorMessage('Could not find object %s in this age' % name)
    return None


def GetPlayer(ki, name, playerList, showError = True, thisAgeOnly = False):
    name = name.lower()
    if name == 'me':
        return PtGetLocalPlayer()
    # ok, look for the player
    result = None
    for player in playerList: # There are also folders in that list, so make sure we only process the correct types
        if isinstance(player, ptVaultNodeRef):
            player = player.getChild().upcastToPlayerInfoNode()
            if (player.playerGetName().lower().replace(' ', '') == name or str(player.playerGetID()) == name):
                result = ptPlayer(player.playerGetName(), player.playerGetID())
                break
        elif isinstance(player, ptPlayer):
            if (player.getPlayerName().lower().replace(' ', '') == name or str(player.getPlayerID()) == name):
                result = player
                break
    if isinstance(result, ptPlayer):
        if thisAgeOnly and not PtValidateKey(PtGetAvatarKeyFromClientID(result.getPlayerID())):
            if showError: ki.DisplayErrorMessage('Player %s is not in your age' % result.getPlayerName())
            return None
        return result
    if showError: ki.DisplayErrorMessage('Could not find player %s' % name)
    return None


def GetObjects(ki, names, playerList, mustHaveCoord = False):
    objects = []
    if not len(names):
        try:
            import xUserKIFlymode
            if len(xUserKIFlymode.flyingObjects):
                return xUserKIFlymode.flyingObjects
        except ImportError: pass # don't fail if xUserKIFlymode does not exist
        names = ['me']
    for name in names:
        if name == 'all' and xUserKIConfig.IsAdmin():
            # add all players from current age except for myself
            agePlayers = PtGetPlayerList()
            if not len(agePlayers):
                ki.DisplayErrorMessage('There is nobody besides you in the current age, so \'all\' is nobody')
            # append the scene objects of all players to the list
            for player in agePlayers:
                objects.append(PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject())
        else:
            expandedNames = []
            try: # check if it is an object list
                expandedNames = xUserKIData.ObjectLists[PtGetAgeName()][name]
            except: # not an object list, or no data found
                try: # check if it is a struct list
                    for element in xUserKIData.StructLists[PtGetAgeName()][name]:
                        expandedNames.append(element[0][0])
                except: # not a struct list either, or no data found
                    expandedNames = [name] # just add this one
            for expandedName in expandedNames:
                object = GetObject(ki, expandedName, playerList, mustHaveCoord)
                if not object: return 0
                objects.append(object)
    return objects


def GetPlayers(ki, names, playerList, thisAgeOnly = False):
    players = []
    if not len(names):
        names = ['me']
    for name in names:
        if name == 'all':
            # add all players from current age except for myself
            agePlayers = PtGetPlayerList()
            if not len(agePlayers):
                ki.DisplayErrorMessage('There is nobody besides you in the current age, so \'all\' is nobody')
            # append this list to the one we already have
            for player in agePlayers:
                players.append(player)
        else:
            player = GetPlayer(ki, name, playerList, thisAgeOnly=thisAgeOnly)
            if not player: return 0
            players.append(player)
    return players


def GetSDL(varname, index):
    sdl = PtGetAgeSDL()
    return sdl[str(varname)][index]


def SetSDL(varname, index, value):
    sdl = PtGetAgeSDL()
    sdl.setFlags(varname,1,1)
    sdl.sendToClients(varname)
    sdl.setIndex(varname,index,value)


def JoinListRec(list):
    # get list sorted
    if type(list) == type({}): # it is a dict
        sortedList = list.keys()
    else:
        sortedList = list
    sortedList.sort()
    # assemble result
    result = ''
    for item in sortedList:
        result += '\n%s: %s' % (item, JoinList(list[item]))
    return result


def JoinList(list):
    if type(list) == type({}): # it is a dict
        list = list.keys()
    list.sort()
    return string.join(list, ', ')


def WarpObjectRelative(object, x, y, z, localAxes = False):
    matrix = object.getLocalToWorld()
    if localAxes: # move relative to object axes
        translateMatrix = ptMatrix44()
        translateMatrix.makeTranslateMat(ptVector3(x, y, z))
        matrix = matrix * translateMatrix
    else: # move relative to global axes
        matrix.translate(ptVector3(x, y, z))
    object.netForce(1)
    object.physics.warp(matrix)


def WarpObjectToPos(object, x, y, z):
    pos = object.position()
    matrix = object.getLocalToWorld()
    matrix.translate(ptVector3(x-pos.getX(), y-pos.getY(), z-pos.getZ()))
    object.netForce(1)
    object.physics.warp(matrix)


def IsFloat(number):
    try:
        test = float(number)
        return True
    except:
        return False


def IsInt(number):
    try:
        test = int(number)
        return True
    except:
        return False


def GetObjectName(object):
    if object.isAvatar():
        return PtGetClientName(object.getKey())
    return object.getName()


def GetChronicle(name, default = None):
    vault = ptVault()
    entry = vault.findChronicleEntry(name)
    if (type(entry) != type(None)):
        return str(entry.chronicleGetValue())
    return default


def SetChronicle(name, value):
    vault = ptVault()
    entry = vault.findChronicleEntry(name)
    if (type(entry) != type(None)):
        entry.chronicleSetValue(value)
        entry.save()
    else:
        vault.addChronicleEntry(name, 1, value) # 1 is the type, but don't ask me what it means


def ApplyStruct(structName, mode = 'normal'):
    age = PtGetAgeName()
    # get struct data
    try:
        struct = xUserKIData.StructLists[age][structName]
    except:
        return False # no data available, or the struct does not exist
    if mode == 'here':
        avatarPos = PtGetLocalAvatar().position()
        deltaX = avatarPos.getX() - struct[0][3][0]
        deltaY = avatarPos.getY() - struct[0][3][1]
        deltaZ = avatarPos.getZ() - struct[0][3][2]
    # apply it
    for element in struct:
        object = PtFindSceneobject(element[0][0], age)
        # calculate matrix
        objview = ptPoint3(element[1][0], element[1][1], element[1][2])
        objup = ptVector3(-element[2][0], -element[2][1], -element[2][2])
        if mode == 'here':
            objpos = ptVector3(element[3][0] + deltaX, element[3][1] + deltaY, element[3][2] + deltaZ)
        else:
            objpos = ptVector3(element[3][0], element[3][1], element[3][2])
        matrix = ptMatrix44()
        matrix.make(ptPoint3(0,0,0),objview,objup)
        if len(element) == 5:
            matrix.scale(ptVector3(element[4][0], element[4][1], element[4][2]))
        matrix.translate(objpos)
        # apply it
        object.netForce(1)
        object.draw.enable()
        object.physics.disable()
        object.physics.warp(matrix)
    return True


def AgeInitialized():
    # I had some code here attempting to access SDL, but it would crash the game when linking to Gira...?!?
    global gAgeInitialized
    return gAgeInitialized



# Relay callback functions
def OnEarlyInit(ki):
    RunUserKIExtensions('OnEarlyInit', lambda f: f(ki))


def OnNewAgeLoaded(ki):
    global gFirstAge, gAgeInitialized
    gAgeInitialized = True
    RunUserKIExtensions('OnNewAgeLoaded', lambda f: f(ki, gFirstAge))
    gFirstAge = False


def OnAvatarSpawn(ki):
    RunUserKIExtensions('OnAvatarSpawn', lambda f: f(ki))


def OnMemberUpdate(ki):
    RunUserKIExtensions('OnMemberUpdate', lambda f: f(ki))


def OnLinkingOut(ki):
    global gAgeInitialized
    gAgeInitialized = False
    RunUserKIExtensions('OnLinkingOut', lambda f: f(ki))


def OnTimer(ki, id):
    RunUserKIExtensions('OnTimer', lambda f: f(ki, id), everyone=False)


def OnControlKey(ki, controlKey, activeFlag):
    RunUserKIExtensions('OnControlKey', lambda f: f(ki, controlKey, activeFlag))


def OnDefaultKey(ki, isShift, isCtrl, keycode):
    RunUserKIExtensions('OnDefaultKey', lambda f: f(ki, isShift, isCtrl, keycode))


def OnCommand(ki, command, silent):
    try:
        parts = command.split()
        if not len(parts): return False
        if (parts[0].lower() == 'info'):
            ki.DisplayStatusMessage('This is based on the Offline KI %s by diafero' % gUserKIVersion, 0)
            ki.DisplayStatusMessage('Also containing contributions by Agenotfound, Almlys, a\'moaca\', Ashtar, cjkelly1, DarkFalkon, D\'Lanor, Dustin, LCC, GPNMilano, H\'astin, Hoikas, Kaelis Ebonrai, Sirius, Zrax and unknown AdminKI and UserKI programmers', 0)
            ki.DisplayStatusMessage('Updated and ported for TOC-MOUL usage by Mystler', 0)
            return True
        # relay event
        return RunUserKIExtensions('OnCommand', lambda f: f(ki, command[len(parts[0])+1:], parts[0].lower(), parts[1:], ki.BKPlayerList, silent), everyone=False)
    except Exception, detail:
        ki.DisplayErrorMessage('Error while handling command \'%s\': %s' % (command, detail))
        return True
