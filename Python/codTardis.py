# -*- coding: utf-8 -*-

from Plasma import *
from PlasmaTypes import *
import random

# Max
TardisMaster = ptAttribSceneobject(1, "Tardis Object")
respVisible = ptAttribResponder(2, "resp: Tardis Visible")
respInvisible = ptAttribResponder(3, "resp: Tardis Invisible")
TardisRegSenDeSpawn = ptAttribActivator(4, 'Tardis RegSen DeSpawn')

# Constants
kTardisWarpPoints = ["TardisSpawnZero", "TardisSpawnFerry", "TardisSpawnHarbor", "TardisSpawnLibrary", "TardisSpawnMuseum", "TardisSpawnCatwalk", "TardisSpawnGuildhallUpper"]
kTardisLightShows = ["", "TardisLightShowFerry", "TardisLightShowHarbor", "TardisLightShowLibrary", "TardisLightShowMuseum", "TardisLightShowCatwalk", "TardisLightShowGuildhallUpper"]
kTardisSDL = "Event15"
kTimerRespawnId = 1
kTimerDespawnId = 2
kDespawnTime = 15


class codTardis(ptResponder):

    def __init__(self):
        ptResponder.__init__(self)
        self.id = 8501016
        self.version = 1
        self.tardisLocation = 0
        self.tardisHold = 0


    def OnServerInitComplete(self):
        ageSDL = PtGetAgeSDL()
        ageSDL.setFlags(kTardisSDL, 1, 1)
        ageSDL.setNotify(self.key, kTardisSDL, 0)
        ageSDL.sendToClients(kTardisSDL)
        
        self.tardisLocation = ageSDL[kTardisSDL][0]
        PtDebugPrint("TARDIS is on " + kTardisWarpPoints[self.tardisLocation])
        if self.tardisLocation == 0:
            respInvisible.run(self.key, avatar = PtGetLocalAvatar(), fastforward = 1)
            self.TryRespawn()
        else:
            respVisible.run(self.key, avatar = PtGetLocalAvatar(), fastforward = 1)
            self.SetLightEnabled(self.tardisLocation, True)
        self.SetTardisPos(self.tardisLocation)


    def SetLightEnabled(self, pos, enabled):
        lightObj = PtFindSceneobject(kTardisLightShows[pos], PtGetAgeName())
        if enabled:
            lightObj.draw.enable()
        else:
            lightObj.draw.disable()


    def SetTardisPos(self, pos):
        spawnPoint = PtFindSceneobject(kTardisWarpPoints[pos], PtGetAgeName())
        TardisMaster.sceneobject.physics.warpObj(spawnPoint.getKey())


    def TryRespawn(self):
        if TardisMaster.sceneobject.isLocallyOwned():
            time = random.randint(300, 900)
            PtAtTimeCallback(self.key, time, kTimerRespawnId)
            PtDebugPrint("We are the Time Lord and will respawn the TARDIS in %d seconds" % time)

        
        
    def OnTimer(self, id):
        if id == kTimerRespawnId:
            ageSDL = PtGetAgeSDL()
            ageSDL[kTardisSDL] = (random.randint(1, len(kTardisWarpPoints) - 1),)
        if id == kTimerDespawnId:
            self.SetTardisPos(0)
            self.SetLightEnabled(self.tardisLocation, False)


    def OnNotify(self, state, id, events):
        if PtFindAvatar(events) != PtGetLocalAvatar():
            return

        # Despawn, trigger when TARDIS is visible and in our region
        ageSDL = PtGetAgeSDL()
        if id == TardisRegSenDeSpawn.id:
            if not self.tardisHold and ageSDL[kTardisSDL][0] and kTardisWarpPoints[ageSDL[kTardisSDL][0]] == events[0][3].getName():
                ageSDL[kTardisSDL] = (0,)


    def OnSDLNotify(self, VARname, SDLname, playerID, tag):
        ageSDL = PtGetAgeSDL()
        value = ageSDL[VARname][0]
        if VARname == kTardisSDL:
            PtDebugPrint("TARDIS SDL changed to %d" % value)
            if value == 0:
                respInvisible.run(self.key)
                PtAtTimeCallback(self.key, kDespawnTime, kTimerDespawnId)
                self.TryRespawn()
            else:
                self.SetTardisPos(value)
                self.SetLightEnabled(value, True)
                respVisible.run(self.key)
                self.tardisLocation = value


    def OnBackdoorMsg(self, target, param):
        if target == "TardisHold":
            self.tardisHold = param
            
