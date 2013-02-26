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
# Include Plasma code
from Plasma import *
from PlasmaTypes import *

# for save/load
import cPickle

## COMMENTED OUT by Jeff due to the re-write in the garrison wall

##############################################################
# define the attributes/parameters that we need from the 3dsMax scene
##############################################################
northWall = ptAttribSceneobjectList(1,"North Wall",byObject=1)
##############################################################
# grsnWallImagerDisplayN
##############################################################
ReceiveInit = false

## for team light responders
kTeamLightsOn = 0
kTeamLightsOff = 1

## game states

kWaiting    = 0
kNorthSit   = 1
kSouthSit   = 2
kNorthSelect = 3
kSouthSelect = 4
kNorthReady = 5
kSouthReady = 6
kNorthPlayerEntry = 7
kSouthPlayerEntry = 8
kGameInProgress = 9
kNorthWin = 10
kSouthWin = 11
kSouthQuit = 12
kNorthQuit = 13


class grsnWallImagerDisplayN(ptResponder):
   
    # constants
    
    def __init__(self):
        "construction"
        PtDebugPrint("grsnWallImagerDisplayN::init begin")
        ptResponder.__init__(self)
        self.id = 52398
        self.version = 1
        PtDebugPrint("grsnWallImagerDisplayN::init end")        

    def RequestGameState(self):
        ageSDL = PtGetAgeSDL()
        
        for blocker in ageSDL["northWall"]:
            if blocker >= 0:
                northWall.value[blocker].runAttachedResponder(kTeamLightsOn)
        
    def OnServerInitComplete(self):
        global ReceiveInit
        
        ageSDL = PtGetAgeSDL()
        PtDebugPrint("grsnWallPython::OnServerInitComplete")        
        solo = true
        if len(PtGetPlayerList()):
            solo = false
            ReceiveInit = true
            self.RequestGameState()
            return
        else:
            print"solo in climbing wall"
            
        #ageSDL.setFlags("nState",0,1)
        #ageSDL.setFlags("sState",0,1)
        #ageSDL.setFlags("NumBlockers",0,1)
        #ageSDL.setFlags("nBlockerChange",0,1)
        #ageSDL.setFlags("sBlockerChange",0,1)
        
        ageSDL.setNotify(self.key,"nState",0.0)
        ageSDL.setNotify(self.key,"sState",0.0)
        ageSDL.setNotify(self.key,"NumBlockers",0.0)
        ageSDL.setNotify(self.key,"nBlockerChange",0.0)
        ageSDL.setNotify(self.key,"sBlockerChange",0.0)
        
        #ageSDL.sendToClients("nState")
        #ageSDL.sendToClients("sState")
        #ageSDL.sendToClients("NumBlockers")
        #ageSDL.sendToClients("nBlockerChange")
        #ageSDL.sendToClients("sBlockerChange")
            
    def OnSDLNotify(self,VARname,SDLname,playerID,tag):
        
        ageSDL = PtGetAgeSDL()
        value = ageSDL[VARname][0]
        state = value
        print "grsnWallImagerDisplayN.OnSDLNotify: VARname = ",VARname," SDLname = ",SDLname," playerID = ",playerID," value = ",value
        
        if ((VARname == "nState") or (VARname == "sState")):
            if ((value == kSouthSit) or (value == kNorthSit)):
                i = 0
                while (i < 171):
                    #clear wall settings
                    northWall.value[i].runAttachedResponder(kTeamLightsOff)
                    i = i + 1                
        elif (VARname == "nBlockerChange"):
            index = value
            on = ageSDL[VARname][1]
            if (on):
                northWall.value[state].runAttachedResponder(kTeamLightsOn)
                print"Imager display N drawing n wall index",state               
            else:
                northWall.value[state].runAttachedResponder(kTeamLightsOff)
                print"Imager display N clearing n wall index",state
