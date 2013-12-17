# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *

actSendUp = ptAttribActivator(30, 'Actvtr: Elev Up Btn')
actSendDn = ptAttribActivator(31, 'Actvtr: Elev Down Btn')

actCall1 = ptAttribActivator(32, 'Actvtr: Call Btn #1')
actCall2 = ptAttribActivator(33, 'Actvtr: Call Btn #2')
actCall3 = ptAttribActivator(34, 'Actvtr: Call Btn #3')

respStrain = ptAttribResponder(35, 'Rspndr: Elev Locked Sound')

resp1to2 = ptAttribResponder(36, 'Rspndr: 1 to 2')
resp1to3 = ptAttribResponder(37, 'Rspndr: 1 to 3')
resp2to3 = ptAttribResponder(38, 'Rspndr: 2 to 3')
resp3to1 = ptAttribResponder(39, 'Rspndr: 3 to 1')
resp3to2 = ptAttribResponder(40, 'Rspndr: 3 to 2')
resp2to1 = ptAttribResponder(41, 'Rspndr: 2 to 1')

respDoor1Open = ptAttribResponder(42, 'Rspndr: Door #1 Open')
respDoor1Closed = ptAttribResponder(43, 'Rspndr: Door #1 Closed')

respDoor2Open = ptAttribResponder(44, 'Rspndr: Door #2 Open')
respDoor2Closed = ptAttribResponder(45, 'Rspndr: Door #2 Closed')

respDoor3Open = ptAttribResponder(46, 'Rspndr: Door #3 Open')
respDoor3Closed = ptAttribResponder(47, 'Rspndr: Door #3 Closed')

respOnboardDoorAOpen = ptAttribResponder(48, 'Rspndr: OnboardDoor #1 Open')
respOnboardDoorAClosed = ptAttribResponder(49, 'Rspndr: OnboardDoor #1 Closed')

respOnboardDoorBOpen = ptAttribResponder(50, 'Rspndr: OnboardDoor #2 Open')
respOnboardDoorBClosed = ptAttribResponder(51, 'Rspndr: OnboardDoor #2 Closed')

xrgnDoor1 = ptAttribExcludeRegion(53,"xRgn: Door #1")
xrgnDoor2 = ptAttribExcludeRegion(54,"xRgn: Door #2")
xrgnDoor3 = ptAttribExcludeRegion(55,"xRgn: Door #3")
xrgnOnboardDoorA = ptAttribExcludeRegion(56,"xRgn: OnboardDoor #1")


# global varariables
elevCurrFloor = 1
elevIdle = 1

kStringAgeSDLElvCurrFloor = 'Event11'
kStringAgeSDLElvIdle = 'Event01'
AgeStartedIn = None

class codAufzug01(ptResponder):


    def __init__(self):
        ptResponder.__init__(self)
        self.id = 8501002
        version = 1
        self.version = version


    def OnFirstUpdate(self):
        global AgeStartedIn
        AgeStartedIn = PtGetAgeName()


    def OnServerInitComplete(self):
        global AgeStartedIn
        global elevCurrFloor
        global elevIdle
        
        if (AgeStartedIn == PtGetAgeName()):
            ageSDL = PtGetAgeSDL()
        else:
            PtDebugPrint('codAufzug01.OnServerInitComplete():\tERROR -- not in the age we started in?')
            return
            
        ageSDL.setFlags(kStringAgeSDLElvIdle, 1, 1)
        ageSDL.sendToClients(kStringAgeSDLElvIdle)
        ageSDL.setNotify(self.key, kStringAgeSDLElvCurrFloor, 0.0)
        ageSDL.setNotify(self.key, kStringAgeSDLElvIdle, 0.0)
        
        try:
            elevCurrFloor = ageSDL[kStringAgeSDLElvCurrFloor][0]
            elevIdle = ageSDL[kStringAgeSDLElvIdle][0]
        except:
            elevCurrFloor = 1
            elevIdle = 1
            PtDebugPrint('codAufzug01.OnServerInitComplete():\tERROR: age sdl read failed, defaulting:')
        PtDebugPrint(('codAufzug01.OnServerInitComplete():\t%s=%d, %s=%d' % (kStringAgeSDLElvCurrFloor, elevCurrFloor, kStringAgeSDLElvIdle, elevIdle)))
        
        if (len(PtGetPlayerList()) == 0):
            PtDebugPrint('codAufzug01.OnServerInitComplete():\tsolo player... initializing elevator state')
            if (not (elevIdle)):
                PtDebugPrint('\tmaking elevator idle')
                ageSDL[kStringAgeSDLElvIdle] = (1,)
                elevIdle = 1
            PtDebugPrint(('\tplacing elevator at floor %s' % elevCurrFloor))
            if (elevCurrFloor == 1):
                resp2to1.run(self.key, fastforward=true)
            elif (elevCurrFloor == 2):
                resp1to2.run(self.key, fastforward=true)
            else:
                resp2to3.run(self.key, fastforward=true)
                
        respDoor1Closed.run(self.key, fastforward=true)
        respDoor2Closed.run(self.key, fastforward=true)
        respDoor3Closed.run(self.key, fastforward=true)
        
        # init elevator 'doors'
        xrgnDoor1.clearNow(self.key)
        xrgnDoor2.clearNow(self.key)
        xrgnDoor3.clearNow(self.key)
        if elevIdle:
            if (elevCurrFloor == 1):
                respOnboardDoorAOpen.run(self.key)
                respDoor1Open.run(self.key, fastforward=true)
                xrgnDoor1.releaseNow(self.key)
            elif (elevCurrFloor == 2):
                respOnboardDoorAOpen.run(self.key)
                respDoor2Open.run(self.key, fastforward=true)
                xrgnDoor2.releaseNow(self.key)
            elif (elevCurrFloor == 3):
                respOnboardDoorAOpen.run(self.key)
                respDoor3Open.run(self.key, fastforward=true)
                xrgnDoor3.releaseNow(self.key)
        else:
            respOnboardDoorAClosed.run(self.key)
            xrgnOnboardDoorA.clearNow(self.key)


    def OnSDLNotify(self, VARname, SDLname, playerID, tag):
        global AgeStartedIn
        global elevIdle
        global elevCurrFloor
        
        if (AgeStartedIn == PtGetAgeName()):
            ageSDL = PtGetAgeSDL()
        else:
            PtDebugPrint('codAufzug01.OnSDLNotify():\tERROR -- not in the age we started in?')
            return
            
        PtDebugPrint(('codAufzug01.OnSDLNotify():\t VARname:%s, SDLname:%s, tag:%s, value:%d, playerID:%d' % (VARname, SDLname, tag, ageSDL[VARname][0], playerID)))
        
        if (VARname == kStringAgeSDLElvIdle):
            elevIdle = ageSDL[kStringAgeSDLElvIdle][0]
            if (not (elevIdle)):
                xrgnDoor1.clearNow(self.key)
                xrgnDoor2.clearNow(self.key)
                xrgnDoor3.clearNow(self.key)
                xrgnOnboardDoorA.clearNow(self.key)
                respOnboardDoorAClosed.run(self.key)
                self.Buttons(false)
            else:
                if elevCurrFloor == 1:
                    xrgnOnboardDoorA.releaseNow(self.key)
                    xrgnDoor1.releaseNow(self.key)
                    respOnboardDoorAOpen.run(self.key)
                    respDoor1Open.run(self.key)
                elif elevCurrFloor == 2:
                    xrgnOnboardDoorA.releaseNow(self.key)
                    xrgnDoor2.releaseNow(self.key)
                    respOnboardDoorAOpen.run(self.key)
                    respDoor2Open.run(self.key)
                elif elevCurrFloor == 3:
                    xrgnOnboardDoorA.releaseNow(self.key)
                    xrgnDoor3.releaseNow(self.key)
                    respOnboardDoorAOpen.run(self.key)
                    respDoor3Open.run(self.key)
                self.Buttons(true)
            return
            
        if (VARname == kStringAgeSDLElvCurrFloor): # set by anim event detectors on elevator (elev overrides high sdl)
            elevCurrFloor = ageSDL[kStringAgeSDLElvCurrFloor][0]
            ageSDL[kStringAgeSDLElvIdle] = (1,)
            return


    def OnNotify(self, state, id, events):
        global elevIdle
        global AgeStartedIn
        global elevCurrFloor
        
        ageSDL = PtGetAgeSDL()
        
        if (id == resp2to1.id) or (id == resp3to1.id):
            ageSDL[kStringAgeSDLElvCurrFloor] = (1,)
        if (id == resp1to2.id) or (id == resp3to2.id):
            ageSDL[kStringAgeSDLElvCurrFloor] = (2,)
        if (id == resp1to3.id) or (id == resp2to3.id):
            ageSDL[kStringAgeSDLElvCurrFloor] = (3,)
        
        if (not (state)):
            return
            
        if (AgeStartedIn == PtGetAgeName()):
            ageSDL = PtGetAgeSDL()
        else:
            PtDebugPrint('codAufzug01.OnNotify():\tERROR -- not in the age we started in?')
            return
            
        ##################
        # elevator call/send buttons #
        ##################
        
        if (not (((id == actCall1.id) or ((id == actCall2.id) or ((id == actCall3.id) or ((id == actSendUp.id) or (id == actSendDn.id))))))):
            return
            
        if (not (elevIdle)):
            return
            
        if ((id == actCall1.id) and (elevCurrFloor != 1)):
            ageSDL[kStringAgeSDLElvIdle] = (0,)
            if (elevCurrFloor == 2):
                resp2to1.run(self.key)
                respDoor2Closed.run(self.key)
            else:
                resp3to1.run(self.key)
                respDoor3Closed.run(self.key)
            return
            
        if ((id == actCall2.id) and (elevCurrFloor != 2)):
            ageSDL[kStringAgeSDLElvIdle] = (0,)
            if (elevCurrFloor == 1):
                resp1to2.run(self.key)
                respDoor1Closed.run(self.key)
            else:
                resp3to2.run(self.key)
                respDoor3Closed.run(self.key)
            return
            
        if ((id == actCall3.id) and (elevCurrFloor != 3)):
            ageSDL[kStringAgeSDLElvIdle] = (0,)
            if (elevCurrFloor == 1):
                resp1to3.run(self.key)
                respDoor1Closed.run(self.key)
            else:
                resp2to3.run(self.key)
                respDoor2Closed.run(self.key)
            return
            
        if ((id == actSendUp.id) and (elevCurrFloor != 3)):
            ageSDL[kStringAgeSDLElvIdle] = (0,)
            if (elevCurrFloor == 1):
                resp1to2.run(self.key)
                respDoor1Closed.run(self.key)
            else:
                resp2to3.run(self.key)
                respDoor2Closed.run(self.key)
            return
            
        if ((id == actSendDn.id) and (elevCurrFloor != 1)):
            ageSDL[kStringAgeSDLElvIdle] = (0,)
            if (elevCurrFloor == 2):
                resp2to1.run(self.key)
                respDoor2Closed.run(self.key)
            else:
                resp3to2.run(self.key)
                respDoor3Closed.run(self.key)
            return

    def Buttons(self,enable):
        if enable:
            PtAtTimeCallback(self.key, 5, 1)
        else:
            actSendUp.disable()
            actSendDn.disable()
            actCall1.disable()
            actCall2.disable()
            actCall3.disable()
            
    def OnTimer(self,id):
        if (id == 1):
            actSendUp.enable()
            actSendDn.enable()
            actCall1.enable()
            actCall2.enable()
            actCall3.enable()
            
            