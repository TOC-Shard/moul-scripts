# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *
from PlasmaKITypes import *
import string
import time
variable = None
AgeStartedIn = None

ImagerName = ptAttribString(1, 'Name of the Imager')
ImagerRegion = ptAttribActivator(2, 'Imager Activator RegionSensor')
HoodInfoImagerScript = ptAttribActivator(3, "Imager script (xSimpleImager)")

delayrunning = 0

class codVisitorImager(ptResponder,):


    def __init__(self):
        ptResponder.__init__(self)
        self.id = 8501004
        version = 1
        self.version = version
        print '__init__codVisitorImager v.',
        print version


    def OnNotify(self, state, id, events):
        global delayrunning
        LocalAvatar = PtFindAvatar(events)
        Avatar = PtGetLocalAvatar()
        if ((id == ImagerRegion.id) and (Avatar == LocalAvatar)):
            if (delayrunning == 0):
                playername = PtGetLocalPlayer().getPlayerName()
                self.IUpdatePlayerList(playername)
                delayrunning = 1
                PtAtTimeCallback(self.key, 300, 6428)


    def RetryRecentVisitors(self):
        PtAtTimeCallback(self.key, 1, 1)


    def OnTimer(self, id):
        global delayrunning
        if (id == 1):
            self.UpdateRecentVisitors()
        if (id == 6428):
            delayrunning = 0


    def IGetDeviceInbox(self):
        deviceNode = None
        deviceInbox = None

        # find the device
        avault = ptAgeVault()
        adevicesfolder = avault.getAgeDevicesFolder()
        adevices = adevicesfolder.getChildNodeRefList()
        for device in adevices:
            device = device.getChild()
            devicetn = device.upcastToTextNoteNode()
            if devicetn and devicetn.getTitle() == ImagerName.value:
                deviceNode = devicetn
                break

        # if we have the device then find the inbox
        if deviceNode:
            inboxes = deviceNode.getChildNodeRefList()
            for inbox in inboxes:
                inbox = inbox.getChild()
                inboxfolder = inbox.upcastToFolderNode()
                if inboxfolder:
                    deviceInbox = inboxfolder
                    break
        return deviceInbox


    def IUpdatePlayerList(self, playername):
        deviceInbox = self.IGetDeviceInbox()
        playerlist = None

        # if we have the inbox then look for the heek score note
        if deviceInbox:
            items = deviceInbox.getChildNodeRefList()
            for item in items:
                item = item.getChild()
                itemtn = item.upcastToTextNoteNode()
                if itemtn:
                    if itemtn.getTitle() == "Visitors, Visiteurs, Besucher":
                        playerlist = itemtn
                        break
                    elif itemtn.getTitle() == "Most Recent Visitors":
                        itemtn.setTitle("Visitors, Visiteurs, Besucher")
                        playerlist = itemtn
                        break

            # if we have the text note then update it, otherwise create it
            if playerlist:
                currenttime = time.gmtime(PtGetDniTime())
                currenttimestr = time.strftime("%m/%d/%Y %I:%M %p", currenttime)
                thetext = playerlist.getText()
                if (thetext.count("\n") + 1) > 15:
                    thetext = thetext[:thetext.rfind("\n")]
                thetext = currenttimestr + (" " * (30 - len(currenttimestr))) + playername + "\n" + thetext
                
                playerlist.setText(thetext)
                playerlist.forceSave()
            else:
                currenttime = time.gmtime(PtGetDniTime())
                currenttimestr = time.strftime("%m/%d/%Y %I:%M %p", currenttime)
                playername = PtGetLocalPlayer().getPlayerName()
                thetext = currenttimestr + (" " * (30 - len(currenttimestr))) + playername
                
                playerlist = ptVaultTextNoteNode(0)
                playerlist.setTitle("Visitors, Visiteurs, Besucher")
                playerlist.setText(thetext)
                deviceInbox.addNode(playerlist)

        if playerlist and playerlist.getID() > 0:
            sname = "Update=%d" % (playerlist.getID())
            self.ISendNotify(HoodInfoImagerScript.value, sname, 1.0)


    def ISendNotify(self, receiver, name, value):
        notify = ptNotify(self.key)
        notify.clearReceivers()
        if type(receiver) == type([]):
            for key in receiver:
                notify.addReceiver(key)
        else:
            notify.addReceiver(receiver)
        notify.netPropagate(1)
        notify.netForce(1)
        notify.setActivate(1.0)
        notify.addVarNumber(name, value)
        notify.send()