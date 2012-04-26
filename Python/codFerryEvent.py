# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *
respRun = ptAttribResponder(1, 'resp: On Timer', netForce=1)
EventTime = 900

class codFerryEvent(ptModifier,):
    __module__ = __name__

    def __init__(self):
        ptModifier.__init__(self)
        self.id = 8501005
        self.version = 1
        print '__init__codFerryEvent v.',
        print self.version

    def OnFirstUpdate(self):
        pass

    def OnServerInitComplete(self):
        self.ISetTimers()

    def OnNotify(self, state, id, events):
        pass

    def OnSDLNotify(self, VARname, SDLname, playerID, tag):
        pass

    def OnTimer(self, TimerID):
        print ('OnTimer: callback id=%d' % TimerID)
        if (TimerID == 1):
            respRun.run(self.key)
            print 'Started the event responder!'
        elif (TimerID == 2):
            self.ISetTimers()

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
            print 'You missed the event.'
        timeLeft = (EventTime - int((EventPercent * EventTime)))
        timeLeft += 1
        PtAtTimeCallback(self.key, timeLeft, 2)
        print ('Next event starts in %d seconds' % timeLeft)
