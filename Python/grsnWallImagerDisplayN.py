#imports
from Plasma import *
from PlasmaTypes import *
from grsnWallConstants import *

#Max Wire
yImager = ptAttribSceneobjectList(1,"Yellow Imager", byObject=1)

class grsnWallImagerDisplayN(ptResponder):
    
    def __init__(self):
        PtDebugPrint("grsnWallImagerDisplayN::init")
        ptResponder.__init__(self)
        self.id = 52398
        self.version = 2
        self.ageSDL = None

    def OnServerInitComplete(self):
        PtDebugPrint("grsnWallImagerDisplayN::OnServerInitComplete")
        self.ageSDL = PtGetAgeSDL()
        
        self.ageSDL.setNotify(self.key, "nState", 0.0)
        
        if(len(PtGetPlayerList()) and self.ageSDL["nState"] >= kWait):
            for blocker in self.ageSDL["northWall"]:
                if(blocker == -1):
                    return
                yImager.value[blocker].runAttachedResponder(kBlockerOn)

    def OnSDLNotify(self,VARname,SDLname,playerID,tag):
        #We only get a notify from nState
        value = self.ageSDL[VARname][0]
        if(value == kWait):
            for blocker in self.ageSDL["northWall"]:
                if(blocker == -1):
                    break
                yImager.value[blocker].runAttachedResponder(kBlockerOn)
        if(value == kSelectCount):
            for i in range(0,171):
                yImager.value[i].runAttachedResponder(kBlockerOff)
