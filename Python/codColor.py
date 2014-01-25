# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *
import time

class codColor(ptResponder):

    def __init__(self):
        ptResponder.__init__(self)
        self.id = 8501010
        self.version = 1

        
    def OnFirstUpdate(self):
        pass
#        self.CheckDate()

        
    def SetFogColor(self, setto1, setto2, setto3):
        PtConsoleNet(('Graphics.Renderer.Fog.SetDefColor %s %s %s' % (setto1, setto2, setto3)), 1)
        PtDebugPrint(('DEBUG: codColor: Color set to %s %s %s' % (setto1, setto2, setto3)))
        
        
    def CheckDate(self):
        dnitime = PtGetDniTime()
        dayNum = int(time.strftime('%d', time.gmtime(dnitime)))
        monthNum = int(time.strftime('%m', time.gmtime(dnitime)))
        
        if (monthNum == 12):
            self.SetFogColor(0.9, 0.9, 0.9)
            PtDebugPrint(('DEBUG: codColor: Current month is %d' % (monthNum)))
        elif (monthNum == 01):
            if (dayNum <= 17):
                self.SetFogColor(0.9, 0.9, 0.9)
                PtDebugPrint(('DEBUG: codColor: Current month is %d' % (monthNum)))
        else:
            self.SetFogColor(0.4, 0.3, 0.1)
            PtDebugPrint(('DEBUG: codColor: Current month is %d' % (monthNum)))
            