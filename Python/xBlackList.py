# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *
import os
import shutil
import xUserKIConfig

def removeData():
    if xUserKIConfig.IsAdmin(): return
    files = ["libeay32.dll",      #Main
            "ssleay32.dll",
            "AvailableLinks.inf",
            "AvailableTOCLinks.inf",
            "avi/PicardJaradaGreeting.bik", #avi
            "dat/GlobalClothing_District_Armor.prp", #dat,
            "dat/GlobalClothing_District_test.prp",
            "dat/cityofdimensions_District_April.prp",
            "dat/cityofdimensions_District_StoryWall.prp",
            "dat/Ercana_District_ercaImgrFix.prp"]
    folders = ["sfx/streamingCache"]
    for file in files:
        try:
            os.remove(file)
            PtDebugPrint("xBlackList: removed file %s" % file)
        except:
            PtDebugPrint("xBlackList: file %s already removed" % (file),level=kDebugDumpLevel)
    for folder in folders:
        try:
            shutil.rmtree(folder)
            PtDebugPrint("xBlackList: removed folder %s" % file)
        except:
            PtDebugPrint("xBlackList: folder %s already removed" % (file),level=kDebugDumpLevel)
