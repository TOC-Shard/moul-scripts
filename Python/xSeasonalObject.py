# -*- coding: utf-8 -*-

from Plasma import *
from PlasmaTypes import *
import time

# Max
SDLName = ptAttribString(1, "SDL Name (Optional)")
StartDay = ptAttribString(2, "Start Day")
StartMonth = ptAttribString(3, "Start Month")
StopDay = ptAttribString(4, "Stop Day")
StopMonth = ptAttribString(5, "Stop Month")



class xSeasonalObject(ptMultiModifier, object):

    def __init__(self):
        ptMultiModifier.__init__(self)
        self.id = 8501015
        self.version = 1

    def OnFirstUpdate(self):
        self.CheckDate()

    def OnServerInitComplete(self):
        pass

    def DisableObject(self):
        ageSDL = PtGetAgeSDL()
        PtDebugPrint("xSeasonalObject.DisableObject:  Attempting to disable drawing and collision on %s..." % self.sceneobject.getName(), level=kDebugDumpLevel)
        self.sceneobject.draw.disable()
        self.sceneobject.physics.suppress(True)
        if (SDLName.value != ""):
            ageSDL.setIndex(SDLName, 0, 0)
            ageSDL.setFlags(sdlName.value, 1, 1)
            ageSDL.sendToClients(sdlName.value)
            ageSDL.setNotify(self.key, sdlName.value, 0.0)

    def EnableObject(self):
        ageSDL = PtGetAgeSDL()
        PtDebugPrint("xSeasonalObject.EnableObject:  Attempting to enable drawing and collision on %s..." % self.sceneobject.getName(), level=kDebugDumpLevel)
        self.sceneobject.draw.enable()
        self.sceneobject.physics.suppress(False)
        if (SDLName.value != ""):
            ageSDL.setIndex(SDLName, 0, 1)
            ageSDL.setFlags(sdlName.value, 1, 1)
            ageSDL.sendToClients(sdlName.value)
            ageSDL.setNotify(self.key, sdlName.value, 0.0)

    
    def CheckDate(self):
        dnitime = PtGetDniTime()
        dayNum = int(time.strftime('%d', time.gmtime(dnitime)))
        monthNum = int(time.strftime('%m', time.gmtime(dnitime)))
        
        hideObject = True
        
        StartDayIS = int(StartDay.value)
        StopDayIS = int(StopDay.value)
        StartMonthIS = int(StartMonth.value)
        StopMonthIS = int(StopMonth.value)
        
        print monthNum
        
        if monthNum == StartMonthIS or monthNum == StopMonthIS:
            if StartMonthIS == StopMonthIS:
                if dayNum >= StartDayIS and dayNum <= StopDayIS:
                    hideObject = False
            elif (monthNum == StartMonthIS and dayNum >= StartDayIS) or (monthNum == StopMonthIS and dayNum <= StopDayIS):
                hideObject = False
        elif StopMonthIS > StartMonthIS and monthNum > StartMonthIS and monthNum < StopMonthIS:
            hideObject = False
        elif StopMonthIS < StartMonthIS and (monthNum > StartMonthIS or monthNum < StopMonthIS):
            hideObject = False
            
        if (hideObject):
            self.DisableObject()
            PtDebugPrint("xSeasonalObject.CheckDate: Month and Day is in range - disabling",level=kDebugDumpLevel)
        else:
            self.EnableObject()
            PtDebugPrint("xSeasonalObject.CheckDate: Month and Day is in range - enabling",level=kDebugDumpLevel)
            
