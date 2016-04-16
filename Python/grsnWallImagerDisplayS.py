#imports
from Plasma import *
from PlasmaTypes import *
from grsnWallConstants import *

#Max Wire
pImager = ptAttribSceneobjectList(2,"Purple Imager", byObject=1)

class grsnWallImagerDisplayS(ptResponder):
    
    def __init__(self):
        PtDebugPrint("grsnWallImagerDisplayS::init")
        ptResponder.__init__(self)
        self.id = 52397
        self.version = 2
        self.ageSDL = None

    def OnServerInitComplete(self):
        PtDebugPrint("grsnWallImagerDisplayS::OnServerInitComplete")
        self.ageSDL = PtGetAgeSDL()
        
        self.ageSDL.setNotify(self.key, "sState", 0.0)
        
        if(len(PtGetPlayerList()) and self.ageSDL["sState"] >= kWait):
            for blocker in self.ageSDL["southWall"]:
                if(blocker == -1):
                    return
                pImager.value[blocker].runAttachedResponder(kBlockerOn)

    def OnSDLNotify(self,VARname,SDLname,playerID,tag):
        #We only get a notify from nState
        value = self.ageSDL[VARname][0]
        if(value == kWait):
            for blocker in self.ageSDL["southWall"]:
                if(blocker == -1):
                    break
                pImager.value[blocker].runAttachedResponder(kBlockerOn)
        if(value == kSelectCount):
            for i in range(0,171):
                pImager.value[i].runAttachedResponder(kBlockerOff)
