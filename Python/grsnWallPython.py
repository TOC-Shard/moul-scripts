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
from PlasmaKITypes import *
from PlasmaGame import *
from PlasmaGameConstants import *
import time

##############################################################
# define the attributes/parameters that we need from the 3dsMax scene
##############################################################

northPanelClick = ptAttribActivator(1,"North Panel Clickables")
southPanelClick = ptAttribActivator(2,"South Panel Clickables")

northPanel = ptAttribSceneobjectList(3,"North Panel Objects",byObject=1)
southPanel = ptAttribSceneobjectList(4,"South Panel Objects",byObject=1)

# if northWall = 5 and southWall = 6 then your control panel
# controls the wall that YOU climb on (useful for debugging)
# just remember to switch them back before going live...
northWall = ptAttribSceneobjectList(5,"North Wall",byObject=1)
southWall = ptAttribSceneobjectList(6,"South Wall",byObject=1)

northChair = ptAttribActivator(7,"North Chair")
southChair = ptAttribActivator(8,"South Chair")

northLights = ptAttribSceneobjectList(9,"North Panel Lights",byObject=1)
southLights = ptAttribSceneobjectList(10,"South Panel Lights",byObject=1)

northCountLights = ptAttribSceneobjectList(11,"North Count Lights",byObject=1)
southCountLights = ptAttribSceneobjectList(12,"South Count Lights",byObject=1)

upButtonS    = ptAttribActivator(13, "S up count button")
dnButtonS    = ptAttribActivator(14, "S down count button")
readyButtonS = ptAttribActivator(15, "S ready button")

upButtonN    = ptAttribActivator(18, "N up count button")
dnButtonN    = ptAttribActivator(19, "N down count button")
readyButtonN = ptAttribActivator(20, "N ready button")

goButtonN = ptAttribActivator(21,"N Go Button activator")
goButtonS = ptAttribActivator(22,"S Go Button activator")

goBtnNObject = ptAttribSceneobject(23,"N Go Button object")
goBtnSObject = ptAttribSceneobject(24,"S Go Button object")

nChairSit = ptAttribActivator(25,"N sit component")
sChairSit = ptAttribActivator(26,"S sit component")

fiveBtnN = ptAttribActivator(27,"5 btn N")
tenBtnN = ptAttribActivator(28,"10 btn N")
fifteenBtnN = ptAttribActivator(29,"15 btn N")

fiveBtnS = ptAttribActivator(30,"5 btn S")
tenBtnS = ptAttribActivator(31,"10 btn S")
fifteenBtnS = ptAttribActivator(32,"15 btn S")

sTubeOpen = ptAttribNamedResponder(33,"S tube open",netForce=1)
nTubeOpen = ptAttribNamedResponder(34,"N tube open",netForce=1)

sTubeClose = ptAttribNamedResponder(35,"S tube close",netForce=1)
nTubeClose = ptAttribNamedResponder(36,"N tube close",netForce=1)

sTubeEntry = ptAttribNamedActivator(37,"S tube entry trigger")
nTubeEntry = ptAttribNamedActivator(38,"N tube entry trigger")

sTubeMulti = ptAttribBehavior(43,"s tube entry multi",netForce=0)
nTubeMulti = ptAttribBehavior(44,"n tube entry multi",netForce=0)

sTubeExclude = ptAttribExcludeRegion(45,"s tube exclude")
nTubeExclude = ptAttribExcludeRegion(46,"n tube exclude")

sTeamWarpPt = ptAttribSceneobject(47,"s team warp point")
nTeamWarpPt = ptAttribSceneobject(48,"n team warp point")

sTeamWin = ptAttribActivator(49,"s team win")
nTeamWin = ptAttribActivator(50,"n team win")

sTeamQuit = ptAttribActivator(51,"s team quit")
nTeamQuit = ptAttribActivator(52,"n team quit")

sTeamWinTeleport = ptAttribSceneobject(53,"s team win point")
nTeamWinTeleport = ptAttribSceneobject(54,"n team win point")

nQuitBehavior = ptAttribBehavior(55,"s quit behavior")
sQuitBehavior = ptAttribBehavior(56,"n quit behavior")

# sfx responders

nPanelSound = ptAttribResponder(57,"n panel sound",['main','up','down','select','blockerOn','blockerOff','gameStart','denied'],netForce=1)
sPanelSound = ptAttribResponder(58,"s panel sound",['main','up','down','select','blockerOn','blockerOff','gameStart','denied'],netForce=1)

######################

LightP = ptAttribMaterialAnimation(61,"LightP")
LightY = ptAttribMaterialAnimation(62,"LightY")
LightPitY = ptAttribSceneobjectList(63, "LightPitY")
LightPitP = ptAttribSceneobjectList(64, "LightPitP")
LightReadyY = ptAttribSceneobjectList(65, "LightReadyY")
LightReadyP = ptAttribSceneobjectList(66, "LightReadyP")

##############################################################
# grsnWallPython
##############################################################

## globals

## for team light responders
kTeamLightsOn = 0
kTeamLightsOff = 1
kRedFlash = 2
kRedOn = 3
kRedOff = 4

## for go button light states
kDim = 0
kBright = 1
kPulse = 2
##

## game states

kWaiting = 0
kSit = 1 #Sit
kSelect = 2 #Count Blocker
kReady = 3 #Set Blocker
kWaitEntry = 4 #Rdy for Entry
kPlayerEntry = 5 #Player Entry
kGameInProgress = 6
kWin = 7
kQuit = 8

kTeleYWin = 11
kTelePWin = 12
kTeleYQuit = 13
kTelePQuit = 14

PurpleState = kWaiting
YellowState = kWaiting

NorthCount = 0
BlockerCountLimit = 0
SouthCount = 0
NorthWall = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
SouthWall = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
ReceiveInit = false
NorthBlockers = []
SouthBlockers = []


# Event
Wallname = "Wall System:"
Countdown = 101
RunTime = 102
PrintTimer = 103
FinishTime = 104
GameReset = 105
GameResetFinish = 106

WallCheck1 = 111
WallCheck2 = 112
WallCheck3 = 113
WallCheck4 = 114

TOCLOGO = [36,37,46,65, 39,40,48,50,67,69,77,78, 42,43,51,70,80,81, 100,102,117,118,119,126,127, 95,103,104,112,120,121, 105,122,131, 107,124,133]

Countdowntimer = 6
SpeakEnable = 1
GameTimeOld = 0
GameTimeStart = 0

purpleplayer = ""
yellowplayer = ""


class grsnWallPython(ptResponder):
   
    # constants
    
    def __init__(self):
        "construction"
        PtDebugPrint("grsnWallPython::init begin")
        ptResponder.__init__(self)
        self.id = 52392
        self.version = 4
        
        
    def OnServerInitComplete(self):
        global ReceiveInit
        
        PtDebugPrint("grsnWallPython::OnServerInitComplete")        
        solo = true
        ageSDL = PtGetAgeSDL()
        
        if len(PtGetPlayerList()):
            solo = false
            ReceiveInit = true
            
        else:
            print"grsnWallPython: solo in climbing wall"

        ageSDL.setFlags("nChairOccupant",0,1)
        ageSDL.setFlags("sChairOccupant",0,1)
        ageSDL.setFlags("nState",0,1)
        ageSDL.setFlags("sState",0,1)
        ageSDL.setFlags("NumBlockers",0,1)
        ageSDL.setFlags("nBlockerChange",0,1)
        ageSDL.setFlags("sBlockerChange",0,1)
        ageSDL.setFlags("northWall",0,1)
        ageSDL.setFlags("southWall",0,1)

        ageSDL.setNotify(self.key,"nChairOccupant",0.0)
        ageSDL.setNotify(self.key,"sChairOccupant",0.0)
        ageSDL.setNotify(self.key,"nState",0.0)
        ageSDL.setNotify(self.key,"sState",0.0)
        ageSDL.setNotify(self.key,"NumBlockers",0.0)
        ageSDL.setNotify(self.key,"nBlockerChange",0.0)
        ageSDL.setNotify(self.key,"sBlockerChange",0.0)
        
        ageSDL.sendToClients("nChairOccupant")
        ageSDL.sendToClients("sChairOccupant")
        ageSDL.sendToClients("nState")
        ageSDL.sendToClients("sState")
        ageSDL.sendToClients("NumBlockers")
        ageSDL.sendToClients("nBlockerChange")
        ageSDL.sendToClients("sBlockerChange")
        ageSDL.sendToClients("northWall")
        ageSDL.sendToClients("southWall")
        self.LightPanal()
        

        if (solo):
            ageSDL["northWall"] = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
            ageSDL["southWall"] = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
            ageSDL.setIndex("nChairOccupant",0,-1)
            ageSDL.setIndex("sChairOccupant",0,-1)
            ageSDL.setIndex("nWallPlayer",0,-1)
            ageSDL.setIndex("sWallPlayer",0,-1)
            ageSDL.setIndex("nState",0,0)
            ageSDL.setIndex("sState",0,0)
            self.SetPanelMode(kWaiting)
        else:
            print"requesting game state message from SDL"
            self.RequestGameState()
            self.Tubes()
    
    def OnSDLNotify(self,VARname,SDLname,playerID,tag):
        global BlockerCountLimit
        global NorthBlockers
        global SouthBlockers
        global YellowState
        global PurpleState
        
        ageSDL = PtGetAgeSDL()
        value = ageSDL[VARname][0]
        print "grsnWallPython.OnSDLNotify: VARname = ",VARname," SDLname = ",SDLname," playerID = ",playerID," value = ",value
        if (VARname == "nState"):
            YellowState = ageSDL[VARname][0]
            if YellowState == kSelect:
                self.SetPanelMode(kSelect)
            if YellowState == kReady:
                self.SetPanelMode(kReady)
            if YellowState == kWaitEntry:
                self.SetPanelMode(kWaitEntry)
                if (PtGetLocalClientID() == ageSDL["nChairOccupant"][0]):
                    print "grsnWallPython.OnSDLNotify: Yellow Player ready...Tube"
                    self.EnableButtons("yellow","panel","disable")
            if YellowState == kWin:
                PtAtTimeCallback(self.key,0,FinishTime)
                PtAtTimeCallback(self.key,10,GameReset)
                    
        elif (VARname == "sState"):
            PurpleState = ageSDL[VARname][0]
            if PurpleState == kSelect:
                self.SetPanelMode(kSelect)
            if PurpleState == kReady:
                self.SetPanelMode(kReady)
            if PurpleState == kWaitEntry:
                self.SetPanelMode(kWaitEntry)
                if (PtGetLocalClientID() == ageSDL["sChairOccupant"][0]):
                    print "grsnWallPython.OnSDLNotify: Purple Player ready...Tube"
                    self.EnableButtons("purple","panel","disable")
            if PurpleState == kWin:
                PtAtTimeCallback(self.key,0,FinishTime)
                PtAtTimeCallback(self.key,10,GameReset)
                    
        elif (VARname == "NumBlockers"):
            print "grsnWallPython.OnSDLNotify(): Number of Blockers changed"
            BlockerCountLimit = ageSDL[VARname][0]
            if (YellowState == kSelect):
                self.UpdateBlockerCountDisplay("select")
            if (YellowState == kReady):
                self.UpdateBlockerCountDisplay("set")
            
        elif (VARname == "nBlockerChange"):
            index = ageSDL[VARname][0]
            on = ageSDL[VARname][1]
            self.SetWallIndex(index,on,"yellow")
            self.ChangeNorthBlocker(index)
            
        elif (VARname == "sBlockerChange"):
            index = ageSDL[VARname][0]
            on = ageSDL[VARname][1]
            self.SetWallIndex(index,on,"purple")
            self.ChangeSouthBlocker(index)
            
        if (YellowState == kPlayerEntry and PurpleState == kPlayerEntry):
            output = "%s Both players entered - Please wait in front of the ladder. Countdown begins in 20 sec." %Wallname
            PtSendKIMessage(kKILocalChatStatusMsg,output)
                
        self.LightPanal()

        
    def SetPanelMode(self,state):
        global purpleplayer
        global yellowplayer
        
        print "grsnWallPython::SetPanelMode - state change to ", state
        
        if (state == kWaiting):
            self.ResetPanelBlocker()
            self.UpdateBlockerCountDisplay("reset")
            self.EnableButtons("allside","all","disable")
            self.Tubes()
            purpleplayer = ""
            yellowplayer = ""
#            goBtnSObject.value.runAttachedResponder(kDim) #NOT WORK
#            goBtnNObject.value.runAttachedResponder(kDim) #NOT WORK
            
#        elif (state == kSit):
            #set go button to bright
#            goBtnSObject.value.runAttachedResponder(kBright) #NOT WORK
            #set go button to bright
#            goBtnNObject.value.runAttachedResponder(kBright) #NOT WORK
            
        elif (state == kSelect):
            self.ResetPanelBlocker()
            # make all of the counter lights flash 
            self.UpdateBlockerCountDisplay("select")
            #enable up / down buttons
            self.EnableButtons("allside","buttons","enable")
#            goBtnSObject.value.runAttachedResponder(kDim) #NOT WORK
#            goBtnNObject.value.runAttachedResponder(kDim) #NOT WORK
            print"enabled all n switches"
            
        elif (state == kReady):
            # turn unselected count lights solid, and turn off the other lights
            self.UpdateBlockerCountDisplay("set")
            #disable adjustment buttons
            self.EnableButtons("allside","buttons","disable")
            self.EnableButtons("allside","panel","enable")
#            goBtnSObject.value.runAttachedResponder(kRedFlash) #NOT WORK
#            goBtnNObject.value.runAttachedResponder(kRedFlash) #NOT WORK
            
        elif (state == kWaitEntry):
            self.Tubes()
#            goBtnSObject.value.runAttachedResponder(kBright) #NOT WORK
#            goBtnNObject.value.runAttachedResponder(kBright) #NOT WORK

        elif (state == kGameInProgress):
            self.ChangeGameState("allside",kGameInProgress)
#            goBtnSObject.value.runAttachedResponder(kBright) #NOT WORK
#            goBtnNObject.value.runAttachedResponder(kBright) #NOT WORK
                
    def Tubes(self):
        ageSDL = PtGetAgeSDL()
        StateN = ageSDL["nState"][0]
        StateS = ageSDL["sState"][0]
        
        #print "grsnWallPython::Tubes:Tubes state ",State
            
        if (StateN == kWaitEntry) and (StateS == kWaitEntry):
            #run responder to open tube
            sTubeOpen.run(self.key,avatar=PtGetLocalAvatar())
            nTubeOpen.run(self.key,avatar=PtGetLocalAvatar())
            print"grsnWallPython::Tubes: Tubes open"
            
        else:
            sTubeExclude.clear(self.key)
            nTubeExclude.clear(self.key)
            sTubeClose.run(self.key,avatar=PtGetLocalAvatar(),fastforward=1)
            nTubeClose.run(self.key,avatar=PtGetLocalAvatar(),fastforward=1)
    
    def LookupIndex(self,index,north):
        global NorthWall
        global SouthWall
        global BlockerCountLimit
        
        i = 0
        print"looking north ",north
        if (north):
            while (i < BlockerCountLimit):
                if (NorthWall[i] == index):
                    print"index found in north list in slot ",i
                    return true
                print "yellow wall [",i,"] = ",NorthWall[i]
                i = i + 1
        else:
            while (i < BlockerCountLimit):
                if (SouthWall[i] == index):
                    print"index found in south list in slot ",i
                    return true
                print "purple wall [",i,"] = ",SouthWall[i]
                i = i + 1
        
        print"index not found"
        return false

    def SetWallIndex(self,index,value,side):
        global NorthWall
        global SouthWall
        global SouthCount
        global NorthCount
        
        ageSDL = PtGetAgeSDL()
        
        i = 0
        if (value):
            if (side == "yellow"):
                while (NorthWall[i] >= 0):
                    i = i + 1
                    if (i == 20):
                        print"yikes - somehow overran the array!"
                        return
                NorthWall[i] = index
                ageSDL.setIndex("northWall", i, index)
                NorthCount = NorthCount + 1
                print"set side wall index ",index," in slot ",i," to true"
            elif (side == "purple"):
                while (SouthWall[i] >= 0):
                    i = i + 1
                    if (i == 20):
                        print"yikes - somehow overran the array!"
                        return
                SouthWall[i] = index
                ageSDL.setIndex("southWall", i, index)
                SouthCount = SouthCount + 1
                print"set south wall index ",index," in slot ",i," to true"
        else:
            if (side == "yellow"):
                while (NorthWall[i] != index):
                    i = i + 1
                    if (i == 20):
                        print"(grsnWallPython)this should not get hit - looked for non-existent NorthWall entry!"
                        return
                NorthWall[i] = -1
                ageSDL.setIndex("northWall", i, -1)
                NorthCount = NorthCount - 1
                print"removed index ",index," from list slot ",i
            elif (side == "purple"):
                while (SouthWall[i] != index):
                    i = i + 1
                    if (i == 20):
                        print"(grsnWallPython)this should not get hit - looked for non-existent SouthWall entry!"
                        return
                SouthWall[i] = -1
                ageSDL.setIndex("southWall", i, -1)
                SouthCount = SouthCount - 1
                print"removed index ",index," from list slot ",i
            

    def IAmMaster(self):
        return (self.sceneobject.isLocallyOwned())
        
    def ChangeGameState(self,side,newState):
        print "grsnWallPython::ChangeGameState: sending change game state message with state ",newState
        ageSDL = PtGetAgeSDL()
        if (side == "yellow"):
            ageSDL["nState"] = (newState,)
        elif (side == "purple"):
            ageSDL["sState"] = (newState,)
        elif (side == "allside"):
            ageSDL["nState"] = (newState,)
            ageSDL["sState"] = (newState,)
        
    def ChangeBlockerCount(self, newCount):
        global BlockerCountLimit
        print "grsnWallPython::ChangeBlockerCount: sending change blocker count message with new count ",newCount
        
        BlockerCountLimit = newCount
        
        ageSDL = PtGetAgeSDL()
        ageSDL["NumBlockers"] = (newCount,)
        
    def ChangeBlockerState(self, on, index, side):
        print "grsnWallPython::ChangeBlockerState: sending change blocker state message with team ", side, ", index ", index, " and on", on 
        ageSDL = PtGetAgeSDL()
        if (side == "yellow"):
            ageSDL["nBlockerChange"] = (index,on,)
        elif (side == "purple"):
            ageSDL["sBlockerChange"] = (index,on,)

    def RequestGameState(self):
        global YellowState
        global PurpleState
        global BlockerCountLimit
        ageSDL = PtGetAgeSDL()
        
        YellowState = ageSDL["nState"][0]
        PurpleState = ageSDL["sState"][0]
        BlockerCountLimit = ageSDL["NumBlockers"][0]
        for blocker in ageSDL["northWall"]:
            if blocker >= 0:
                self.SetWallIndex(blocker, true, true) # this updates NorthWall and NorthCount for us
                self.ChangeNorthBlocker(blocker)
        for blocker in ageSDL["southWall"]:
            if blocker >= 0:
                self.SetWallIndex(blocker, true, false) # this updates SouthWall and SouthCount for us
                self.ChangeSouthBlocker(blocker)
        ### synchronise client with current game state ###
        if (YellowState != kReady):
            self.SetPanelMode(YellowState)
        
    def UpdateBlockerCountDisplay(self,station):
        global BlockerCountLimit
        
        numSelected = BlockerCountLimit 
        if (station == "select"):
            PtDebugPrint("grsnWallPython::UpdateBlockerCountDisplay - select") 
            i = 0
            while i < numSelected:
                northCountLights.value[i].runAttachedResponder(kTeamLightsOn)
                southCountLights.value[i].runAttachedResponder(kTeamLightsOn)
                i = i + 1
            i = numSelected
            while i < 20:
                northCountLights.value[i].runAttachedResponder(kRedFlash)
                southCountLights.value[i].runAttachedResponder(kRedFlash)
                i = i + 1
            
        elif (station == "set"):
            PtDebugPrint("grsnWallPython::UpdateBlockerCountDisplay - set") 
            i = 0
            while i < numSelected:
                southCountLights.value[i].runAttachedResponder(kTeamLightsOff)
                northCountLights.value[i].runAttachedResponder(kTeamLightsOff)
                i = i + 1
            i = numSelected
            while i < 20:
                southCountLights.value[i].runAttachedResponder(kRedOn)
                northCountLights.value[i].runAttachedResponder(kRedOn)
                i = i + 1
                
        elif (station == "reset"):
            PtDebugPrint("grsnWallPython::UpdateBlockerCountDisplay - reset") 
            i = 0
            while i < 20:
                northCountLights.value[i].runAttachedResponder(kTeamLightsOff)
                southCountLights.value[i].runAttachedResponder(kTeamLightsOff)
                i = i + 1
        
    
    def ChangeSouthBlocker(self,index):
        global BlockerCountLimit
        ageSDL = PtGetAgeSDL()
        # we clicked or un-clicked on a control panel button corresponding to a wall blocker
        print"found South index ",index
        wallPicked = southWall.value[index]
        animPicked = southLights.value[index]
        if (self.LookupIndex(index,false)):
            #turn this guy on
            wallPicked.physics.enable()
            if (PtGetLocalClientID() == ageSDL["sChairOccupant"][0]):
                animPicked.runAttachedResponder(kTeamLightsOn)
                counterPicked = southCountLights.value[SouthCount - 1]
                counterPicked.runAttachedResponder(kTeamLightsOn)
                sPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='blockerOn')
        else:
            wallPicked.physics.disable()
            if (PtGetLocalClientID() == ageSDL["sChairOccupant"][0]):
                animPicked.runAttachedResponder(kTeamLightsOff)
                counterPicked = southCountLights.value[SouthCount]
                counterPicked.runAttachedResponder(kTeamLightsOff)
                sPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='blockerOff')
        return    
   
    def ChangeNorthBlocker(self,index):
        global BlockerCountLimit
        ageSDL = PtGetAgeSDL()
        # we clicked or un-clicked on a control panel button corresponding to a wall blocker
        print"found North index ",index
        wallPicked = northWall.value[index]
        animPicked = northLights.value[index]
        if (self.LookupIndex(index,true)):
            #turn this guy on
            wallPicked.physics.enable()
            if (PtGetLocalClientID() == ageSDL["nChairOccupant"][0]):
                animPicked.runAttachedResponder(kTeamLightsOn)
                counterPicked = northCountLights.value[NorthCount - 1]
                counterPicked.runAttachedResponder(kTeamLightsOn)
                nPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='blockerOn')
        else:
            wallPicked.physics.disable()
            if (PtGetLocalClientID() == ageSDL["nChairOccupant"][0]):
                animPicked.runAttachedResponder(kTeamLightsOff)
                counterPicked = northCountLights.value[NorthCount]
                counterPicked.runAttachedResponder(kTeamLightsOff)
                nPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='blockerOff')
        return
        
    def EnableButtons(self,side,station,set):
        
        if (station == "panel") or (station == "all"):
            i = 0
            while i < 171:
                if (set == "enable"):
                    #PtDebugPrint("grsnWallPython::EnableButtons - Enable Panel Blocker physics") 
                    if (side == "purple" or side == "allside"):
                        southPanel.value[i].physics.enable()
                    if (side == "yellow" or side == "allside"):
                        northPanel.value[i].physics.enable()
                if (set == "disable"):
                    #PtDebugPrint("grsnWallPython::EnableButtons - Disable Panel Blocker physics") 
                    if (side == "purple" or side == "allside"):
                        southPanel.value[i].physics.disable()
                    if (side == "yellow" or side == "allside"):
                        northPanel.value[i].physics.disable()
                i = i + 1
                
        if (station == "buttons" or station == "all"):
            if (set == "enable"):
                print"grsnWallPython::EnableButtons - Enable Count Blocker Buttons"
                # Purple
                upButtonS.enable()
                dnButtonS.enable()
                readyButtonS.enable()
                fiveBtnS.enable()
                tenBtnS.enable()
                fifteenBtnS.enable()
                # Yellow
                upButtonN.enable()
                dnButtonN.enable()
                readyButtonN.enable()
                fiveBtnN.enable()
                tenBtnN.enable()
                fifteenBtnN.enable()
            if (set == "disable"):
                print"grsnWallPython::EnableButtons - Disable Count Blocker Buttons"
                # Purple
                upButtonS.disable()
                dnButtonS.disable()
                readyButtonS.disable()
                fiveBtnS.disable()
                tenBtnS.disable()
                fifteenBtnS.disable()
                # Yellow
                upButtonN.disable()
                dnButtonN.disable()
                readyButtonN.disable()
                fiveBtnN.disable()
                tenBtnN.disable()
                fifteenBtnN.disable()
        
    def ResetPanelBlocker(self):
        global SouthCount
        global NorthCount
        global NorthWall
        global SouthWall
        
        print"grsnWallPython::ResetPanelBlocker - RESETING GAME"
        
        i = 0
        while (i < 171):
            if (i < 20):
                NorthWall[i] = -1
                SouthWall[i] = -1
                
            southLights.value[i].runAttachedResponder(kTeamLightsOff)
            northLights.value[i].runAttachedResponder(kTeamLightsOff)
            
            southWall.value[i].physics.disable()
            northWall.value[i].physics.disable()
            
            i = i + 1
        
        self.ChangeBlockerCount(0)
        NorthCount = 0
        SouthCount = 0
        
        print"grsnWallPython::ResetPanelBlocker - RESETING GAME - FINISHED"
    
        
    def EventBlockerChange(self,param):
        self.ResetPanelBlocker()
        self.ChangeBlockerCount(int(param))
        self.ChangeGameState("allside",kReady)
    
    def WallCheck(self,param):
        i = 0
        while (i < 171):
            if (param == "alloff"):
                if (i < 1):
                    self.UpdateBlockerCountDisplay("reset")
                    self.ResetPanelBlocker()
            elif (param == "allon"):
                if (i < 20):
                    southCountLights.value[i].runAttachedResponder(kTeamLightsOn)
                    northCountLights.value[i].runAttachedResponder(kTeamLightsOn)
                southLights.value[i].runAttachedResponder(kTeamLightsOn)
                northLights.value[i].runAttachedResponder(kTeamLightsOn)
                    
            i = i + 1
            
        if (param == "toc"):
            for index in TOCLOGO:
                southLights.value[index].runAttachedResponder(kTeamLightsOn)
                northLights.value[index].runAttachedResponder(kTeamLightsOn)
    
    
    
    def OnTimer(self,id):
        global YellowState
        global PurpleState
        global GameTimeStart
        global GameTimeOld
        global Countdowntimer
        global purpleplayer
        global yellowplayer
        
        avatar = PtGetLocalAvatar()
        if (id == kTeleYQuit):
            PtFakeLinkAvatarToObject(avatar.getKey(),nTeamWinTeleport.value.getKey())
            PtWearMaintainerSuit(avatar.getKey(),false)
            PtSendKIMessage(kEnableEntireYeeshaBook,0)
            if (YellowState == kGameInProgress):
                self.ChangeGameState("purple",kWin)
                self.ChangeGameState("yellow",kQuit)
        elif (id == kTelePQuit):
            PtFakeLinkAvatarToObject(avatar.getKey(),sTeamWinTeleport.value.getKey())
            PtWearMaintainerSuit(avatar.getKey(),false)
            PtSendKIMessage(kEnableEntireYeeshaBook,0)
            if (PurpleState == kGameInProgress):
                self.ChangeGameState("yellow",kWin)
                self.ChangeGameState("purple",kQuit)
        elif (id == kTeleYWin):
#            PtFakeLinkAvatarToObject(avatar.getKey(),nTeamWinTeleport.value.getKey())
            PtWearMaintainerSuit(avatar.getKey(),false)
            PtSendKIMessage(kEnableEntireYeeshaBook,0)
            if (PurpleState == kGameInProgress):
                self.ChangeGameState("yellow",kWin)
                self.ChangeGameState("purple",kQuit)
#            PtGetLocalAvatar().avatar.exitSubWorld()
        elif (id == kTelePWin):
#            PtFakeLinkAvatarToObject(avatar.getKey(),sTeamWinTeleport.value.getKey())
            PtWearMaintainerSuit(avatar.getKey(),false)
            PtSendKIMessage(kEnableEntireYeeshaBook,0)
            if (YellowState == kGameInProgress):
                self.ChangeGameState("purple",kWin)
                self.ChangeGameState("yellow",kQuit)
#            PtGetLocalAvatar().avatar.exitSubWorld()
            
        elif (id == Countdown):
            if (Countdowntimer == 0):
                output = "%s GO" %Wallname
                PtSendKIMessage(kKILocalChatStatusMsg,output)
                Countdowntimer = 6
                GameTimeStart = PtGetDniTime()
                self.SetPanelMode(kGameInProgress)
                PtAtTimeCallback(self.key,300,RunTime)
            elif (Countdowntimer == 6):
                if ((YellowState == kPlayerEntry) and (PurpleState == kPlayerEntry)):
                    output = "%s Start in" %Wallname
                    PtSendKIMessage(kKILocalChatStatusMsg,output)
                    Countdowntimer -= 1
                    PtAtTimeCallback(self.key,1,Countdown)
                else:
                    output = "%s Players not ready" %Wallname
                    PtSendKIMessage(kKILocalChatStatusMsg,output)
            else:
                output = "%s %s" % (Wallname,Countdowntimer)
                PtSendKIMessage(kKILocalChatStatusMsg,output)
                Countdowntimer -= 1
                PtAtTimeCallback(self.key,1,Countdown)
                
        elif (id == RunTime):
            nexttime = PtGetDniTime() - GameTimeStart
            if ((GameTimeOld == GameTimeStart) and (GameTimeStart != 0)):
                consumedtime = PtGetDniTime() - GameTimeStart
                time = self.TimeConvert(consumedtime)
                output = "%s Elapsed Time: %s" % (Wallname,time)
                PtSendKIMessage(kKILocalChatStatusMsg,output)
                PtAtTimeCallback(self.key,300,RunTime)
            else:
                if (nexttime == 300):
                    GameTimeOld = GameTimeStart
                    PtAtTimeCallback(self.key,0,RunTime)
                    
        elif (id == FinishTime):
            if (GameTimeStart != 0):
                consumedtime = PtGetDniTime() - GameTimeStart
                time = self.TimeConvert(consumedtime)
                
                if (PurpleState == kWin):
                    playerwin = purpleplayer
                    playerlost = yellowplayer
                elif (YellowState == kWin):
                    playerwin = yellowplayer
                    playerlost = purpleplayer
                    
                output = "%s Player %s has WON after %s" % (Wallname,playerwin,time)
                PtSendKIMessage(kKILocalChatStatusMsg,output)
                output2 = "%s Player %s has lost" % (Wallname,playerlost)
                PtSendKIMessage(kKILocalChatStatusMsg,output2)
                
                GameTimeStart = 0
                GameTimeOld = 0
                
        elif (id == GameReset):
            output = "%s Wall will reset in 10 sec" % (Wallname)
            PtSendKIMessage(kKILocalChatStatusMsg,output)
            PtAtTimeCallback(self.key,10,GameResetFinish)
                
        elif (id == GameResetFinish):
            self.SetPanelMode(kWaiting)
            self.ChangeGameState("allside",kWaiting)
            output = "%s Wall has reset" % (Wallname)
            PtSendKIMessage(kKILocalChatStatusMsg,output)
            
        elif (id == WallCheck1):
            self.WallCheck("allon")
            PtAtTimeCallback(self.key,2,WallCheck2)
        elif (id == WallCheck2):
            self.WallCheck("alloff")
            PtAtTimeCallback(self.key,1,WallCheck3)
        elif (id == WallCheck3):
            self.WallCheck("toc")
            
   
    def OnNotify(self,state,id,events):
        global YellowState
        global PurpleState
        global NorthCount
        global SouthCount
        global BlockerCountLimit
        global NorthWall
        global SouthWall
        global nTrigger
        global sTrigger
        global purpleplayer
        global yellowplayer
        
        print "grsnWall - Notify ",state,id,events
        ageSDL = PtGetAgeSDL()
        avatar = PtFindAvatar(events)
        PurpleState = PurpleState
        YellowState = YellowState
        print"PurpleState = ",PurpleState
        print"YellowState = ",YellowState
            
        # responder / behavior notifications
        
        if (id == sQuitBehavior.id):
            for event in events:
                if (event[0] == kMultiStageEvent and event[1] == 0 and event[2] == kEnterStage):
                    print"start touching quit jewel, warp out"
                    if (avatar == PtGetLocalAvatar()):
                        PtAtTimeCallback(self.key ,1 ,kTelePQuit)
                    return
        
        if (id == nQuitBehavior.id):
            for event in events:
                if (event[0] == kMultiStageEvent and event[1] == 0 and event[2] == kEnterStage):
                    print"start touching quit jewel, warp out"
                    if (avatar == PtGetLocalAvatar()):
                        PtAtTimeCallback(self.key ,1 ,kTeleYQuit)
                    return
                    
        if (id == nTubeOpen.id):
            print"tube finished opening"
            nTubeExclude.release(self.key)
        
        if (id == nTubeMulti.id):
            for event in events:
                print "got nTubeMulti.id: event[0] = ", event[0], " event[1] = ", event[1], "event[2] = ", event[2]
                if event[0] == kMultiStageEvent and event[1] == 0 and event[2] == kEnterStage: 
                    print"Smart seek completed. close tube"
                    nTubeClose.run(self.key,avatar=avatar)
                elif event[0] == kMultiStageEvent and event[1] == 0 and event[2] == kAdvanceNextStage:
                    print"multistage complete, warp to wall south room with suit"
                    if (avatar == PtGetLocalAvatar()):
                        PtWearMaintainerSuit(PtGetLocalAvatar().getKey(),true)
                        PtSendKIMessage(kDisableEntireYeeshaBook,0)
                    nTubeExclude.clear(self.key)
                    avatar.physics.warpObj(sTeamWarpPt.value.getKey())
                    self.ChangeGameState("yellow",kPlayerEntry)
                    if (PurpleState == kPlayerEntry):
                        PtAtTimeCallback(self.key,20,Countdown)
                    
                    
        if (id == sTubeOpen.id):
            print"tube finished opening"
            sTubeExclude.release(self.key)
        
        if (id == sTubeMulti.id):
            for event in events:
                print "got sTubeMulti.id: event[0] = ", event[0], " event[1] = ", event[1], "event[2] = ", event[2]
                if event[0] == kMultiStageEvent and event[1] == 0 and event[2] == kEnterStage: 
                    print"Smart seek completed. close tube"
                    sTubeClose.run(self.key,avatar=avatar)
                elif event[0] == kMultiStageEvent and event[1] == 0 and event[2] == kAdvanceNextStage:
                    print"multistage complete, warp to wall north room with suit"
                    if (avatar == PtGetLocalAvatar()):
                        PtWearMaintainerSuit(PtGetLocalAvatar().getKey(),true)
                        PtSendKIMessage(kDisableEntireYeeshaBook,0)
                    sTubeExclude.clear(self.key)
                    avatar.physics.warpObj(nTeamWarpPt.value.getKey())
                    self.ChangeGameState("purple",kPlayerEntry)
                    if (YellowState == kPlayerEntry):
                        PtAtTimeCallback(self.key,20,Countdown)
                    
        
        # activator notifications
        if ((id == sTeamWin.id) and (PtGetLocalAvatar() == PtFindAvatar(events))):
            print"Purple - you win"
            PtFakeLinkAvatarToObject(avatar.getKey(),sTeamWinTeleport.value.getKey())
            #avatar.physics.warpObj(sTeamWinTeleport.value.getKey())
#            self.ChangeGameState("purple",kWin)
#            self.ChangeGameState("yellow",kQuit)
            PtAtTimeCallback(self.key, 1, kTelePWin)
            #ageSDL.setIndex("sChairState",0,kWin)
            #ageSDL.setIndex("nChairState",0,kQuit)
            
        if ((id == nTeamWin.id) and (PtGetLocalAvatar() == PtFindAvatar(events))):
            print"Yellow - you win"
            PtFakeLinkAvatarToObject(avatar.getKey(),nTeamWinTeleport.value.getKey())
            #avatar.physics.warpObj(nTeamWinTeleport.value.getKey())
#            self.ChangeGameState("yellow",kWin)
#            self.ChangeGameState("purple",kQuit)
            PtAtTimeCallback(self.key, 1, kTeleYWin)
            #ageSDL.setIndex("sChairState",0,kQuit)
            #ageSDL.setIndex("nChairState",0,kWin)
            
        if (id == nTeamQuit.id and state):
            if (avatar == PtGetLocalAvatar()):
                avatar.avatar.runBehaviorSetNotify(nQuitBehavior.value,self.key,nQuitBehavior.netForce)
#            self.ChangeGameState("yellow",kQuit)
#            self.ChangeGameState("purple",kWin)
            nTrigger = avatar
            #PtAtTimeCallback(self.key, 1.5, knQuit)
            #ageSDL.setIndex("sChairState",0,kWin)
            #ageSDL.setIndex("nChairState",0,kQuit)
            return
            
        if (id == sTeamQuit.id and state):
            if (avatar == PtGetLocalAvatar()):
                avatar.avatar.runBehaviorSetNotify(sQuitBehavior.value,self.key,sQuitBehavior.netForce)
#            self.ChangeGameState("yellow",kWin)
#            self.ChangeGameState("purple",kQuit)
            sTrigger = avatar
            #PtAtTimeCallback(self.key, 1.5, ksQuit)
            #ageSDL.setIndex("sChairState",0,kQuit)
            #ageSDL.setIndex("nChairState",0,kWin)
            return    
        
        #if (not(state) and (id != nTubeEntry.id)):
        #    return
            
        if (id == southChair.id):
            print"clicked south chair"
            avID = PtGetClientIDFromAvatarKey(avatar.getKey())
            if state:
                occupant = ageSDL["sChairOccupant"][0]
                print"occupant ",occupant
                purpleplayer = PtGetClientName(avatar.getKey())
                if (avID == PtGetClientIDFromAvatarKey(PtGetLocalAvatar().getKey())):
                    print"sitting down in south chair"
                    southChair.disable()
                    ageSDL.setIndex("sChairOccupant",0,avID)
                    if (PurpleState == kWaiting):
                        self.ChangeGameState("purple", kSit)
                    return
        
        if id==sChairSit.id:
            for event in events:
                if event[0]==6 and event[1]==1 and state == 0:
                    print"standing up from south chair"
                    southChair.enable()
                    ageSDL.setIndex("sChairOccupant",0,-1)
                    if (PurpleState == kSit):
                        self.ChangeGameState("purple", kWaiting)
                    return
                            
        if (id == northChair.id):
            print"clicked north chair"
            avID = PtGetClientIDFromAvatarKey(avatar.getKey())
            if state:
                occupant = ageSDL["nChairOccupant"][0]
                print"occupant ",occupant
                yellowplayer = PtGetClientName(avatar.getKey())
                if (avID == PtGetClientIDFromAvatarKey(PtGetLocalAvatar().getKey())):
                    print"sitting down in north chair"
                    northChair.disable()
                    ageSDL.setIndex("nChairOccupant",0,avID)
                    if (YellowState == kWaiting):
                        self.ChangeGameState("yellow", kSit)
                    return
        
        if id==nChairSit.id:
            for event in events:
                if event[0]==6 and event[1]==1 and state == 0:
                    print"standing up from north chair"
                    northChair.enable()
                    ageSDL.setIndex("nChairOccupant",0,-1)
                    if (YellowState == kSit):
                        self.ChangeGameState("yellow", kWaiting)
                    return
                            
        
        elif not state:
            return

        elif id == goButtonS.id:
            print"picked s go button"
            if (PurpleState == kSit and YellowState == kSit):
                print"set index to kSelect"
                self.ChangeGameState("allside", kSelect)
                sPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='main')
            elif(PurpleState == kReady):
                print"check to see if you've used all your wall blockers"          
                numSelected = SouthCount
                maxSelections = BlockerCountLimit
                print"numSelected = ", numSelected, ", maxSelections = ", BlockerCountLimit
                if (numSelected < maxSelections):
                    sPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='denied')
                else:
                    self.ChangeGameState("purple",kWaitEntry)
                    sPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='gameStart')
            return

        elif id == goButtonN.id:
            print"picked n go button"
            if (YellowState == kSit and PurpleState == kSit):
                print"set index to kSelect"
                self.ChangeGameState("allside", kSelect)
                nPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='main')
            elif(YellowState == kReady):
                print"check to see if you've used all your wall blockers"       
                numSelected = NorthCount
                maxSelections = BlockerCountLimit
                print"numSelected = ", numSelected, ", maxSelections = ", BlockerCountLimit
                if (numSelected < maxSelections):
                    nPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='denied')
                else:
                    self.ChangeGameState("yellow",kWaitEntry)
                    nPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='gameStart')
            return

        if (avatar != PtGetLocalAvatar()):
            print"not activated by me"
            return
        
        if (id == nTubeEntry.id):
            nTrigger = PtFindAvatar(events)
            print"entered team purple tube, run behavior"
            ageSDL.setIndex("nWallPlayer",0,PtGetClientIDFromAvatarKey(avatar.getKey()))
            avatar.avatar.runBehaviorSetNotify(nTubeMulti.value,self.key,nTubeMulti.netForce)
            #PtAtTimeCallback(self.key, 0.5, knEnter)
            
        if (id == sTubeEntry.id):
            sTrigger = PtFindAvatar(events)
            print"entered team yellow tube, run behavior"
            ageSDL.setIndex("sWallPlayer",0,PtGetClientIDFromAvatarKey(avatar.getKey()))
            avatar.avatar.runBehaviorSetNotify(sTubeMulti.value,self.key,sTubeMulti.netForce)
            #PtAtTimeCallback(self.key, 0.5, ksEnter)
        
        if id == upButtonS.id:
            print "up button south"
            if (PurpleState == kSelect):
                numSelected = BlockerCountLimit
                print"correct state, blocker count limit ",BlockerCountLimit
                if (numSelected < 20):
                    self.ChangeBlockerCount(numSelected + 1)                    
                    sPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='up')
                elif (numSelected == 20):
                    sPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='denied')
                else:
                    print"somehow think blocker count limit greater than 20?"
            return
            
        elif id == dnButtonS.id:
            print "down button south"
            if (PurpleState == kSelect):
                numSelected = BlockerCountLimit
                if (numSelected > 1):
                    self.ChangeBlockerCount(numSelected - 1)
                    sPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='down')
                elif (numSelected == 1):
                    sPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='denied')
            return
            
        elif id == fiveBtnS.id:
            print"five button south"
            if (PurpleState == kSelect):
                self.ChangeBlockerCount(5)
                sPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='up')
            return
            
        elif id == tenBtnS.id:
            print"ten button south"
            if (PurpleState == kSelect):
                self.ChangeBlockerCount(10)
                sPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='up')
            return
            
        elif id == fifteenBtnS.id:
            print"fifteen button south"
            if (PurpleState == kSelect):
                self.ChangeBlockerCount(15)
                sPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='up')
            return
            
        elif id == readyButtonS.id:
            print "ready button south"
            if (PurpleState == kSelect):
                numSelected = BlockerCountLimit
                if (numSelected > 0):
                    self.ChangeGameState("purple",kReady)
                    sPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='select')
                    if (YellowState == kSelect):
                        self.ChangeGameState("yellow",kReady)
                else:
                    sPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='denied')
            else:
                sPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='denied')
            return
        
        if id == upButtonN.id:
            print "up button north"
            if (YellowState == kSelect):
                numSelected = BlockerCountLimit
                if (numSelected < 20):
                    self.ChangeBlockerCount(numSelected + 1)
                    nPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='up')
                elif (numSelected == 20):
                    nPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='denied')
                else:
                    print"somehow think blocker count limit greater than 20?"
            return
            
        elif id == dnButtonN.id:
            print "down button north"
            if (YellowState == kSelect):
                numSelected = BlockerCountLimit
                if (numSelected > 0):
                    self.ChangeBlockerCount(numSelected - 1)
                    nPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='down')
                elif (BlockerCountLimit == 1):
                    nPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='denied')
            return
            
        elif id == fiveBtnN.id:
            print"five button north"
            if (YellowState == kSelect):
                self.ChangeBlockerCount(5)
                nPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='up')
            return
            
        elif id == tenBtnN.id:
            print"ten button north"
            if (YellowState == kSelect):
                self.ChangeBlockerCount(10)
                nPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='up')
            return
            
        elif id == fifteenBtnN.id:
            print"fifteen button north"
            if (YellowState == kSelect):
                self.ChangeBlockerCount(15)
                nPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='up')
            return
            
        elif id == readyButtonN.id:
            print "ready button north"
            if (YellowState == kSelect):
                numSelected = BlockerCountLimit
                if (numSelected > 0):
                    self.ChangeGameState("yellow",kReady)
                    nPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='select')
                    if (PurpleState == kSelect):
                        self.ChangeGameState("purple",kReady)
                        print"force south chair to keep up"
                else:
                    nPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='denied')
            else:
                nPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='denied')
            return

        for event in events:
            if event[0]==kPickedEvent and event[1] == 1:
                panelPicked = event[3]
                objName = panelPicked.getName()
                print "player picked blocker named ", objName
                north = 0
                if (PtGetLocalClientID() == ageSDL["nChairOccupant"][0]):
                    try:
                        index = northPanel.value.index(panelPicked)
                        north = 1
                    except:
                        print"no wall blocker found"
                        return
                    
                if (PtGetLocalClientID() == ageSDL["sChairOccupant"][0]):
                    try:
                        index = southPanel.value.index(panelPicked)
                    except:
                        print"no wall blocker found"
                        return
                        
                if (north): #you picked something on the north panel
                    if (YellowState != kReady):
                        print"no blocker picking for you!"
                        nPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='denied')
                        return
                    #numSelected = ageSDL["northCount"][0]
                    numSelected = NorthCount
                    #ageSDL.setIndex("lastChangedIndexN",0,index)
                    print"numSelected = ",numSelected
                    #maxSelections = ageSDL["northCountLimit"][0]
                    maxSelections = BlockerCountLimit
                    #if (ageSDL["northWall"][index]==0):
                    if (self.LookupIndex(index,true) == 0):
                        if (numSelected == maxSelections):
                            print"you've picked all you can"
                            nPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='denied')
                            return
                        #numSelected = numSelected + 1
                        #ageSDL.setIndex("northCount",0,numSelected)
                        #NorthCount = numSelected
                        #self.SetWallIndex(index,true,true)
                        self.ChangeBlockerState(true, index, "yellow")
                    else:
                        numSelected = numSelected - 1
                        if (numSelected == -1):
                            print"what?!?"
                            return
                        #ageSDL.setIndex("northCount",0,numSelected)
                        #NorthCount = numSelected
                        #self.SetWallIndex(index,false,true)
                        self.ChangeBlockerState(false,index,"yellow")
                else: #you picked one on the south panel
                    if (PurpleState != kReady):
                        print"no blocker picking for you!"
                        sPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='denied')
                        return
                    #numSelected = ageSDL["southCount"][0]
                    numSelected = SouthCount
                    #ageSDL.setIndex("lastChangedIndexS",0,index)
                    print"numSelected = ",numSelected
                    #maxSelections = ageSDL["southCountLimit"][0]
                    maxSelections = BlockerCountLimit
                    #if (ageSDL["southWall"][index]==0):
                    if (self.LookupIndex(index,false) == 0):
                        if (numSelected == maxSelections):
                            print"you've picked all you can"
                            sPanelSound.run(self.key,avatar=PtGetLocalAvatar(),state='denied')
                            return
                        #numSelected = numSelected + 1
                        #ageSDL.setIndex("southCount",0,numSelected)
                        #SouthCount = numSelected
                        #self.SetWallIndex(index,true,false)
                        self.ChangeBlockerState(true,index,"purple")
                    else:
                        numSelected = numSelected - 1
                        if (numSelected == -1):
                            print"what?!?"
                            return
                        #ageSDL.setIndex("southCount",0,numSelected)
                        #SouthCount = numSelected
                        #self.SetWallIndex(index,false,false)
                        self.ChangeBlockerState(false,index,"purple")

    def LightPanal(self):
        global YellowState
        global PurpleState
        
        ageSDL = PtGetAgeSDL()
        nSit = ageSDL["nChairOccupant"][0]
        sSit = ageSDL["sChairOccupant"][0]
        
        LightP.animation.speed(1)
        LightP.animation.stop()
        LightP.animation.skipToTime(0.16)
        LightY.animation.speed(1)
        LightY.animation.stop()
        LightY.animation.skipToTime(0.16)
        
        if (YellowState == kSelect or PurpleState == kSelect):
            LightP.animation.play()
            LightY.animation.play()
            
        if YellowState == kWin:
            LightY.animation.speed(0.25)
            LightY.animation.play()
            
        if PurpleState == kWin:
            LightP.animation.speed(0.25)
            LightP.animation.play()
            
        i = 0
        while i < 2:
            if (YellowState == kWaiting or PurpleState == kWaiting):
                LightPitY.value[i].draw.disable()
                LightPitP.value[i].draw.disable()
                LightReadyY.value[i].draw.disable()
                LightReadyP.value[i].draw.disable()

            if nSit > -1:
                LightPitY.value[i].draw.enable()
            else:
                LightPitY.value[i].draw.disable()

            if sSit > -1:
                LightPitP.value[i].draw.enable()
            else:
                LightPitP.value[i].draw.disable()

            if (YellowState == kWaitEntry or YellowState == kWin):
                LightReadyY.value[i].draw.enable()
            else:
                LightReadyY.value[i].draw.disable()
            
            if (PurpleState == kWaitEntry or PurpleState == kWin):
                LightReadyP.value[i].draw.enable()
            else:
                LightReadyP.value[i].draw.disable()

            if YellowState == kWin:
                LightReadyP.value[i].draw.disable()
            
            if PurpleState == kWin:
                LightReadyY.value[i].draw.disable()
            
            i = i + 1

            
    def TimeConvert(self, sec):
        t = time.localtime(sec)
        endcalls = time.strftime("%M:%S", t)
        return endcalls
        
        
    def OnBackdoorMsg(self, target, param):
        if target == "event":
            if param == "wallcheck":
                output = "%s Welcome to the TOC Wall Tournament!" % Wallname
                PtSendKIMessage(kKILocalChatStatusMsg,output)
                PtAtTimeCallback(self.key,1,WallCheck1)
            elif param == "countdown":
                PtAtTimeCallback(self.key,1,Countdown)
            elif param == "finish":
                PtAtTimeCallback(self.key,1,FinishTime)
            elif param == "reset":
                PtAtTimeCallback(self.key,0,GameResetFinish)
        elif target == "prep":
            self.EventBlockerChange(param)
        elif target == "lighton":
            southLights.value[int(param)].runAttachedResponder(kTeamLightsOn)
            northLights.value[int(param)].runAttachedResponder(kTeamLightsOn)
        elif target == "lightoff":
            southLights.value[int(param)].runAttachedResponder(kTeamLightsOff)
            northLights.value[int(param)].runAttachedResponder(kTeamLightsOff)
        elif target == "allon":
            self.WallCheck("allon")
        elif target == "alloff":
            self.WallCheck("alloff")
        elif target == "toc":
            self.WallCheck("toc")
                