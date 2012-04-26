# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *
from PlasmaKITypes import *
from PlasmaVaultConstants import *
import string

#=============================================================
# define the attributes that will be entered in max
#=============================================================
ImagerName = ptAttribString(1,"Name of the Imager")
FontColor = ptAttribString(2,"Color: Red,Green,Blue,Alpha")
FontSize = ptAttribInt(3,"Font Size")
FontFace = ptAttribString(4,"Font Face")
TextXOffset = ptAttribInt(7,"Text X Offset", 0, (-10000,1000000))
TextYOffset = ptAttribInt(8,"Text Y Offset", 0, (-10000,1000000))
UpdateTime = ptAttribFloat(9,"Update Interval", 0, (0,100))
IncAmount = ptAttribInt(10,"Increment px amount per update.")
ImagerMap1 = ptAttribDynamicMap(11, "The Dynamic Texture Map1")
ImagerMap2 = ptAttribDynamicMap(12, "The Dynamic Texture Map2")
ImagerMap3 = ptAttribDynamicMap(13, "The Dynamic Texture Map3")
ImagerMap4 = ptAttribDynamicMap(14, "The Dynamic Texture Map4")
#----------
# globals
#----------
kFontColor = []
kTextFontSize = 0
kTextFontFace = ""
kTextXStart = 0
kTextYStart = 0
kUpdateTime = 0
kMessage = ""
kTextXPos = []
kIncAmount = 0
kCursorStart = [0,0,0,0]
kCursorEnd = [0,0,0,0]
CurrentMessage = ["","","",""]
kNextChar = [0,0,0,0]
kFirstChar = [0,0,0,0]
kTextWidth = [0,0,0,0]
kLastUpdate = 0
kNewChar = 0


#====================================

class TOCNewsTicker(ptModifier):

    def __init__(self):
        global Instance
        ptModifier.__init__(self)
        Instance = self
        self.id = 8501999
        self.version = 1
        print "TOCNewsTicker: init  version=%d.%d"%(self.version,3)
    ############################
    def OnServerInitComplete(self):

        global kTextFontSize
        global kFontColor
        global kTextFontFace
        global kTextXStart
        global kTextYStart
        global kUpdateTime
        global kCharWidth
        global kMessage
        global kTextXPos
        global kIncAmount
        global kCursorStart
        global kCursorEnd
        global CurrentMessage
        global kLastUpdate


        kTextFontSize = FontSize.value
        kTextFontFace = FontFace.value
        kTextXStart = 0
        kTextYStart = 0
        kTextXPos = [kTextXStart,kTextXStart,kTextXStart,kTextXStart]
        kIncAmount = IncAmount.value

        kFontColor = FontColor.value.split(",")
        kFontColor = ptColor(red=float(kFontColor[0]),green=float(kFontColor[1]),blue=float(kFontColor[2]),alpha=float(kFontColor[3]))
        self.UpdateMarqueeMessage()
    ############################
    def UpdateMarqueeMessage(self):
        global kMessage
        global kLastUpdate

        inbox = ptVault().getGlobalInbox()
        inboxChildList = inbox.getChildNodeRefList()

        for child in inboxChildList:
            PtDebugPrint("TOCNewsTicker: looking at node " + str(child),level=kDebugDumpLevel)
            node = child.getChild()
            folderNode = node.upcastToFolderNode()
            if type(folderNode) != type(None):
                PtDebugPrint("TOCNewsTicker: node is named %s" % (folderNode.getFolderName()),level=kDebugDumpLevel)
                if folderNode.getFolderName() == ImagerName.value:
                    folderNodeChildList = folderNode.getChildNodeRefList()
                    for folderChild in folderNodeChildList:
                        PtDebugPrint("TOCNewsTicker: looking at child node " + str(folderChild),level=kDebugDumpLevel)
                        childNode = folderChild.getChild()
                        textNode = childNode.upcastToTextNoteNode()
                        if type(textNode) != type(None):
                            PtDebugPrint("TOCNewsTicker: child node is named %s" % (textNode.getTitle()),level=kDebugDumpLevel)
                            if textNode.getTitle() == ImagerName.value:
                                if textNode.getText() == "":
                                    if kMessage == "":
                                        self.setTimerCallback(30)
                                    #print "TOCNewsTicker: No message was found."

                                elif kMessage != textNode.getText():
                                    oldmessage = kMessage
                                    kMessage = textNode.getText()
                                    self.setMarquee(ImagerMap1,0)
#                                    self.setMarquee(ImagerMap2,1)
#                                    self.setMarquee(ImagerMap3,2)
#                                    self.setMarquee(ImagerMap4,3)
#                                    self.getMaxChars()
                                    if oldmessage == "":
                                        kLastUpdate = PtGetDniTime()
                                        self.setTimerCallback(kUpdateTime)
                                PtDebugPrint("TOCNewsTicker: Marquee contents are '%s'" % (kMessage),level=kDebugDumpLevel)
                                return
        self.setTimerCallback(30)

    ############################

    def setMarquee(self, ImagerMap, x):

        ImagerMap.textmap.clearToColor(ptColor(0,0,0,0))
        ImagerMap.textmap.setTextColor(kFontColor, true)
        ImagerMap.textmap.setFont(kTextFontFace,kTextFontSize)
        ImagerMap.textmap.setWrapping(512, 512)
        ImagerMap.textmap.drawText(kTextXPos[x],kTextYStart,kMessage)
    ############################

    def setTimerCallback(self, timerlength):
        PtClearTimerCallbacks(self.key)
        PtAtTimeCallback(self.key,timerlength,1)
