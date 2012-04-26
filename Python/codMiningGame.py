# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *
import random

#Max Wire
dialog = ptAttribGUIDialog(1, "GUI Dialog")
respSND1 = ptAttribResponder(2, "resp: SND 1")
respSND2 = ptAttribResponder(3, "resp: SND 2")
respSND3 = ptAttribResponder(4, "resp: SND 3")
respSND4 = ptAttribResponder(5, "resp: SND 4")
respSND5 = ptAttribResponder(6, "resp: SND 5")
respSND6 = ptAttribResponder(7, "resp: SND 6")

miningPlace1 = ptAttribActivator(8, "Mining Side 1")
miningPlace2 = ptAttribActivator(9, "Mining Side 2")
miningPlace3 = ptAttribActivator(10, "Mining Side 3")
miningPlace4 = ptAttribActivator(11, "Mining Side 4")
miningPlace5 = ptAttribActivator(12, "Mining Side 5")
miningPlace6 = ptAttribActivator(13, "Mining Side 6")

#constants
kButton1 = 101
kButton2 = 102
kButton3 = 103
kButton4 = 104
kButton5 = 105
kButton6 = 106

kTimer = 107
kPoints = 108

kSounds = [respSND1, respSND2, respSND3, respSND4, respSND5, respSND6]

#globals
gMiningSide = 0
gCurrSound = 0
gSounds = []
gNumSounds = 1

gPickedSound = 0
gPoints = 0
gCurrPoints = 0
ChronStr = ""

class codMiningGame(ptModifier):

    def __init__(self):
        ptModifier.__init__(self)
        self.id = 2967431
        self.version = 1
        self.Timer = 0

    def OnServerInitComplete(self):
        PtLoadDialog("MiningGUI")

    def OnNotify(self,state,id,events):
        global gMiningSide
        global gSounds
        global gCurrSound
        global gPickedSound
        global gPoints
        global gCurrPoints
        global gNumSounds
        PtDebugPrint(id)

        if (id == -1):
            if state:
                vault = ptVault()
                entry = vault.findChronicleEntry('MGOre')
                if (type(entry) == type(None)): #does entry exist?
                    vault.addChronicleEntry('MGOre', 0, ChronStr)
                else:
                    entry.chronicleSetValue(ChronStr)
                    entry.save()
                return

        if(state):
            return

        if (PtFindAvatar(events) != PtGetLocalAvatar()):
            return

        gMiningSide = id - 7
        PtDebugPrint("Show MiningGUI")
        PtShowDialog("MiningGUI")

        ptGUIControlButton(dialog.dialog.getControlFromTag(kButton1)).disable()
        ptGUIControlButton(dialog.dialog.getControlFromTag(kButton2)).disable()
        ptGUIControlButton(dialog.dialog.getControlFromTag(kButton3)).disable()
        ptGUIControlButton(dialog.dialog.getControlFromTag(kButton4)).disable()
        ptGUIControlButton(dialog.dialog.getControlFromTag(kButton5)).disable()
        ptGUIControlButton(dialog.dialog.getControlFromTag(kButton6)).disable()
        ptGUIControlTextBox(dialog.dialog.getControlFromTag(kPoints)).setString("0")

        gPickedSound = 0
        gSounds = [0]
        gCurrSound = 0
        gNumSounds = 1
        gPoints = 0
        PtAtTimeCallback(self.key, 0.5, 1)
        #respSND1.run(self.key)

    def OnTimer(self, id):
        global gCurrSound
        global gCurrPoints

        if (id == 1):
            if gCurrSound < len(gSounds):
                kSounds[gSounds[gCurrSound]].run(self.key, netPropagate=0)
            gCurrSound += 1
            if (gCurrSound < len(gSounds)):
                PtAtTimeCallback(self.key, 0.5, 1)
            else:
                ptGUIControlButton(dialog.dialog.getControlFromTag(kButton1)).enable()
                ptGUIControlButton(dialog.dialog.getControlFromTag(kButton2)).enable()
                ptGUIControlButton(dialog.dialog.getControlFromTag(kButton3)).enable()
                ptGUIControlButton(dialog.dialog.getControlFromTag(kButton4)).enable()
                ptGUIControlButton(dialog.dialog.getControlFromTag(kButton5)).enable()
                ptGUIControlButton(dialog.dialog.getControlFromTag(kButton6)).enable()
                self.StartTimer()

        elif (id == 2):
            gCurrPoints += -10
            if gCurrPoints <= 0:
                self.FinishGame()
                self.BreakTimer()
            ptGUIControlTextBox(dialog.dialog.getControlFromTag(kTimer)).setString(str(gCurrPoints))
            if (self.Timer):
                PtAtTimeCallback(self.key, 0.1, 2)

    def OnGUINotify(self,id,control,event):
        global gPickedSound
        global gPickedSound
        global gPoints
        global gCurrSound

        if control:
            tagID = control.getTagID()
            PtDebugPrint("TagID = %i" % tagID)
        else:
            return
        if ((event != kAction) and (event != kValueChanged)):
            return

        if tagID < 100:
            return

        sound = tagID - 101

        kSounds[sound].run(self.key, netPropagate=0)

        if sound == gSounds[gPickedSound]:
            gPickedSound += 1
            if gPickedSound == len(gSounds):
                PtDebugPrint("Finished All Sounds")
                ptGUIControlButton(dialog.dialog.getControlFromTag(kButton1)).disable()
                ptGUIControlButton(dialog.dialog.getControlFromTag(kButton2)).disable()
                ptGUIControlButton(dialog.dialog.getControlFromTag(kButton3)).disable()
                ptGUIControlButton(dialog.dialog.getControlFromTag(kButton4)).disable()
                ptGUIControlButton(dialog.dialog.getControlFromTag(kButton5)).disable()
                ptGUIControlButton(dialog.dialog.getControlFromTag(kButton6)).disable()
                gCurrSound = 0
                gPickedSound = 0
                self.BreakTimer()
                gPoints = gPoints + (gCurrPoints * len(gSounds))
                ptGUIControlTextBox(dialog.dialog.getControlFromTag(kPoints)).setString(str(gPoints))
                self.GenerateSounds()
        else:
            ptGUIControlButton(dialog.dialog.getControlFromTag(kButton1)).disable()
            ptGUIControlButton(dialog.dialog.getControlFromTag(kButton2)).disable()
            ptGUIControlButton(dialog.dialog.getControlFromTag(kButton3)).disable()
            ptGUIControlButton(dialog.dialog.getControlFromTag(kButton4)).disable()
            ptGUIControlButton(dialog.dialog.getControlFromTag(kButton5)).disable()
            ptGUIControlButton(dialog.dialog.getControlFromTag(kButton6)).disable()
            self.BreakTimer()
            self.FinishGame()

    def GenerateSounds(self):
        global gSounds
        global gNumSounds

        i = 0
        gNumSounds += 1
        PtDebugPrint("Generate %i sounds" % gNumSounds)
        gSounds = []
        while i < gNumSounds:
            sound = random.randint(0,5)
            PtDebugPrint("Append sound %i" % i)
            gSounds.append(sound)

            i += 1
        PtDebugPrint("Generating Finished... gSounds = %i" % len(gSounds))
        PtAtTimeCallback(self.key, 1, 1)

    def BreakTimer(self):
        self.Timer = 0

    def StartTimer(self):
        global gCurrPoints

        self.Timer = 1
        gCurrPoints = 1000

        ptGUIControlTextBox(dialog.dialog.getControlFromTag(kTimer)).setString("1000")
        PtAtTimeCallback(self.key, 0.1, 2)

    def FinishGame(self):
        global ChronStr

        prob = [0,0,0,0,0,0,0]  #0-zinc, 1-aluminium, 2-iron, 3-copper, 4-silver, 5-gold, 6-platinum
        PtHideDialog("MiningGUI")
        if gMiningSide == 1:
            prob[0] = 330
            prob[1] = 350
            prob[2] = 220
            prob[3] = 50
            prob[4] = 3

        elif gMiningSide == 2:
            prob[0] = 600
            prob[2] = 210
            prob[3] = 170

        elif gMiningSide == 3:
            prob[0] = 50
            prob[3] = 100
            prob[4] = 200
            prob[5] = 60
            prob[6] = 15

        elif gMiningSide == 4:
            prob[0] = 60
            prob[1] = 200
            prob[2] = 250
            prob[3] = 170
            prob[4] = 50
            prob[5] = 15
            prob[6] = 3

        elif gMiningSide == 5:
            prob[5] = 80
            prob[6] = 50

        elif gMiningSide == 6:
            prob[0] = 700
            prob[1] = 200
            prob[2] = 100

        mult = gPoints/1000
        i = 0
        rand = [0,0,0,0,0,0,0]
        while i < 7:
            prob[i] = int(prob[i]*mult)
            rand[i] = random.randint(0,gPoints)
            i += 1

        met = [0,0,0,0,0,0,0]

        i = 0
        while i < 7:
            if rand[i] <= prob[i]:
                met[i] = rand[i]

            i += 1

        ChronStr = str(gPoints)

        i = 0
        while i < 7:
            ChronStr = ChronStr + "," + str(met[i])

            i += 1

        pounds = (gPoints * 0.454)/1000
        diagP1 = PtGetLocalizedString("CoD.MiningGame.CollectOre1")
        diagP2 = PtGetLocalizedString("CoD.MiningGame.CollectOre2")
        diagStr = diagP1 + ("%.2f" % pounds) + diagP2
        PtYesNoDialog(self.key, diagStr)
