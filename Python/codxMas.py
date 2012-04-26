# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *
from bisect import *
import time
import datetime

xMasSuprisesdl = 'Event12'
xMasKranzsdl = 'Event14'

class codxMas(ptResponder):

    def __init__(self):
        ptResponder.__init__(self)
        self.id = 8501007
        self.version = 1


    def OnServerInitComplete(self):
        self.xMasSuprise()
        self.xMasKranz()


    def get_sunday_in_advent(self):
        dnitime = PtGetDniTime()
        isyear = int(time.strftime('%Y', time.gmtime(dnitime)))
        christmas = datetime.date(isyear, 12, 25)
        offset = datetime.timedelta(days=christmas.isoweekday())
        sundays = [christmas - offset - datetime.timedelta(weeks=week) for week in xrange(4)]
        sundays.sort()
        return sundays


    def xMasSuprise(self):
        dnitime = PtGetDniTime()
        dayNum = int(time.strftime('%d', time.gmtime(dnitime)))
        monthNum = int(time.strftime('%m', time.gmtime(dnitime)))
        sdlName = xMasSuprisesdl
        sdl = PtGetAgeSDL()
        sdl.setFlags(sdlName, 1, 1)
        sdl.sendToClients(sdlName)
        if (monthNum == 12):
            if (dayNum <= 24):
                sdl.setIndex(sdlName, 0, dayNum)
                PtDebugPrint(('codxMas: Current month is %d, day is %d - enabling' % (monthNum, dayNum)))
            else:
                sdl.setIndex(sdlName, 0, 24)
                PtDebugPrint(('codxMas: Current month is %d, day is %d - enabling' % (monthNum, dayNum)))
        else:
            sdl.setIndex(sdlName, 0, 0)
            PtDebugPrint(('codxMas: Current month is %d, day is %d - disabling' % (monthNum, dayNum)))


    def xMasKranz(self):
        dnitime = PtGetDniTime()
        sdlName = xMasKranzsdl
        sdl = PtGetAgeSDL()
        sdl.setFlags(sdlName, 1, 1)
        sdl.sendToClients(sdlName)
        dayNum = int(time.strftime('%d', time.gmtime(dnitime)))
        monthNum = int(time.strftime('%m', time.gmtime(dnitime)))
        yearNum = int(time.strftime('%Y', time.gmtime(dnitime)))
        dates = self.get_sunday_in_advent()
        adventweek = bisect(dates, datetime.date(yearNum, monthNum, dayNum))
        sdl.setIndex(sdlName, 0, adventweek)
        PtDebugPrint(('codxMas: Current Adventweek is %d' % (adventweek)))
