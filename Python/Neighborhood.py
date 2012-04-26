# -*- coding: utf-8 -*-
""" *==LICENSE==*

CyanWorlds.com Engine - MMOG client, server and tools
Copyright (C) 2011  Cyan Worlds, Inc.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Additional permissions under GNU GPL version 3 section 7

If you modify this Program, or any covered work, by linking or
combining it with any of RAD Game Tools Bink SDK, Autodesk 3ds Max SDK,
NVIDIA PhysX SDK, Microsoft DirectX SDK, OpenSSL library, Independent
JPEG Group JPEG library, Microsoft Windows Media SDK, or Apple QuickTime SDK
(or a modified version of those libraries),
containing parts covered by the terms of the Bink SDK EULA, 3ds Max EULA,
PhysX SDK EULA, DirectX SDK EULA, OpenSSL and SSLeay licenses, IJG
JPEG Library README, Windows Media SDK EULA, or QuickTime SDK EULA, the
licensors of this Program grant you additional
permission to convey the resulting work. Corresponding Source for a
non-source form of such a combination shall include the source code for
the parts of OpenSSL and IJG JPEG Library used as well as that of the covered
work.

You can contact Cyan Worlds, Inc. by email legal@cyan.com
 or by snail mail at:
      Cyan Worlds, Inc.
      14617 N Newport Hwy
      Mead, WA   99021

 *==LICENSE==* """
"""
Module: Neighborhood.py
Age: Neighborhood
Date: August 2002
event manager hooks for the Neighborhood
"""

from Plasma import *
from PlasmaTypes import *
import time


sdlHNY = "nb01HappyNewYearVis"
sdlFireworks = ["nb01FireworksOnBalcony","nb01FireworksOnBanner","nb01FireworksOnFountain"]

EventTime = 3600

class Neighborhood(ptResponder):

    def __init__(self):
        ptResponder.__init__(self)
        self.id = 5014
        self.version = 1

    def OnFirstUpdate(self):
        #~ # record our visit in player's chronicle
        #~ kModuleName = "Neighborhood"
        #~ kChronicleVarName = "LinksIntoNeighborhood"
        #~ kChronicleVarType = 0
        #~ vault = ptVault()
        #~ if type(vault) != type(None):
            #~ entry = vault.findChronicleEntry(kChronicleVarName)
            #~ if type(entry) == type(None):
                #~ # not found... add current level chronicle
                #~ vault.addChronicleEntry(kChronicleVarName,kChronicleVarType,"%d" %(1))
                #~ PtDebugPrint("%s:\tentered new chronicle counter %s" % (kModuleName,kChronicleVarName))
            #~ else:
                #~ import string
                #~ count = string.atoi(entry.chronicleGetValue())
                #~ count = count + 1
                #~ entry.chronicleSetValue("%d" % (count))
                #~ entry.save()
                #~ PtDebugPrint("%s:\tyour current count for %s is %s" % (kModuleName,kChronicleVarName,entry.chronicleGetValue()))
        #~ else:
            #~ PtDebugPrint("%s:\tERROR trying to access vault -- can't update %s variable in chronicle." % (kModuleName,kChronicleVarName))
        agevault = ptAgeVault()
        ageinfo = agevault.getAgeInfo()
        guid = ageinfo.getAgeInstanceGuid()
        if guid == "cbf61339-817f-4b97-b642-cb55a46026e3": # Neighborhood-GUID from "Contest Hood"
            PtPageInNode("TOCmod02")
            
    def OnNotify(self,state,id,events):
        pass

    def OnServerInitComplete(self):
        self.HNY_SEE()
        for sdl in sdlFireworks:
            self.SetSDL(sdl, 0, 0)

    def OnTimer(self, TimerID):
        PtDebugPrint('Neighborhood: OnTimer: callback id=%d' % TimerID)
        if (TimerID == 1):
            for sdl in sdlFireworks:
                self.SetSDL(sdl, 0, 1)
            PtDebugPrint('Neighborhood: Fireworks starts')
            PtAtTimeCallback(self.key, 120, 3)
        elif (TimerID == 2):
            self.ISetTimers()
        elif (TimerID == 3):
            for sdl in sdlFireworks:
                self.SetSDL(sdl, 0, 0)
            PtDebugPrint('Neighborhood: Fireworks is - disabled')
            #re-set timers
            self.ISetTimers()

    def SetSDL(self, varname, index, value):
        sdl = PtGetAgeSDL()
        sdl.setFlags(varname, 1, 1)
        sdl.sendToClients(varname)
        sdl.setIndex(varname, index, value)

    def ISetTimers(self):
        dnitime = PtGetDniTime()
        minNum = int(time.strftime('%M', time.gmtime(dnitime)))
        secNum = int(time.strftime('%S', time.gmtime(dnitime)))
        inTime = (secNum + (minNum * 60))
        #if (inTime == 0):
        #    PtAtTimeCallback(self.key, 0, 1)
        #    PtDebugPrint(('Neighborhood: Start Fireworks'))
        #else:
        #    PtDebugPrint('Neighborhood: Fireworks - You missed the event.')
        timeLeft = (EventTime - inTime)
        inmin = (timeLeft / 60)
        #start fireworks in <time to 0 seconds>
        PtAtTimeCallback(self.key, timeLeft, 1)
        PtDebugPrint('Neighborhood: Next Firework Show starts in %d seconds (%d minutes)' % (timeLeft, inmin))

    def HNY_SEE(self):
        dnitime = PtGetDniTime()
        dayNum = int(time.strftime('%d', time.gmtime(dnitime)))
        monthNum = int(time.strftime('%m', time.gmtime(dnitime)))
        sdlName = sdlHNY
        if (monthNum == 12):
            if (dayNum == 31):
                self.ISetTimers()
                self.SetSDL(sdlName, 0, 1)
                PtDebugPrint(('Neighborhood: HNY is - enabled'))
            else:
                self.SetSDL(sdlName, 0, 0)
                PtDebugPrint(('Neighborhood: HNY is - disabled'))
        elif (monthNum == 1):
            if (dayNum == 1):
                self.ISetTimers()
                self.SetSDL(sdlName, 0, 1)
                PtDebugPrint(('Neighborhood: HNY is - enabled'))
            else:
                self.SetSDL(sdlName, 0, 0)
                PtDebugPrint(('Neighborhood: HNY is - disabled'))
        else:
            self.SetSDL(sdlName, 0, 0)
            PtDebugPrint(('Neighborhood: HNY is - disabled'))
