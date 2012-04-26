# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *
import time

class codColor(ptResponder):

    def __init__(self):
        ptResponder.__init__(self)
        self.id = 8501010
        self.version = 1

    def OnServerInitComplete(self):
        self.FogColor()

    def FogColor(self):
        dnitime = PtGetDniTime()
        dayNum = int(time.strftime('%d', time.gmtime(dnitime)))
        monthNum = int(time.strftime('%m', time.gmtime(dnitime)))
        if (monthNum == 12):
            PtConsoleNet(('Graphics.Renderer.Fog.SetDefColor 0.9 0.9 0.9'), 1)
            PtDebugPrint(('codColor: Current month is %d, Color set to 0.9 0.9 0.9' % (monthNum)))
        elif (monthNum == 01):
            if (dayNum <= 17):
                PtConsoleNet(('Graphics.Renderer.Fog.SetDefColor 0.9 0.9 0.9'), 1)
                PtDebugPrint(('codColor: Current month is %d, Color set to 0.9 0.9 0.9' % (monthNum)))
        else:
            PtConsoleNet(('Graphics.Renderer.Fog.SetDefColor 0.4 0.3 0.1'), 1)
            PtDebugPrint(('codColor: Current month is %d, Color set to 0.4 0.3 0.1' % (monthNum)))
