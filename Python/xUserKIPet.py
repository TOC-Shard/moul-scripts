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

def OnCommand(ki, arg, cmnd, args, playerList, silent):
######Pet Commands######
    if (cmnd == 'pet'):
        #set PetType
        isvld = 1
        if (arg == 'Cat'):
            PetType = 'PetCat'
        elif (arg == 'Raven'):
            PetType = 'PetRaven'
        else:
            ki.DisplayStatusMessage('Usage: /pet <Petname>', netPropagate=0)
            ki.DisplayStatusMessage('Pets are: Cat, Raven', netPropagate=0)
            isvld = 0
        #set ChronicleValue
        if (isvld == 1):
            vault = ptVault()
            if type(vault) != type(None): #is the Vault online?
                entry = vault.findChronicleEntry('PetType')
                if (type(entry) == type(None)): #does entry exist?
                    vault.addChronicleEntry('PetType', 0, PetType)
                else:
                    oldValue = entry.chronicleGetValue()
                    entry.chronicleSetValue(PetType)
                    entry.save()
                    oldValuel = oldValue.split("t")
                    oldValue = oldValuel[1]
                    PetTypel = PetType.split("t")
                    PetType = PetTypel[1]
                    if (PetType != oldValue):
                        ki.DisplayStatusMessage('Your Pet changed from %s to %s' % (oldValue, PetType), netPropagate=0)
                    else:
                        ki.DisplayStatusMessage('You already have the Pet %s' % PetType, netPropagate=0)
            else:
                PtDebugPrint("ERROR xUserKIPet::PetType - Vault offline?")
        return True

######Additional Animations######
    if (cmnd == 'doabarrelroll'):
        player = PtGetLocalPlayer()
        playerKey = PtGetAvatarKeyFromClientID(player.getPlayerID())
        avatar = playerKey.getSceneObject()
        gender = PtGetLocalAvatar().avatar.getAvatarClothingGroup()
        avatar.avatar.netForce(1)
        if (gender == 1):
            avatar.avatar.oneShot(playerKey, 1, 1, "FemaleBarrelRoll", 0, 0)
        else:
            avatar.avatar.oneShot(playerKey, 1, 1, "MaleBarrelRoll", 0, 0)
        avatarName = PtGetClientName()
        ki.DisplayStatusMessage("%s does a barrel roll!" % avatarName)
        return True

######Other Commands#########
    if (cmnd == 'enablegps'):
        try:
            import xPsnlVaultSDL
            psnlSDL = xPsnlVaultSDL.xPsnlVaultSDL()
            psnlSDL["GPSEnabled"] = (1,)
            if (not silent):
                ki.DisplayStatusMessage('Your GPS is now enabled.', netPropagate=0)
        except:
            pass
        return True
    if cmnd == 'testage':
        PtLinkToAge("test")
        return True

######Story Commands#############
    if (cmnd == 'story'):
        arg = arg.lower()
        if arg in ['on', 'off']:
            value = arg
            vault = ptVault()
            entry = vault.findChronicleEntry('StoryOn')
            if (type(entry) == type(None)):
                vault.addChronicleEntry('StoryOn', 0, arg)
            else:
                entry.chronicleSetValue(arg)
                entry.save()
            ki.DisplayStatusMessage('Status of your Story participation: %s' % (arg), netPropagate=0)
        else:
            ki.DisplayStatusMessage('Usage: /story <on|off>', netPropagate=0)

        return True
    return False
