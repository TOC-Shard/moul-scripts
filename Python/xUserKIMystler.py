# -*- coding: utf-8 -*-
import string
import os
from Plasma import *
from PlasmaTypes import *
from PlasmaKITypes import *
from PlasmaVaultConstants import *
from PlasmaNetConstants import *
from PlasmaConstants import *
import xUserKI
import xUserKIConfig

def OnCommand(ki, arg, cmnd, args, playerList, silent):
    if cmnd == 'linkanim':
        (valid, activate,) = xUserKI.GetArg(ki, cmnd, args, '0|1', lambda args:(len(args) == 1), lambda args:args[0])
        if not valid:
            return True
        if (activate in ['0', '1']):
            vault = ptVault()
            if type(vault) != type(None):
                entry = vault.findChronicleEntry("DestinyLinkAnim")
                if type(entry) == type(None):
                    vault.addChronicleEntry("DestinyLinkAnim", 0, activate)
                else:
                    entry.chronicleSetValue(activate)
                    entry.save()
            ki.DisplayStatusMessage('You have set the TOC Link animation to %s' % activate, 0)
        else:
            ki.DisplayStatusMessage('You have to use /linkanim 0 or 1', 0)
        return True
    if cmnd == 'resetmarkers':
        import xCheat
        xCheat.ResetGZGame(0)
        if not silent: ki.AddChatLine(None, 'Your GZ marker games have been reset.', 0)
        return True
    if not xUserKIConfig.IsAdmin(): return False
    if cmnd == 'assassinate':
        ki.DisplayStatusMessage('OMG! %s is assassinating %s' % (PtGetClientName(), arg), 1)
        return True
    if cmnd == 'ccm':
        ki.DisplayStatusMessage(arg, 1)
        return True
    if cmnd == 'wear':
        avatar = PtGetLocalAvatar()
        try:
            avatar.netForce(1)
            avatar.avatar.wearClothingItem(arg)
            avatar.avatar.saveClothing()
        except:
            ki.DisplayErrorMessage('Unknown Problem! Maybe invalid clothing item!')
        return True
    if cmnd == 'getpillars':
        AgeName = PtGetAgeName()
        if AgeName == 'Kadish':
            xUserKI.SetSDL('PillarRoomSolved', 0, 1)
            xUserKI.SetSDL('PillarsResetting', 0, 0)
            xUserKI.SetSDL('pheight01', 0, 1)
            xUserKI.SetSDL('pheight02', 0, 4)
            xUserKI.SetSDL('pheight03', 0, 1)
            xUserKI.SetSDL('pheight04', 0, 2)
            xUserKI.SetSDL('budget', 0, 0)
            ki.DisplayStatusMessage('Solving the pillar puzzle!', 0)
        else:
            ki.DisplayStatusMessage('You have to be in Kadish!', 0)
        return True
    if cmnd == 'resetpillars':
        AgeName = PtGetAgeName()
        if AgeName == 'Kadish':
            xUserKI.SetSDL('PillarRoomSolved', 0, 0)
            xUserKI.SetSDL('PillarsResetting', 0, 1)
            ki.DisplayStatusMessage('Resetting the pillars!', 0)
        else:
            ki.DisplayStatusMessage('You have to be in Kadish!', 0)
        return True
    if cmnd == 'shroomie':
        AgeName = PtGetAgeName()
        if AgeName == 'Teledahn':
            tldnShroomieBrain.ShroomieKISpawn()
        else:
            ki.DisplayStatusMessage('You have to be in Teledahn!', 0)
        return True
    if cmnd == 'getpodsymbol':
        AgeName = PtGetAgeName()
        if AgeName in ['Negilahn',
        'Dereno',
        'Payiferen',
        'Tetsonot']:
            PodSymbol.StartSymbol()
            avatarName = PtGetClientName()
            ki.DisplayStatusMessage('%s called the pod symbol!' % avatarName, 1)
        else:
            ki.DisplayStatusMessage('You have to be in a pod age!', 0)
        return True
    if cmnd == 'openthedoor':
        AgeName = PtGetAgeName()
        if AgeName in ['EderDelin',
        'EderTsogal']:
            BlueSpiral.WinGame()
            avatarName = PtGetClientName()
            ki.DisplayStatusMessage('%s opened the door... HAAAAAX!' % avatarName, 1)
        else:
            ki.DisplayStatusMessage('You have to be in Eder Delin or Eder Tsogal!', 0)
        return True
    if cmnd == 'ahnyspherebot':
        AgeName = PtGetAgeName()
        if AgeName == 'Ahnonay':
            sphere = xUserKI.GetSDL("ahnyCurrentSphere", 0)
            if sphere == 1:
                xUserKI.SetSDL("ahnyCurrentSphere", 0, 2)
                ki.DisplayStatusMessage('A bot rotated the spheres forward!', 1)
            else:
                ki.DisplayStatusMessage('You have to be in Ahnonay Sphere 1!', 0)
        else:
            ki.DisplayStatusMessage('You have to be in Ahnonay Sphere 1!', 0)
        return True
    if cmnd == 'getbugs':
        AgeName = PtGetAgeName()
        if (AgeName == 'Gira'):
            avatar = PtGetLocalAvatar()
            currbugCount = PtGetNumParticles(avatar.getKey())
            if (currbugCount < 0):
                currbugCount = 0
            particleSystem = GiraBugs.GetParticleSystem()
            if (currbugCount != 0):
                percentToKill = 1
                PtKillParticles(0,percentToKill,avatar.getKey())
                currbugCount = 0
                PtSetLightAnimStart(avatar.getKey(), "RTOmni-BugLightTest", false)
            elif (currbugCount == 0):
                PtTransferParticlesToObject(particleSystem.value.getKey(),avatar.getKey(),10)
                currbugCount = 10
                PtSetLightAnimStart(avatar.getKey(), "RTOmni-BugLightTest", true)
            PtSetParticleDissentPoint(0,0,10000,avatar.getKey())
            vault = ptVault()
            if type(vault) != type(None):
                entry = vault.findChronicleEntry("BugsOnAvatar")
                if type(entry) == type(None):
                    vault.addChronicleEntry("BugsOnAvatar",0,str(currbugCount))
                else:
                    entry.chronicleSetValue(str(currbugCount))
                    entry.save()
            avatarName = PtGetClientName()
            ki.DisplayStatusMessage('%s got the Bugs... HAAAAAAAAX!' % avatarName, 1)
        else:
            ki.DisplayStatusMessage('You have to be in Eder Gira!', 0)
        return True
    if cmnd == 'getwedges':
        AgeName = PtGetAgeName()
        if AgeName == 'Personal':
            import xPsnlVaultSDL
            psnlSDL = xPsnlVaultSDL.xPsnlVaultSDL()
            psnlSDL['psnlBahroWedge01'] = (1,)
            psnlSDL['psnlBahroWedge02'] = (1,)
            psnlSDL['psnlBahroWedge03'] = (1,)
            psnlSDL['psnlBahroWedge04'] = (1,)
            psnlSDL['psnlBahroWedge05'] = (1,)
            psnlSDL['psnlBahroWedge06'] = (1,)
            psnlSDL['psnlBahroWedge07'] = (1,)
            psnlSDL['psnlBahroWedge08'] = (1,)
            psnlSDL['psnlBahroWedge09'] = (1,)
            psnlSDL['psnlBahroWedge10'] = (1,)
            psnlSDL['psnlBahroWedge11'] = (1,)
            psnlSDL['psnlBahroWedge12'] = (1,)
            psnlSDL['psnlBahroWedge13'] = (1,)
            ki.DisplayStatusMessage('Got you all the wedges! Please re-link!', 0)
        else:
            ki.DisplayStatusMessage('You have to be in your Relto!', 0)
        return True
    if cmnd == 'finishpellets':
        AgeName = PtGetAgeName()
        if (AgeName == 'Ercana'):
            time = PtGetDniTime()
            time = time + 10
            xUserKI.SetSDL("ercaBakeFinishTime", 0, time)
            ki.DisplayStatusMessage('Your pellets are finished in 10 seconds!', 0)
        else:
            ki.DisplayStatusMessage('You have to be in YOUR Ercana!', 0)
        return True
    if cmnd == 'flink':
        (valid, data,) = xUserKI.GetArg(ki, cmnd, args, 'object> <[list of avatars]>|<object', lambda args: len(args) >= 2,
            lambda args: (xUserKI.GetObject(ki, args[0], playerList), xUserKI.GetObjects(ki, args[1:], playerList)),
            lambda args: len(args) == 1,
            lambda args: (xUserKI.GetObject(ki, args[0], playerList), xUserKI.GetObjects(ki, ['me'], playerList)))
        if not valid or not data:
            return True
        (object, avatars) = data
        for avatar in avatars:
            PtFakeLinkAvatarToObject(avatar.getKey(), object.getKey())
        return True

    ### Christopher's stuff begins here ###
    if cmnd == 'getchronicle':
        vault = ptVault()
        entry = vault.findChronicleEntry(arg)
        if type(entry) == type(None):
            ki.DisplayStatusMessage('This value does not exist', 0)
        else:
            Value = entry.chronicleGetValue()
            ki.DisplayStatusMessage('This chronicle has a value of %s' % (Value), 0)
        return True
    return False
