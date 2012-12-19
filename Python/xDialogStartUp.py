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

from Plasma import *
from PlasmaTypes import *
from PlasmaKITypes import *
from PlasmaConstants import *
from PlasmaNetConstants import *

import PlasmaControlKeys
import re
import string

#MaxWire
##Dialogs
GUIDiag4b   = ptAttribGUIDialog(1, "GUI Dialog 4b")
GUIDiag4c   = ptAttribGUIDialog(2, "GUI Dialog 4c")
GUIDiag4d   = ptAttribGUIDialog(3, "GUI Dialog 4d")
GUIDiag6    = ptAttribGUIDialog(4, "GUI Dialog 6")

##Responders for player highlite
respP1      = ptAttribResponder(5, "resp: 4B Player01", ["in", "out"])
respP2      = ptAttribResponder(6, "resp: 4B Player02", ["in", "out"])
respP3      = ptAttribResponder(7, "resp: 4B Player03", ["in", "out"])
respP4      = ptAttribResponder(8, "resp: 4B Player04", ["in", "out"])
respP5      = ptAttribResponder(9, "resp: 4B Player05", ["in", "out"])

##Animation for avatar selection
selectAnim  = ptAttribAnimation(15, "Selection Animation")

##Sounds
respSFXSwitch = ptAttribResponder(11, "Switch Sound Resp")
respSFXLink   = ptAttribResponder(12, "Link Sound Resp")

#Constants
##Explorer Dialog
k4bExploreID        = 200
k4bQuitID           = 201
k4bCreateID         = 202
k4bDeleteID         = 203
k4bPlayer01         = 204
k4bPlayerTxt01      = 214
k4bPlayer02         = 205
k4bPlayerTxt02      = 215
k4bPlayer03         = 206
k4bPlayerTxt03      = 216
k4bPlayer04         = 207
k4bPlayerTxt04      = 217
k4bPlayer05         = 208
k4bPlayerTxt05      = 218

##Delete Dialog
k4cYesID            = 300
k4cNoID             = 301
k4cStaticID         = 302
k4cEditID           = 303

##Error Dialog
k4dYesID            = 400
k4dTextID           = 401

##Create Dialog
k6BackID            = 600
k6PlayID            = 601
k6NameID            = 602
k6MaleID            = 603
k6FemaleID          = 604

##Timer
kAnimTimer = 1
kMovementTimer = 2
kInitTimer = 3

##Other
kMinusExplorer      = 204
kExp_Buttons        = [k4bPlayer01,k4bPlayer02,k4bPlayer03,k4bPlayer04,k4bPlayer05]
kExp_TxtBox         = [k4bPlayerTxt01,k4bPlayerTxt02,k4bPlayerTxt03,k4bPlayerTxt04,k4bPlayerTxt05]
kExp_Resp           = [respP1,respP2,respP3,respP4,respP5]

#Globals
gPlayerList         = None
gSelectedSlot       = 0
gExplorerScreen     = True

#=================================================================================================

class xDialogStartUp(ptResponder):

    def __init__(self):
        ptResponder.__init__(self)
        self.id = 5340
        self.version = 5
        self.ageLink = None
        print "xDialogStartUp: init  version = %d" % self.version

    ###############################
    def OnServerInitComplete(self):
        global gSelectedSlot
        
        gSelectedSlot = k4bPlayer01
        self.InitPlayerList()
        PtGetControlEvents(True,self.key)
        PtSendKIMessage(kDisableKIandBB,0)
        PtAtTimeCallback(self.key,0.5,kInitTimer)

    #################################
    def BeginAgeUnload(self, avatar):
        if GUIDiag4b.dialog.isEnabled():
            PtHideDialog("GUIDialog04b")
        if GUIDiag4c.dialog.isEnabled():
            PtHideDialog("GUIDialog04c")
        if GUIDiag4d.dialog.isEnabled():
            PtHideDialog("GUIDialog04d")
        if GUIDiag6.dialog.isEnabled():
            PtHideDialog("GUIDialog06")

    ###################################
    def OnNotify(self,state,id,events):
        if id==(-1): ##Callback from Quit
            if state:
                PtConsole("App.Quit")

    #######################################
    def OnGUINotify(self,id,control,event):
        if control:
            tagID = control.getTagID()

        ##################
        ##  Explorer    ##
        ##################

        if (id == GUIDiag4b.id):
            if (event == kAction or event == kValueChanged):
                if (tagID == k4bExploreID): #Explore
                    if gSelectedSlot:
                        PtDebugPrint("Player selected.")
                        #Setting active Player
                        playerID = gPlayerList[gSelectedSlot-kMinusExplorer][1]
                        print "Setting active player."
                        respSFXLink.run(self.key)
                        PtSetActivePlayer(playerID)

                elif (tagID == k4bQuitID): #Quit
                    PtYesNoDialog(self.key,"Are you sure you want to quit?")

                elif (tagID == k4bDeleteID): #Delete
                    if gSelectedSlot:
                        playerName = gPlayerList[gSelectedSlot-kMinusExplorer][0]
                        deleteString = U"If you want to DELETE this explorer enter \"" + unicode(playerName) + U"\" in the box below.\nThis action cannot be reversed!"
                        ptGUIControlTextBox(GUIDiag4c.dialog.getControlFromTag(k4cStaticID)).setStringW(deleteString)
                        self.ActivatePlayerButtons(0)
                        PtShowDialog("GUIDialog04c")

                elif (tagID == k4bCreateID): #Create
                    self.ActivatePlayerButtons(0)
                    PtShowDialog("GUIDialog06")

                elif  (tagID == k4bPlayer01 or tagID == k4bPlayer02 or tagID == k4bPlayer03 or tagID == k4bPlayer04 or tagID == k4bPlayer05) and not (tagID == gSelectedSlot):
                    self.SelectSlot(tagID)

        ######################
        ##  Delete Player   ##
        ######################

        elif (id == GUIDiag4c.id):
            if (event == kAction or event == kValueChanged):
                if (tagID == k4cYesID): #Confirm
                    playerID = 0
                    playerName = gPlayerList[gSelectedSlot-kMinusExplorer][0]
                    playerID = gPlayerList[gSelectedSlot-kMinusExplorer][1]
                    playerNameEnter = ptGUIControlEditBox(GUIDiag4c.dialog.getControlFromTag(k4cEditID)).getString()
                    if (playerName == playerNameEnter):
                        PtDeletePlayer(playerID)
                    else:
                        errorString = "The entered name did not match."
                        ptGUIControlTextBox(GUIDiag4d.dialog.getControlFromTag(k4dTextID)).setString(errorString)
                        PtShowDialog("GUIDialog04d")

                    ptGUIControlEditBox(GUIDiag4c.dialog.getControlFromTag(k4cEditID)).setString("")

                elif (tagID == k4cNoID): #Cancel
                    PtHideDialog("GUIDialog04c")
                    self.ActivatePlayerButtons(1)

        ######################
        ##  Error Screen    ##
        ######################

        elif (id == GUIDiag4d.id):
            if (event == kAction or event == kValueChanged):
                if (tagID == k4dYesID): #Continue
                    self.ActivatePlayerButtons(1)
                    PtHideDialog("GUIDialog04d")

        ######################
        ##  Create Dialog   ##
        ######################

        elif (id == GUIDiag6.id):
            if (event == kAction or event == kValueChanged):
                if (tagID == k6BackID): #Back to Playerselect
                    PtHideDialog("GUIDialog06")
                    self.ActivatePlayerButtons(1)

                elif (tagID == k6PlayID): #Create the Avatar
                    playerName = ptGUIControlEditBox(GUIDiag6.dialog.getControlFromTag(k6NameID)).getString()
                    playerNameW = ptGUIControlEditBox(GUIDiag6.dialog.getControlFromTag(k6NameID)).getStringW()

                    try:
                        playerName == playerNameW
                    except:
                        errorString = "Error, invalid name. Please enter another."
                        ptGUIControlTextBox(GUIDiag4d.dialog.getControlFromTag(k4dTextID)).setString(errorString)
                        PtShowDialog("GUIDialog04d")

                    playerGender = ""
                    if ptGUIControlCheckBox(GUIDiag6.dialog.getControlFromTag(k6MaleID)).isChecked():
                        playerGender = "male"
                    if ptGUIControlCheckBox(GUIDiag6.dialog.getControlFromTag(k6FemaleID)).isChecked():
                        playerGender = "female"

                    if playerName == U"" or playerName == "":
                        errorString = "Error, you must enter a name."
                        ptGUIControlTextBox(GUIDiag4d.dialog.getControlFromTag(k4dTextID)).setString(errorString)
                        PtShowDialog("GUIDialog04d")

                    elif playerGender == "":
                        errorString = "Error, you must select a gender."
                        ptGUIControlTextBox(GUIDiag4d.dialog.getControlFromTag(k4dTextID)).setString(errorString)
                        PtShowDialog("GUIDialog04d")

                    else:
                        fixedPlayerName = playerName.strip()
                        (fixedPlayerName, whitespacefixedcount) = re.subn("\s{2,}|[\t\n\r\f\v]", " ", fixedPlayerName)

                        (fixedPlayerName, RogueCount,) = re.subn('[\x00-\x1f]', '', fixedPlayerName)
                        if RogueCount > 0 or whitespacefixedcount > 0:
                            if RogueCount > 0:
                                errorString = "Warning, you entered invalid characters in your player name.  The invalid characters have been removed, please make sure your player name is still what you want."
                            else:
                                errorString = "Warning, your player name has some incorrect formatting.  The formatting has been corrected, please make sure your player name is still what you want."
                            ptGUIControlTextBox(GUIDiag4d.dialog.getControlFromTag(k4dTextID)).setString(errorString)
                            PtShowDialog("GUIDialog04d")

                            ptGUIControlEditBox(GUIDiag6.dialog.getControlFromTag(k6NameID)).setString(fixedPlayerName)
                        else:
                            PtDebugPrint("Creating Player")
                            ptGUIControlButton(GUIDiag6.dialog.getControlFromTag(k6PlayID)).disable()
                            PtCreatePlayer(fixedPlayerName, playerGender, "")

                elif  tagID == k6MaleID: #Male
                    if ptGUIControlCheckBox(GUIDiag6.dialog.getControlFromTag(k6FemaleID)).isChecked():
                        ptGUIControlCheckBox(GUIDiag6.dialog.getControlFromTag(k6FemaleID)).setChecked(0)

                elif  tagID == k6FemaleID: #Female
                    if ptGUIControlCheckBox(GUIDiag6.dialog.getControlFromTag(k6MaleID)).isChecked():
                        ptGUIControlCheckBox(GUIDiag6.dialog.getControlFromTag(k6MaleID)).setChecked(0)

    ##################################################
    def OnControlKeyEvent(self,controlKey,activeFlag):
        if not activeFlag:
            return

        if (controlKey == PlasmaControlKeys.kKeyExitMode):
            PtYesNoDialog(self.key,"Are you sure you want to quit?")

        if not gExplorerScreen:
            return

        elif (controlKey == PlasmaControlKeys.kKeyJump):
            if gSelectedSlot:
                print "Player selected."

                #Start setting active player (we'll link out when this operation completes)
                playerID = gPlayerList[gSelectedSlot-kMinusExplorer][1]
                print "Setting active player."
                respSFXLink.run(self.key)
                PtSetActivePlayer(playerID)

        elif ((controlKey == PlasmaControlKeys.kKeyMoveForward) and (gSelectedSlot > k4bPlayer01)):
            self.SelectSlot(gSelectedSlot - 1)
            PtGetControlEvents(False,self.key)
            PtAtTimeCallback(self.key, 0.5, kAnimTimer)

        elif ((controlKey == PlasmaControlKeys.kKeyMoveBackward) and (gSelectedSlot < k4bPlayer01+len(gPlayerList)-1)):
            self.SelectSlot(gSelectedSlot + 1)
            PtGetControlEvents(False,self.key)
            PtAtTimeCallback(self.key, 0.5, kAnimTimer)

    ######################
    def OnTimer(self, id):
        if (id == kAnimTimer):
            PtGetControlEvents(True,self.key)

        elif (id == kMovementTimer):
            PtDisableMovementKeys()

        elif (id == kInitTimer):
            PtGetLocalAvatar().avatar.loadClothingFromFile(str(gPlayerList[0][1]) + ".clo")
            PtAtTimeCallback(self.key, 0.1, kMovementTimer) #Disable movement keys after possible avatar change

    #####################################################
    def OnAccountUpdate(self, opType, result, playerInt):
        if (result != 0):
            PtDebugPrint("OnAccountUpdate type %u failed: %u" % (opType, result))

            if (result == 12):
                errorString = "Error, this player name already exists."
                ptGUIControlTextBox(GUIDiag4d.dialog.getControlFromTag(k4dTextID)).setString(errorString)
                PtShowDialog("GUIDialog04d")
                ptGUIControlButton(GUIDiag6.dialog.getControlFromTag(k6PlayID)).enable()
            elif (result == 19):
                errorString = "You reached the maximum number of explorers. If you want to create a new explorer you have to delete another one."
                ptGUIControlTextBox(GUIDiag4d.dialog.getControlFromTag(k4dTextID)).setString(errorString)
                PtShowDialog("GUIDialog04d")
                ptGUIControlButton(GUIDiag6.dialog.getControlFromTag(k6PlayID)).enable()
            elif (result == 28):
                errorString = "Invalid name. The name chosen is either reserved, illegal, or shorter than three characters."
                ptGUIControlTextBox(GUIDiag4d.dialog.getControlFromTag(k4dTextID)).setString(errorString)
                PtShowDialog("GUIDialog04d")
                ptGUIControlButton(GUIDiag6.dialog.getControlFromTag(k6PlayID)).enable()
            else:
                errorString = "There has been a Network error. Please try again. If problem persists, please contact support."
                ptGUIControlTextBox(GUIDiag4d.dialog.getControlFromTag(k4dTextID)).setString(errorString)
                PtShowDialog("GUIDialog04d")
            return

        if (playerInt == 0):
            return

        if (opType == PtAccountUpdateType.kActivePlayer):
            print "Active player set."

            #Activate Optionsdialog
            pythonBox = PtFindSceneobject("OptionsDialog", "GUI")
            pmlist = pythonBox.getPythonMods()
            for pm in pmlist:
                notify = ptNotify(self.key)
                notify.clearReceivers()
                notify.addReceiver(pm)
                notify.setActivate(1.0)
                notify.send()

            #Setup the link to the next age
            self.ageLink = ptAgeLinkStruct()
            ageInfo = ptAgeInfoStruct()

            vault = ptVault()
            entry = vault.findChronicleEntry("InitialAvCustomizationsDone")
            if type(entry) != type(None):
                ageInfo.setAgeFilename("Personal")
            else:
                ageInfo.setAgeFilename("AvatarCustomization")
            self.ageLink.setAgeInfo(ageInfo)
            self.ageLink.setLinkingRules(PtLinkingRules.kOwnedBook)

            print "Linking to %s" % (self.ageLink.getAgeInfo().getAgeFilename())
            ptNetLinkingMgr().linkToAge(self.ageLink)
            self.ageLink = None

        elif (opType == PtAccountUpdateType.kCreatePlayer):
            print "Player created."

            #Start setting active player (we'll link out once this operation completes)
            print "Setting active player."
            respSFXLink.run(self.key)
            PtSetActivePlayer(playerInt)

        elif (opType == PtAccountUpdateType.kDeletePlayer):
            self.SelectSlot(k4bPlayer01)
            self.InitPlayerList()

            PtHideDialog("GUIDialog04c")

    #########################
    def InitPlayerList(self):
        global gPlayerList

        #Setup GUI
        gPlayerList = PtGetAccountPlayerList()
        gPlayerList = gPlayerList[1:] #Remove the visitor from the list
        PtDebugPrint("xDialogStartUp.InitPlayerList Enter: gPlayerList = %s" % (str(gPlayerList)))

        #Hide unneeded players
        tagID = k4bPlayer01 + len(gPlayerList)
        while (tagID <= k4bPlayer05):
            ptGUIControlTextBox(GUIDiag4b.dialog.getControlFromTag(tagID)).hide() #Button
            ptGUIControlTextBox(GUIDiag4b.dialog.getControlFromTag(tagID+10)).hide() #Text
            tagID+=1

        for respToRun in kExp_Resp:
            respToRun.run(self.key,state="out")

        kExp_Resp[0].run(self.key,state="in")

        self.ActivatePlayerButtons(1)

        #Setup Player Slots
        for idx in range(0, len(gPlayerList)):
            player = gPlayerList[idx]
            ptGUIControlTextBox(GUIDiag4b.dialog.getControlFromTag(kExp_TxtBox[idx])).setStringW(unicode(player[0]))

        try:
            gPlayerList[0]
        except IndexError:
            self.SelectSlot(0)
        else:
            self.SelectSlot(kExp_Buttons[0])

    ########################################
    def ActivatePlayerButtons(self, toggle):
        gExplorerScreen = toggle

        for tagID in kExp_Buttons:
            PtDebugPrint("xDialogStartUp.PlayerListNotify: setting tagID (%d) to Interesting = %d" % (tagID, toggle))
            if toggle:
                ptGUIControlButton(GUIDiag4b.dialog.getControlFromTag(tagID)).enable()
            else:
                ptGUIControlButton(GUIDiag4b.dialog.getControlFromTag(tagID)).disable()

        if toggle:
            ptGUIControlButton(GUIDiag4b.dialog.getControlFromTag(k4bExploreID)).enable()
            ptGUIControlButton(GUIDiag4b.dialog.getControlFromTag(k4bCreateID)).enable()
            ptGUIControlButton(GUIDiag4b.dialog.getControlFromTag(k4bDeleteID)).enable()
        else:
            ptGUIControlButton(GUIDiag4b.dialog.getControlFromTag(k4bExploreID)).disable()
            ptGUIControlButton(GUIDiag4b.dialog.getControlFromTag(k4bCreateID)).disable()
            ptGUIControlButton(GUIDiag4b.dialog.getControlFromTag(k4bDeleteID)).disable()

    ############################
    def SelectSlot(self, tagID):
        global gSelectedSlot

        if (tagID != gSelectedSlot):
            respSFXSwitch.run(self.key)
            PtDebugPrint("xDialogStartUp.SelectSlot: tagID = %d   gSelectedSlot = %d" % (tagID, gSelectedSlot))
            self.ToggleSelect(gSelectedSlot, False)

            numFrames = 40.0
            frameRate = 30.0
            timeToScroll = 0.5

            currentFrame = (gSelectedSlot - kMinusExplorer) * 10
            nextFrame = (tagID - kMinusExplorer) * 10

            framesToPlay = nextFrame - currentFrame
            if (framesToPlay < 0):
                framesToPlay *= -1

            speedMult = (framesToPlay/frameRate)/timeToScroll
            selectAnim.animation.speed(speedMult)

            animStart = (numFrames/frameRate)*(currentFrame/numFrames)
            animEnd = (numFrames/frameRate)*(nextFrame/numFrames)
            selectAnim.animation.playRange(animStart, animEnd)

            gSelectedSlot = tagID
            self.ToggleSelect(tagID, True)
            id = gPlayerList[gSelectedSlot-kMinusExplorer][1]
            PtGetLocalAvatar().avatar.loadClothingFromFile(str(id) + ".clo")
            PtAtTimeCallback(self.key, 0.1, kMovementTimer) #Disable movement keys after possible avatar change

    ##################################
    def ToggleSelect(self, tagID, on):
        if (tagID == 0):
            return

        idx = kExp_Buttons.index(tagID)
        respToRun = kExp_Resp[idx]

        if on:
            respToRun.run(self.key,state="in")
        else:
            respToRun.run(self.key,state="out")
