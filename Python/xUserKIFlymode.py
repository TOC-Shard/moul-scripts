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

import PlasmaControlKeys

isForward = 0
isBackward = 0
isLeft = 0
isRight = 0
isUp = 0
isDown = 0
isRotLeft = 0
isRotRight = 0
isRun = 0
isAccel = 0

spaceBarDown = 0
rotSpeed = 0.1
lastRot = 0
ySpeed = 1
xSpeed = 1
zSpeed = 1
lastX = 0
lastY = 0
lastZ = 0

# Extended Flymode
defaultLinearSpeed = 0.75
defaultRotationSpeed = 0.75
defaultCallbackRate = 0.05
currentLinearSpeed = defaultLinearSpeed
currentRotationSpeed = defaultRotationSpeed
callbackRate = defaultCallbackRate
currentStrafeMotion = 'd'

rotExtSpeed = 0.1
lastRotExt = 0

flyingObjects = [] # this is referenced from other files and even ages use it to detect whether flymode is enabled
flyIsHidden = False
flyTimerRunning = False
nPlayers = 0
synchObjects = []

# helpful constants
kAxisNames = { 'x': 0, 'y': 1, 'z': 2 }


# Helper functions
def EnableFlymode(objects, ki):
    global flyingObjects, flyIsHidden, flyTimerRunning
    if len(flyingObjects): DisableFlymode() # clear existing array
    if not len(objects): return
    for object in objects:
        object.netForce(1)
        object.physics.disable()
        if object.isAvatar(): object.physics.suppress(1)
    flyingObjects = objects
    PtDisableMovementKeys()
    PtEnableMouseMovement()
    # We might have to start the timer
    if not flyTimerRunning:
        flyTimerRunning = True
        PtAtTimeCallback(ki.key, callbackRate, xUserKI.kFlyModeTimer)


def DisableFlymode(linkingOut = False):
    global flyingObjects, flyIsHidden
    flyIsHidden = False
    if not linkingOut:
        for object in flyingObjects:
            object.netForce(1)
            object.physics.enable()
            object.physics.suppress(0)
    flyingObjects = []
    PtEnableMovementKeys()
    PtEnableMouseMovement()


# Callbacks
def OnControlKey(ki, controlKey, activeFlag):
    if not xUserKIConfig.IsAdmin(): return
    global isForward
    global isBackward
    global isLeft
    global isRight
    global isUp
    global isDown
    global isRun
    global isAccel
    global isRotLeft
    global isRotRight
    global spaceBarDown
    # keep these status keysalways up-to-date
    if (controlKey == PlasmaControlKeys.kKeyModFast):
        isRun = activeFlag
    elif (controlKey == PlasmaControlKeys.kKeyAlwaysRun):
        isAccel = activeFlag
    # enable/disable flymode via "Esc" key
    elif (controlKey == PlasmaControlKeys.kKeyExitMode):
        if activeFlag:
            if len(flyingObjects): DisableFlymode()
            else: EnableFlymode([PtGetLocalAvatar()], ki)
    # movement keys
    elif (controlKey == PlasmaControlKeys.kKeyMoveForward):
        isForward = activeFlag
    elif (controlKey == PlasmaControlKeys.kKeyMoveBackward):
        isBackward = activeFlag
    elif (controlKey == PlasmaControlKeys.kKeyStrafeLeft):
        isLeft = activeFlag
    elif (controlKey == PlasmaControlKeys.kKeyStrafeRight):
        isRight = activeFlag
    elif (controlKey == PlasmaControlKeys.kKeyRotateLeft):
        isRotLeft = activeFlag
    elif (controlKey == PlasmaControlKeys.kKeyRotateRight):
        isRotRight = activeFlag
    elif (controlKey == PlasmaControlKeys.kKeyCamZoomIn):
        isDown = activeFlag
    elif (controlKey == PlasmaControlKeys.kKeyCamZoomOut):
        isUp = activeFlag
    elif (controlKey == PlasmaControlKeys.kKeyJump):
        if spaceBarDown: isDown = activeFlag
        else: isUp = activeFlag
        if not activeFlag: spaceBarDown = not spaceBarDown # toggle down/up move on key up
    # online we update the position others see on key down & up only
    for object in flyingObjects: # this will only do something if there are objects in this array
        object.netForce(1)
        object.physics.warp(object.getLocalToWorld())


def OnNewAgeLoaded(ki, firstAge):
    if firstAge: # don't check for admin, that is not yet set - the command won't be usable without admin privileges anyway
        PtEnableControlKeyEvents(ki.key)


def OnLinkingOut(ki):
    global synchObjects
    synchObjects = []
    DisableFlymode(linkingOut = True)


def OnMemberUpdate(ki):
    global nPlayers
    if len(PtGetPlayerList()) != nPlayers:
        nPlayers = len(PtGetPlayerList())
        PtAtTimeCallback(ki.key, 4, xUserKI.kReposTimer)


def OnTimer(ki, id):
    if id == xUserKI.kReposTimer:
        for object in synchObjects:
            object.netForce(1)
            object.physics.disable()
            object.physics.warp(object.getLocalToWorld())
        for object in flyingObjects:
            object.netForce(1)
            object.physics.disable()
            object.physics.warp(object.getLocalToWorld())
            if flyIsHidden: object.draw.disable()
        return True
    if not xUserKIConfig.IsAdmin(): return False
    # due to this check, you can only use FLymode if you have the admin rights on startup already - on the other hand, it saves all the others from needlessly running this timer
    if id == xUserKI.kFlyModeTimer:
        if not len(flyingObjects):
            global flyTimerRunning
            flyTimerRunning = False
            return
        doStep()
        PtAtTimeCallback(ki.key, callbackRate, xUserKI.kFlyModeTimer)
        return True
    return False


def doStep():
    # state variables
    global isForward
    global isBackward
    global isLeft
    global isRight
    global isUp
    global isDown
    global isRotLeft
    global isRotRight
    global isRun
    global isAccel
    global isDownMode
    # action variables
    global rotSpeed
    global xSpeed
    global zSpeed
    global ySpeed
    global lastX
    global lastY
    global lastZ
    global lastRot
    global currentStrafeMotion # extended Flymode
    global rotExtSpeed
    global lastRotExt
    # save last states
    if ((isForward == 0) and (isBackward == 0)):
        ySpeed = 1
        lastY = 0
    if ((isLeft == 0) and (isRight == 0)):
        xSpeed = 1
        lastX = 0
        rotExtSpeed = 0.1
        lastRotExt = 0
    if ((isUp == 0) and (isDown == 0)):
        zSpeed = 1
        lastZ = 0
    if ((isRotLeft == 0) and (isRotRight == 0)):
        rotSpeed = 0.1
        lastRot = 0
    if (isRun == 1):
        runSpeed = 5
        runrotSpeed = 0.2
    else:
        runSpeed = 0
        runrotSpeed = 0
    xlatX = 0
    xlatY = 0
    xlatZ = 0
    rotate = 0
    rotateExt = 0
    # check current state and how we move
    if (isForward or isBackward):
        if isForward: curY = 1
        else: curY = 2
        if ((lastY == curY) and (isAccel == 1)):
            ySpeed = ySpeed + 0.2
        else:
            ySpeed = 1
        xlatY = (ySpeed + runSpeed)*currentLinearSpeed
        if isForward: xlatY = -xlatY
        lastY = curY
    if (isRight or isLeft):
        if (currentStrafeMotion == 'd'):
            if isRight: curX = 1
            else: curX = 2
            if ((lastX == curX) and (isAccel == 1)):
                xSpeed = xSpeed + 0.2
            else:
                xSpeed = 1
            xlatX = (xSpeed + runSpeed)*currentLinearSpeed
            if isRight: xlatX = -xlatX
            lastX = curX
        else:
            if isRight: curRotExt = 1
            else: curRotExt = 2
            if ((lastRotExt == curRotExt) and (isAccel == 1)):
                rotExtSpeed = rotExtSpeed + 0.02
            else:
                rotExtSpeed = 0.1
            rotateExt = (rotExtSpeed + runrotSpeed)*currentRotationSpeed
            if isRight: rotateExt = -rotateExt
            lastRotExt = curRotExt
    if (isUp or isDown):
        if isDown: curZ = 1
        else: curZ = 2
        if ((lastZ == curZ) and (isAccel == 1)):
            zSpeed = zSpeed + 0.2
        else:
            zSpeed = 1
        xlatZ = (zSpeed + runSpeed)*currentLinearSpeed
        if isDown: xlatZ = -xlatZ
        lastZ = curZ
    if (isRotLeft or isRotRight):
        if isRotLeft: curRot = 1
        else: curRot = 2
        if ((lastRot == curRot) and (isAccel == 1)):
            rotSpeed = rotSpeed + 0.02
        else:
            rotSpeed = 0.1
        rotate = (rotSpeed + runrotSpeed)*currentRotationSpeed
        if isRotLeft: rotate = -rotate
        lastRot = curRot
    # do the actual movement
    for object in flyingObjects:
        MainMatrix = object.getLocalToWorld()
        if (xlatX or xlatY or xlatZ):
            xlatMatrix = ptMatrix44()
            xlatMatrix.makeTranslateMat(ptVector3(xlatX, xlatY, xlatZ))
            MainMatrix = MainMatrix * xlatMatrix
        if rotate:
            rotateMatrix = ptMatrix44()
            rotateMatrix.makeRotateMat(2, rotate)
            MainMatrix = MainMatrix * rotateMatrix
        if rotateExt:
            rotateMatrix = ptMatrix44()
            if (currentStrafeMotion == 'x'):
                rotateMatrix.makeRotateMat(0, rotateExt)
            else:
                rotateMatrix.makeRotateMat(1, rotateExt)
            MainMatrix = MainMatrix * rotateMatrix
        object.netForce(0)
        object.physics.warp(MainMatrix)


def OnDefaultKey(ki, isShift, isCtrl, keycode):
    if not xUserKIConfig.IsAdmin(): return
    if (not isCtrl) and (not isShift):
        global currentLinearSpeed
        global currentRotationSpeed
        global callbackRate
        global currentStrafeMotion
        global lastJumpUp
        if (keycode == 120): # F9
            if (currentStrafeMotion == 'd'):
                currentStrafeMotion = 'x'
            elif (currentStrafeMotion == 'x'):
                currentStrafeMotion = 'y'
            else:
                currentStrafeMotion = 'd'
            return
        elif (keycode == 121): # F10
            for object in flyingObjects:
                newMat = ptMatrix44()
                pos = object.position()
                newMat.translate(ptVector3(pos.getX(), pos.getY(), pos.getZ()))
                object.netForce(1)
                object.physics.warp(newMat)
            return
        elif (keycode == 122): # F11
            currentLinearSpeed = defaultLinearSpeed
            currentRotationSpeed = defaultRotationSpeed
            callbackRate = defaultCallbackRate
            return
        elif (keycode == 123): # F12
            callbackRate = (0.9 * callbackRate)
            if (callbackRate < 0.005):
                callbackRate = 0.005
            return
        elif (keycode == 45): # Insert
            currentLinearSpeed = (0.8 * currentLinearSpeed)
            return
        elif (keycode == 145): # Scroll lock
            currentRotationSpeed = (0.8 * currentRotationSpeed)
            return


def OnCommand(ki, arg, cmnd, args, playerList, silent):
    global flyingObjects, flyIsHidden, synchObjects
    # object manipulation commands needing arguments
    if (cmnd == 'xyz'):
        (valid, data) = xUserKI.GetArg(ki, cmnd, args, 'relative x coordinate> <relative y coordinate> <relative z coordinate> <[list of objects]',
          lambda args: len(args) >= 3, lambda args: (float(args[0]), float(args[1]), float(args[2]), xUserKI.GetObjects(ki, args[3:], playerList)))
        if xUserKIConfig.IsLockedAge():
            ki.DisplayErrorMessage("You are in a locked age, some KI commands are disabled here")
            return True
        if not valid or not data[3]: return True
        # warp them
        for object in data[3]:
            xUserKI.WarpObjectRelative(object, data[0], data[1], data[2])
            if not silent: ki.AddChatLine(None, 'Moved %s by (%1.2f|%1.2f|%1.2f)' % (xUserKI.GetObjectName(object), data[0], data[1], data[2]), 0)
        return True
    if (cmnd in ['x', 'y', 'z']):
        (valid, data) = xUserKI.GetArg(ki, cmnd, args, 'relative %s coordinate> <[list of objects]' % cmnd,
          lambda arg: len(args) >= 1, lambda arg: (float(args[0]), xUserKI.GetObjects(ki, args[1:], playerList)))
        if xUserKIConfig.IsLockedAge():
            ki.DisplayErrorMessage("You are in a locked age, some KI commands are disabled here")
            return True
        if not valid or not data[1]: return True
        # warp them
        for object in data[1]:
            if (cmnd == 'x'):
                xUserKI. WarpObjectRelative(object, data[0], 0, 0)
            elif (cmnd == 'y'):
                xUserKI.WarpObjectRelative(object, 0, data[0], 0)
            elif (cmnd == 'z'):
                xUserKI.WarpObjectRelative(object, 0, 0, data[0])
            if not silent: ki.AddChatLine(None, 'Moved %s by %1.2f along the %s-axis' % (xUserKI.GetObjectName(object), data[0], cmnd), 0)
        return True
# object manipulation commands which don't need further arguments
    if (cmnd in ['normalize', 'repos', 'location', 'ghost', 'unghost']):
        (valid, objects) = xUserKI.GetArg(ki, cmnd, args, '[list of objects]',
          lambda args: True, lambda args: xUserKI.GetObjects(ki, args, playerList))
        if xUserKIConfig.IsLockedAge():
            ki.DisplayErrorMessage("You are in a locked age, some KI commands are disabled here")
            return True
        if not valid or not objects: return True
        # do with them what we want to do
        for object in objects:
            object.netForce(1)
            if (cmnd == 'normalize'):
                newMat = ptMatrix44()
                pos = object.position()
                newMat.translate(ptVector3(pos.getX(), pos.getY(), pos.getZ()))
                object.physics.warp(newMat)
                if not silent: ki.AddChatLine(None, 'Successfully normalized %s' % xUserKI.GetObjectName(object), 0)
            elif (cmnd == 'repos'):
                object.physics.warp(object.getLocalToWorld())
                if not silent: ki.AddChatLine(None, 'Successfully repositioned %s' % xUserKI.GetObjectName(object), 0)
            elif (cmnd == 'location' and not silent):
                pos = object.position()
                at = object.view()
                up = object.up()
                ki.AddChatLine(None, ('%s is at the position (%1.2f|%1.2f|%1.2f)' % (xUserKI.GetObjectName(object), pos.getX(), pos.getY(), pos.getZ())), 0)
                ki.AddChatLine(None, ('%s is looking at (%1.2f|%1.2f|%1.2f)' % (xUserKI.GetObjectName(object), at.getX(), at.getY(), at.getZ())), 0)
                ki.AddChatLine(None, ('%s has (%1.2f|%1.2f|%1.2f) above its head' % (xUserKI.GetObjectName(object), up.getX(), up.getY(), up.getZ())), 0)
            elif (cmnd == 'ghost'):
                object.physics.suppress(True)
                if not silent: ki.AddChatLine(None, 'Successfully ghostified %s' % xUserKI.GetObjectName(object), 0)
            elif (cmnd == 'unghost'):
                object.physics.suppress(False)
                if not silent: ki.AddChatLine(None, 'Successfully de-ghostified %s' % xUserKI.GetObjectName(object), 0)
        return True
# extended object manipulation commands needing arguments
    if (cmnd == 'scale'):
        # determine scale vector - if the first three arguments are numbers, use them for the three dimensions, othewise use only one for all
        (valid, data) = xUserKI.GetArg(ki, cmnd, args, 'scale factor> <[list of objects]>|<scale x> <scale y> <scale z> <[list of objects]',
          # all three dimeniosn defined
          lambda args: len(args) >= 3 and xUserKI.IsFloat(args[1]) and xUserKI.IsFloat(args[2]),
          lambda args: (float(args[0]), float(args[1]), float(args[2]), xUserKI.GetObjects(ki, args[3:], playerList)),
          # only one dimeniosn defined
          lambda args: len(args) >= 1,
          lambda args: (float(args[0]), float(args[0]), float(args[0]), xUserKI.GetObjects(ki, args[1:], playerList)))
        if xUserKIConfig.IsLockedAge():
            ki.DisplayErrorMessage("You are in a locked age, some KI commands are disabled here")
            return True
        if not valid or not data[3]: return True
        # scale them
        for object in data[3]:
            if object.isAvatar():
                ki.DisplayErrorMessage('%s is an avatar and can\'t be scaled' % xUserKI.GetObjectName(object))
                continue
            MainMatrix = object.getLocalToWorld()
            scaleMatrix = ptMatrix44()
            scaleMatrix.makeScaleMat(ptVector3(data[0], data[1], data[2]))
            object.netForce(1)
            object.physics.warp(MainMatrix * scaleMatrix)
            if not silent: ki.AddChatLine(None, 'Scaled %s by (%1.2f|%1.2f|%1.2f)' % (xUserKI.GetObjectName(object), data[0], data[1], data[2]), 0)
        return True
    if (cmnd == 'rot'):
        (valid, data) = xUserKI.GetArg(ki, cmnd, args, 'angle> <[axis (x|y|z)]> <[list of objects]',
          # axis defined
          lambda args: len(args) >= 2 and (args[1] in kAxisNames.keys()),
          lambda args: (float(args[0]), args[1], xUserKI.GetObjects(ki, args[2:], playerList)),
          # axis not defined
          lambda args: len(args) >= 1,
          lambda args: (float(args[0]), 'z', xUserKI.GetObjects(ki, args[1:], playerList)))
        if xUserKIConfig.IsLockedAge():
            ki.DisplayErrorMessage("You are in a locked age, some KI commands are disabled here")
            return True
        if not valid or not data[2]: return True
        # rotate them
        for object in data[2]:
            rotMatrix = ptMatrix44()
            rotMatrix.makeRotateMat(kAxisNames[data[1]], data[0]/180.0*3.1415926535897932384626)
            object.netForce(1)
            object.physics.warp(object.getLocalToWorld() * rotMatrix)
            if not silent: ki.AddChatLine(None, 'Rotated %s by %d degrees around the %s-axis' % (xUserKI.GetObjectName(object), data[0], data[1]), 0)
        return True

    # Admin only part
    if not xUserKIConfig.IsAdmin(): return False
    if cmnd == 'synch':
        (valid, objects) = xUserKI.GetArg(ki, cmnd, args, '[list of objects]',
          lambda args: len(args) >= 1, lambda args: xUserKI.GetObjects(ki, args, playerList))
        if not valid or not objects: return True
        synchObjects += objects
        if not silent: ki.AddChatLine(None, 'Objects added to synch list', 0)
        return True
    if (cmnd == 'flymode'):
        (valid, objects) = xUserKI.GetArg(ki, cmnd, args, '[list of objects]',
          lambda args: len(args) >= 1, lambda args: xUserKI.GetObjects(ki, args, playerList),
          lambda args: len(args) == 0, lambda args: xUserKI.GetObjects(ki, ['me'], playerList)) # default to local player ("me")
        if not valid or not objects: return True
        # release previously bound objects
        if len(flyingObjects): ki.DisplayErrorMessage('You are already flying!')
        else:
            EnableFlymode(objects, ki)
            if not silent: ki.AddChatLine(None, 'Enabled Flymode', 0)
        return True
    if (cmnd == 'noflymode'):
        if not len(flyingObjects): ki.DisplayErrorMessage('You are not flying curretnly!')
        else:
            if flyIsHidden:
                ki.AddChatLine(None, 'Disabled permanent hiding of objects without showing these objects to you - they are now just normally hidden', 0)
            DisableFlymode() # this is put in a helper function to be able to provide other ways of controling flymode
            if not silent: ki.AddChatLine(None, 'Disabled Flymode', 0)
        return True
    # object manipulation commands needing arguments
    if cmnd == 'cicheck':
        (valid, objects,) = xUserKI.GetArg(ki, cmnd, args, '[list of objects]', lambda args:(len(args) >= 1),
            lambda args:xUserKI.GetObjects(ki, args, playerList),
            lambda args:(len(args) == 0),
            lambda args:xUserKI.GetObjects(ki, ['me'], playerList))
        if not valid or not objects:
            return True
        for object in objects:
            xUserKI.WarpObjectRelative(object, 0, 0, 0)
            if not silent:
                ki.AddChatLine(None, ('Object has coordinate interface!'), 0)
        return True
    if (cmnd in ['hide', 'show']):
        (valid, objects) = xUserKI.GetArg(ki, cmnd, args, '[list of objects]',
          lambda args: True, lambda args: xUserKI.GetObjects(ki, args, playerList, mustHaveCoord = False))
        if not valid or not objects: return True
        # hide/show them
        for object in objects:
            object.netForce(1)
            if (cmnd == 'hide'):
                object.draw.disable()
                if not silent: ki.AddChatLine(None, 'Successfully hid %s' % xUserKI.GetObjectName(object), 0)
            elif (cmnd == 'show'):
                object.draw.enable()
                if not silent: ki.AddChatLine(None, 'Successfully showed %s' % xUserKI.GetObjectName(object), 0)
        if (not len(args)) and len(flyingObjects):
            flyIsHidden = (cmnd == 'hide')
            if not silent:
                if flyIsHidden:
                    ki.AddChatLine(None, 'These objects are now permanently hidden, even new players joining will not see them', 0)
                else:
                    ki.AddChatLine(None, 'Permanent hiding is now disabled', 0)
        elif flyIsHidden and cmnd == 'show' and not silent:
            ki.AddChatLine(None, 'You just showed an object while permanent hiding of controlled objects was enabled, so you might be faced to strange happenings', 0)
        return True
    if (cmnd == 'warp'):
        (valid, data) = xUserKI.GetArg(ki, cmnd, args, 'x coordinate> <y coordinate> <z coordinate> <[list of objects]>|<warp location> <[list of objects]>|<target object> <[list of objects]',
          # manually set location
          lambda args: len(args) >= 3 and xUserKI.IsInt(args[0]) and xUserKI.IsInt(args[1]) and xUserKI.IsInt(args[2]),
          lambda args: ((float(args[0]), float(args[1]), float(args[2])), xUserKI.GetObjects(ki, args[3:], playerList)),
          # used warp point or target object
          lambda args: len(args) >= 1,
          lambda args: (str(args[0]), xUserKI.GetObjects(ki, args[1:], playerList)))
        if not valid or not data[1]: return True
        (location, objects) = data
        if type(location) == type(''): # a warp point or a target object
            try:
                import xUserKIData
                location = xUserKIData.WarpPoints[PtGetAgeName()][location]
            except: # Warp point does not exist, or data module is missing
                object = xUserKI.GetObject(ki, location, playerList)
                if not object: return True
                location = (object.position(), 'to %s' % xUserKI.GetObjectName(object), None) # same format as WarpPoints
        else: # a manually set location
            location = (ptPoint3(location[0], location[1], location[2]), 'to (%1.2f|%1.2f|%1.2f)' % (location[0], location[1], location[2]), None) # same format as WarpPoints
        # warp them
        for object in objects:
            xUserKI.WarpObjectToPos(object, location[0].getX(), location[0].getY(), location[0].getZ())
            if location[2] == True: # disable physics
                object.physics.disable()
            elif location[2] == False: # enable physics
                if not object in xUserKIFlymode.flyingObjects:
                    object.physics.enable()
            if not silent: ki.AddChatLine(None, 'Warped %s %s' % (xUserKI.GetObjectName(object), location[1]), 0)
        return True
    return False
