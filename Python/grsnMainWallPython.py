#imports
from Plasma import *
from PlasmaTypes import *
from grsnWallConstants import *

#Max wire
yWall = ptAttribSceneobjectList(1, "Yellow Wall Decals", byObject=1)
pWall = ptAttribSceneobjectList(2, "Purple Wall Decals", byObject=1)
yBlockers = ptAttribSceneobjectList(3, "Yellow Blocker objects", byObject=1)
pBlockers = ptAttribSceneobjectList(4, "Purple Blocker objects", byObject=1)

class grsnMainWallPython(ptResponder):
    
    def __init__(self):
        PtDebugPrint("grsnMainWallPython::init")
        ptResponder.__init__(self)
        self.id = 52394
        self.version = 2
        self.ageSDL = None

    def OnServerInitComplete(self):
        PtDebugPrint("grsnMainWallPython::OnServerInitComplete")
        self.ageSDL = PtGetAgeSDL()
        
        self.ageSDL.setNotify(self.key, "nState", 0.0)
        self.ageSDL.setNotify(self.key, "sState", 0.0)

    def OnClimbingBlockerEvent(self,blocker):
        if(self.ageSDL['nState'][0] == kEnd):
            return

        for i in range(0,171):
            if(yBlockers.value[i] == blocker):
                yWall.value[i].runAttachedResponder(kBlockerBlink)
                if(eventHandler):
                    eventHandler.HandleBlocker()
                break
            elif(pBlockers.value[i] == blocker):
                pWall.value[i].runAttachedResponder(kBlockerBlink)
                if(eventHandler):
                    eventHandler.HandleBlocker()
                break

    def OnSDLNotify(self,VARname,SDLname,playerID,tag):
        #We only set the states for a Notify
        yState = self.ageSDL["nState"][0]
        pState = self.ageSDL["sState"][0]
        if(yState == pState == kEnd):
            for blocker in self.ageSDL["northWall"]:
                if(blocker == -1):
                    break
                yWall.value[blocker].runAttachedResponder(kBlockerOn)
            for blocker in self.ageSDL["southWall"]:
                if(blocker == -1):
                    break
                pWall.value[blocker].runAttachedResponder(kBlockerOn)
        elif(yState == pState == kSelectCount):
            for i in range(0,171):
                yWall.value[i].runAttachedResponder(kBlockerOff)
                pWall.value[i].runAttachedResponder(kBlockerOff)
