# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *
from PlasmaKITypes import *
from PlasmaVaultConstants import *
from PlasmaNetConstants import *
import os
import string

sdlBahroShout = ["islmBahroShoutLibraryRun","islmBahroShoutPalaceRun","islmBahroShoutFerryRun"]

EventTime = 3600

class cityofdimensions(ptResponder):

    def __init__(self):
        ptResponder.__init__(self)
        self.id = 8501000
        self.version = 1

    def OnFirstUpdate(self):
        pass

    def OnServerInitComplete(self):
        self.ISetTimers()
        for sdl in sdlBahroShout:
            self.SetSDL(sdl, 0, 0)
        try:
            import xPsnlVaultSDL
            psnlSDL = xPsnlVaultSDL.xPsnlVaultSDL()
            psnlSDL["GPSEnabled"] = (1,)
        except:
            pass

    def Load(self):
        pass


    def OnNotify(self, state, id, events):
        pass

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
