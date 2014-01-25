# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *
from PlasmaKITypes import *
from PlasmaVaultConstants import *
from PlasmaNetConstants import *
import os
import string

sdlBahroShout = ["islmBahroShoutLibraryRun","islmBahroShoutPalaceRun","islmBahroShoutFerryRun"]

sdlS1FinaleBahro = [    "islmS1FinaleBahroCity1","islmS1FinaleBahroCity2",\
                            "islmS1FinaleBahroCity3","islmS1FinaleBahroCity4","islmS1FinaleBahroCity5",\
                            "islmS1FinaleBahroCity6"]
pagesS1FinaleBahro = [    "TOC_bahroFlyers_city1","TOC_bahroFlyers_city2",\
                            "TOC_bahroFlyers_city3","TOC_bahroFlyers_city4","TOC_bahroFlyers_city5",\
                            "TOC_bahroFlyers_city6"]

DRCStageStateSDL = "islmDRCStageState"

EventTime = 3600

class cityofdimensions(ptResponder):

    def __init__(self):
        ptResponder.__init__(self)
        self.id = 8501000
        self.version = 1

    def OnFirstUpdate(self):
        pass

    def OnServerInitComplete(self):
        ageSDL = PtGetAgeSDL()
        
        self.ISetTimers()
        self.DRCStageState()
        
        for sdl in sdlBahroShout:
            self.SetSDL(sdl, 0, 0)
        try:
            import xPsnlVaultSDL
            psnlSDL = xPsnlVaultSDL.xPsnlVaultSDL()
            psnlSDL["GPSEnabled"] = (1,)
        except:
            pass
        
        try:
            n = 0
            for sdl in sdlS1FinaleBahro:
                ageSDL.setFlags(sdl,1,1)
                ageSDL.sendToClients(sdl)
                ageSDL.setNotify(self.key,sdl,0.0)
                val = ageSDL[sdl][0]
                if val:
                    self.ILoadS1FinaleBahro(n,1)
                n += 1
        except:
            print "ERROR!  Couldn't find all Bahro sdl, leaving default = 0"


    def OnNotify(self, state, id, events):
        pass

        
    def OnSDLNotify(self,VARname,SDLname,playerID,tag):
        ageSDL = PtGetAgeSDL()
        PtDebugPrint("cityofdimensions.OnSDLNotify():\t VARname: %s, SDLname: %s, tag: %s, value: %d" % (VARname,SDLname,tag,ageSDL[VARname][0]))

        if VARname in sdlS1FinaleBahro:
            id = sdlS1FinaleBahro.index(VARname)
            val = ageSDL[sdlS1FinaleBahro[id]][0]
            self.ILoadS1FinaleBahro(id,val)
            
            
    def OnTimer(self, TimerID):
        print ('OnTimer: callback id=%d' % TimerID)
        if (TimerID == 1):
            AgeName = PtGetAgeName()
            if (AgeName == 'cityofdimensions'):
                for sdl in sdlBahroShout:
                    self.SetSDL(sdl, 0, 1)
                PtDebugPrint('Started the Bahro Show!')
                PtAtTimeCallback(self.key, 30, 3)
        elif (TimerID == 2):
            self.ISetTimers()
        elif (TimerID == 3):
            for sdl in sdlBahroShout:
                self.SetSDL(sdl, 0, 0)
            PtDebugPrint('Debug: Bahro Show resetet!')

    def SetSDL(self, varname, index, value):
        sdl = PtGetAgeSDL()
        sdl.setFlags(varname, 1, 1)
        sdl.sendToClients(varname)
        sdl.setIndex(varname, index, value)

    def ISetTimers(self):
        DayTime = PtGetAgeTimeOfDayPercent()
        modifier = (86400 / EventTime)
        temp1 = (modifier * DayTime)
        temp2 = int(temp1)
        EventPercent = (temp1 - temp2)
        if (EventPercent == 0):
            EventPercent = 1
        LastEvent = (PtGetServerTime() - int((EventPercent * EventTime)))
        timeEventStarts = (LastEvent + EventTime)
        if (timeEventStarts > PtGetServerTime()):
            timeTillEvent = (timeEventStarts - PtGetServerTime())
            PtAtTimeCallback(self.key, timeTillEvent, 1)
        else:
            PtDebugPrint('You missed the event.')
        timeLeft = (EventTime - int((EventPercent * EventTime)))
        timeLeft += 1
        PtAtTimeCallback(self.key, timeLeft, 2)
        PtDebugPrint('Next Bahro Show starts in %d seconds' % timeLeft)

        
    def DRCStageState(NewSDLValue):
        ageSDL = PtGetAgeSDL()
        
        if ageSDL[DRCStageStateSDL][0] == 0:
            PtDebugPrint("cityofdimensions.DRCStageState: paging out DRC stage")
            PtPageOutNode("TOC_islmDRCStageState01")
            PtPageOutNode("TOC_islmDRCStageState02")
            
        elif ageSDL[DRCStageStateSDL][0] == 1:
            PtDebugPrint("cityofdimensions.DRCStageState: paging in DRC stage")
            PtPageOutNode("TOC_islmDRCStageState02")
            PtPageInNode("TOC_islmDRCStageState01")
            
        elif ageSDL[DRCStageStateSDL][0] == 2:
            PtDebugPrint("cityofdimensions.DRCStageState: paging in deco DRC stage")
            PtPageInNode("TOC_islmDRCStageState01")
            PtPageInNode("TOC_islmDRCStageState02")

        
    def ILoadS1FinaleBahro(self,bahro,state):
        print "cityofdimensions.ILoadS1FinaleBahro(): bahro = %d, load = %d" % (bahro,state)
#        if not self.sceneobject.isLocallyOwned():
#            return
        if state:
            PtPageInNode(pagesS1FinaleBahro[bahro])
        else:
            PtPageOutNode(pagesS1FinaleBahro[bahro])


    def OnBackdoorMsg(self, target, param):
        if target == "s1finale":
            if param == "on" or param == "1":
                n = 0
                for p in pagesS1FinaleBahro:
                    self.ILoadS1FinaleBahro(n,1)
                    n += 1
            elif param == "off" or param == "0":
                n = 0
                for p in pagesS1FinaleBahro:
                    self.ILoadS1FinaleBahro(n,0)
                    n += 1
        elif target == "bahroshout":
            PtAtTimeCallback(self.key, 0, 1)
