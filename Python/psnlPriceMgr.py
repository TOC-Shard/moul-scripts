# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *
from PlasmaVaultConstants import *

Object = ptAttribSceneobject(1, "Price") #Pellet, Heek, Wall
Game = ptAttribString(2, "Game") #Pellet, Heek, Wall


PelletWinners = [21329] #insert KI# of winner(s)
HeekWinners = [15942] #insert KI# of winners(s)
WallWinners = [3349]


class psnlPriceMgr(ptModifier):

    def __init__(self):
        ptModifier.__init__(self)
        self.id = 7395164
        self.version = 1
        print "__init__psnlPriceMgr v.", self.version

    def OnServerInitComplete(self):
        Activate = False
        Object.sceneobject.draw.disable()
        ageVault = ptAgeVault()
        AgeInfo = ageVault.getAgeInfo()
        folder = AgeInfo.getAgeOwnersFolder()
        if (Game.value == "Pellet"):
            for Player in PelletWinners:
                if folder.hasPlayer(Player):
                    Activate = True
                    PtDebugPrint("psnlPriceMgr: You are a Pelletwinner - Activating PelletPrice")
        if (Game.value == "Heek"):
            for Player in HeekWinners:
                if folder.hasPlayer(Player):
                    Activate = True
                    PtDebugPrint("psnlPriceMgr: You are a Heekwinner - Activating HeekPrice")
        if (Game.value == "Wall"):
            for Player in WallWinners:
                if folder.hasPlayer(Player):
                    Activate = True
                    PtDebugPrint("psnlPriceMgr: You are a Wallwinner - Activating WallPrice")
        if Activate:
            Object.sceneobject.draw.enable()
