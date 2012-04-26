# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *
import time

WeatherSDL = 'Event13' # 1 = Snow, 2 = Rain

class codWeather(ptResponder):

    def __init__(self):
        ptResponder.__init__(self)
        self.id = 8501009
        self.version = 1


    def OnServerInitComplete(self):
        self.Weather()


    def Weather(self):
        dnitime = PtGetDniTime()
        dayNum = int(time.strftime('%d', time.gmtime(dnitime)))
        monthNum = int(time.strftime('%m', time.gmtime(dnitime)))
        sdlName = WeatherSDL
        sdl = PtGetAgeSDL()
        sdl.setFlags(sdlName, 1, 1)
        sdl.sendToClients(sdlName)
        if (monthNum == 01):
            if (dayNum <= 17):
                sdl.setIndex(sdlName, 0, 1)
                PtDebugPrint(('codWeather: Current month is %d, Weather is %s - enabling' % (monthNum, sdlName)))
            else:
                sdl.setIndex(sdlName, 0, 0)
                PtDebugPrint(('codWeather: Current month is %d, Weather is %s - enabling' % (monthNum, sdlName)))
        elif (monthNum == 12):
            sdl.setIndex(sdlName, 0, 1)
            PtDebugPrint(('codWeather: Current month is %d, Weather is %s - enabling' % (monthNum, sdlName)))
        else:
            sdl.setIndex(sdlName, 0, 0)
            PtDebugPrint(('codWeather: Current month is %d, Weather is %s - disabling' % (monthNum, sdlName)))
