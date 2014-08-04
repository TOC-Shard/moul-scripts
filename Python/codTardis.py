# -*- coding: utf-8 -*-

from Plasma import *
from PlasmaTypes import *
from PlasmaKITypes import *
from PlasmaVaultConstants import *
from PlasmaNetConstants import *
from xPsnlVaultSDL import *

import random

# Max
TardisMaster = ptAttribSceneobject(1, "Tardis Object")
respVisible = ptAttribResponder(2, "resp: Tardis Visible")
respInvisible = ptAttribResponder(3, "resp: Tardis Invisible")
TardisRegSenDeSpawn = ptAttribActivator(4, 'Tardis RegSen DeSpawn')

# Global
TardisWarpPoints = ["TardisSpawnZero", "TardisSpawnFerry", "TardisSpawnHarbor", "TardisSpawnLibrary", "TardisSpawnMuseum", "TardisSpawnCatwalk", "TardisSpawnGuildhallUpper"]
TardisLightShows = ["", "TardisLightShowFerry", "TardisLightShowHarbor", "TardisLightShowLibrary", "TardisLightShowMuseum", "TardisLightShowCatwalk", "TardisLightShowGuildhallUpper"]

TardisSDL = "Event15"
TardisVisible = 0
TardisIsOnSpawnPoint = 0
TardisHold = 0

# Timer
kTardisSpawn = 1
kTardisNextSpawn = 2
kTardisNextSpawnTime = 60

class codTardis(ptResponder):

    def __init__(self):
        ptResponder.__init__(self)
        self.id = 8501016
        self.version = 1
        print '__init__codTardis v.',
        print self.version


    def OnFirstUpdate(self):
        pass


    def OnServerInitComplete(self):
        ageSDL = PtGetAgeSDL()
        ageSDL.setFlags(TardisSDL,0,1)
        ageSDL.setNotify(self.key, TardisSDL, 0.0)
        ageSDL.sendToClients(TardisSDL)
        
        self.TardisWho()


    def TardisWho(self):
        global TardisIsOnSpawnPoint
        global TardisVisible
        ageSDL = PtGetAgeSDL()
        
        TardisIsSDL = ageSDL[TardisSDL][0]
        
        if TardisIsSDL == 0:
            respInvisible.run(self.key,avatar=PtGetLocalAvatar(),fastforward=1)
            if not len(PtGetPlayerList()):
                PtAtTimeCallback(self.key,60,kTardisNextSpawn)
            TardisVisible = 0
        else:
            TardisIsOnSpawnPoint = int(TardisIsSDL)
            self.TardisMove(TardisIsOnSpawnPoint)
            respVisible.run(self.key,avatar=PtGetLocalAvatar(),fastforward=1)
            TardisVisible = 1
            
        self.TardisLightShowSwitch(TardisIsOnSpawnPoint)


    def TardisSetSpawnTime(self):
        global kTardisNextSpawnTime
        
        kTardisNextSpawnTime = random.randint(300,900)
        
        
    def TardisSetPos(self, PosNum = 0):
        global TardisVisible
        global TardisNewSpawnPoint
        
        ageSDL = PtGetAgeSDL()
        
        PosNum = int(PosNum)
        if PosNum == 0:
            TardisNewSpawnPoint = random.randint(1,len(TardisWarpPoints)-1)
        else:
            TardisNewSpawnPoint = PosNum
        
        ageSDL[TardisSDL] = (TardisNewSpawnPoint,)
        
        print "codTardis.TardisSetPos: Spawn on ", TardisNewSpawnPoint
        
        
    def TardisSpawn(self, TardisIsOnSpawnPoint):
        TardisIsOnSpawnPoint = int(TardisIsOnSpawnPoint)
        
        self.TardisMove(TardisIsOnSpawnPoint)
        self.TardisLightShowSwitch(TardisIsOnSpawnPoint)
        respVisible.run(self.key)


    def TardisDeSpawn(self):
        global TardisVisible
        
        TardisVisible = 0
        
        respInvisible.run(self.key)
        print "Tardis go away"
        PtAtTimeCallback(self.key,15,0)
        
        
    def TardisMove(self, TardisIsOnSpawnPoint):
        global TardisVisible
        
        TardisIsOnSpawnPoint = int(TardisIsOnSpawnPoint)
        
        if TardisIsOnSpawnPoint != 0:
            TardisVisible = 1
            
        print "Tardis Spawn on " + TardisWarpPoints[TardisIsOnSpawnPoint]
        
        objectis = PtFindSceneobject(TardisWarpPoints[TardisIsOnSpawnPoint], PtGetAgeName())
        
        TardisMaster.sceneobject.netForce(1)
        TardisMaster.sceneobject.physics.warpObj(objectis.getKey())
        TardisMaster.sceneobject.netForce(0)


    def TardisLightShowSwitch(self, TardisIsOnSpawnPoint):
        for i in range(len(TardisLightShows)):
            if i != 0:
                objectis = PtFindSceneobject(TardisLightShows[i], PtGetAgeName())
                objectis.netForce(1)
            
                if TardisIsOnSpawnPoint == i:
                    objectis.draw.enable()
                    #PtDebugPrint(('DEBUG: codTardis.TardisLightShowSwitch:  Attempting to enable drawing on %s...' % TardisLightShows[i]))
                else:
                    objectis.draw.disable()
                    #PtDebugPrint(('DEBUG: codTardis.TardisLightShowSwitch:  Attempting to disable drawing on %s...' % TardisLightShows[i]))
                
                objectis.netForce(0)
        
        
    def OnTimer(self,id):
        global kTardisNextSpawnTime
        global TardisVisible
        
        if id == kTardisSpawn:
            self.TardisSetSpawnTime()
            print "Tardis Spawn in %s sec." % kTardisNextSpawnTime
            PtAtTimeCallback(self.key,kTardisNextSpawnTime,kTardisNextSpawn)
        elif id == kTardisNextSpawn:
            if TardisVisible == 0:
                self.TardisSetPos(0)
        elif id == 0:
            self.TardisMove(0)
            self.TardisLightShowSwitch(0)
    
    
    def OnNotify(self, state, id, events):
        global TardisIsOnSpawnPoint
        global TardisVisible
        global TardisHold
        
        ageSDL = PtGetAgeSDL()
        
        print "codTardis.OnNotify:  state=%f id=%d events=" % (state,id),events
        
        if (id == TardisRegSenDeSpawn.id):
            if TardisHold == 0:
                if TardisVisible == 1:
                    if TardisWarpPoints[ageSDL[TardisSDL][0]] == events[0][3].getName():
                        ageSDL[TardisSDL] = (0,)
                        if (PtFindAvatar(events) == PtGetLocalAvatar()):
                            PtAtTimeCallback(self.key,10,kTardisSpawn)
        #elif (id == respVisible.id):
        #    ageSDL[TardisSDL] = (TardisIsOnSpawnPoint,)
        #elif (id == respInvisible.id):
        #    ageSDL[TardisSDL] = (0,)


    def OnSDLNotify(self,VARname,SDLname,playerID,tag):
        global TardisVisible
        
        ageSDL = PtGetAgeSDL()
        value = ageSDL[VARname][0]
        #print "codTardis.OnSDLNotify: VARname = ",VARname," SDLname = ",SDLname," playerID = ",playerID," tag = ",tag," value = ",value
        
        if (VARname == TardisSDL):
            if value == 0:
                self.TardisDeSpawn()
                PtAtTimeCallback(self.key,900,kTardisSpawn)
            else:
                if TardisVisible == 0:
                    self.TardisSpawn(value)


    def OnBackdoorMsg(self, target, param):
        global TardisHold
        if target == "Tardis":
            self.TardisSetPos(param)
        elif target == "TardisHold":
            TardisHold = param
        elif target == "TardisVis":
            print TardisVisible
            
