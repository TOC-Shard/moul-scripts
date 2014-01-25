# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *
from codColor import *
import string


##############################################################
# define the attributes/parameters that we need from the 3dsMax scene
##############################################################

LakeAni = ptAttribMaterialAnimation(1,"Lake Animation")
LakeScoreAni = ptAttribMaterialAnimation(2,"Lake Score Animation")

##############################################################
# codLakeScore
##############################################################

## globals

LakeFullTime = 3.33
LakeFull = 4000000
LakeTimeLeft = 3600

FullR = 0.4
FullG = 0.3
FullB = 0.1

codColor = codColor()

kGlobalScore = "LakeScore"
kAlgaeScore = "AlgaeScore"

class codLakeScore(ptMultiModifier):

    def __init__(self):
        ptMultiModifier.__init__(self)
        self.id = 8501012
        self.version = 1
        
        self._lakePoints = 0
        self._AlgaePoints = 0
        

    def OnFirstUpdate(self):
        pass
    
        
    def OnServerInitComplete(self):
        ptGameScore.findGlobalScores(kAlgaeScore, self.key)
        ptGameScore.findGlobalScores(kGlobalScore, self.key)
        self.ISetTimers()
        

    def OnTimer(self,id):
        if id == 1:
            ptGameScore.findGlobalScores(kAlgaeScore, self.key)
            ptGameScore.findGlobalScores(kGlobalScore, self.key)
        elif id == 2:
            self.ISetTimers()
            
        
    def OnGameScoreMsg(self, msg):
        if isinstance(msg, ptGameScoreListMsg):
            try:
                l = msg.getScores()
                score = l[0]
                if score.getName() == kGlobalScore:
                    self._lakePoints = score.getPoints()
                elif score.getName() == kAlgaeScore:
                    self._AlgaePoints = score.getPoints()
                self.ScoreMeter()
            except:
                # The score doesn't exist, so let's create it...
                if msg.getName() == kAlgaeScore:
                    type = PtGameScoreTypes.kAccumAllowNegative
                    points = 0
                    ptGameScore.createScore(msg.getOwnerID(), msg.getName(), type, points, self.key)
                    PtDebugPrint("codLakeScore.OnGameScoreMsg():\tkAlgaeScore not Found - Creating")
                elif score.getName() == kGlobalScore:
                    PtDebugPrint("codLakeScore.OnGameScoreMsg():\tkGlobalScore not Found")
        else:
            PtDebugPrint("codLakeScore.OnGameScoreMsg():\telse")
        
        
    def ScoreMeter(self):
        AlgaePoints = self._AlgaePoints
    
        PtDebugPrint(('DEBUG: codLakeScore.ScoreMeter: Algae Score is %s' % AlgaePoints))
        
        self.AnimPos(self.Calculate("Scale", AlgaePoints))
        self.FogColor(self.Calculate("Color", AlgaePoints))
        
        
    def AnimPos(self, Lakestate):
        LakeTime = Lakestate * LakeFullTime
    
        LakeAni.animation.stop()
        LakeScoreAni.animation.stop()
        
        LakeAni.animation.skipToTime(LakeTime)
        LakeScoreAni.animation.skipToTime(LakeTime)
        
        PtDebugPrint(('DEBUG: codLakeScore.AnimPos:  Lake is %s' % Lakestate))
    
    
    def FogColor(self, setfog):
        FogIS1 = FullR * setfog
        FogIS2 = FullG * setfog
        FogIS3 = FullB * setfog
        
        PtDebugPrint(('DEBUG: codLakeScore.FogColor: Set FogColor to %s %s %s' % (FogIS1, FogIS2, FogIS3)))
        PtDebugPrint('DEBUG: codLakeScore.FogColor: Percentage = %f' % setfog)
        
        codColor.SetFogColor(FogIS1, FogIS2, FogIS3)
    
    
    def Calculate(self, what, AlgaePoints):
        a = 1240000000. / 15129.
        b = 5000000. / 123.
        c = 248. / 123.
        x = float(AlgaePoints)

        if (what == "Scale"):
            param = (a / (-x - b) + c) / 2
            if (param > 1):
                param = 1
        elif (what == "Color"):
            param = a / (-x - b) + c
        
        return param
        
    
    def ISetTimers(self):
        DayTime = PtGetAgeTimeOfDayPercent()
        modifier = (86400 / LakeTimeLeft)
        temp1 = (modifier * DayTime)
        temp2 = int(temp1)
        EventPercent = (temp1 - temp2)
        
        if (EventPercent == 0):
            EventPercent = 1
        
        ServerTime = (PtGetServerTime() + 60)
        LastEvent = (ServerTime - int((EventPercent * LakeTimeLeft)))
        timeEventStarts = (LastEvent + LakeTimeLeft)
        
        if (timeEventStarts > ServerTime):
            timeTillEvent = (timeEventStarts - ServerTime)
            PtAtTimeCallback(self.key, timeTillEvent, 1)
        else:
            PtDebugPrint('DEBUG: codLakeScore.ISetTimers: Missing Lake check')
            
        timeLeft = (LakeTimeLeft - int((EventPercent * LakeTimeLeft)))
        timeLeft += 1
        PtAtTimeCallback(self.key, timeLeft, 2)
        PtDebugPrint('DEBUG: codLakeScore.ISetTimers: Next Lake check in %d seconds' % timeLeft)
    
    
    def OnBackdoorMsg(self, target, param):
        if target == "lake":
            self.AnimPos(self.Calculate("Scale", param))
            self.FogColor(self.Calculate("Color", param))
        elif target == "algscore":
            print self._AlgaePoints
        elif target == "lakescore":
            print self._lakePoints

