# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *

actClick = ptAttribActivator(1, "Activator")
resp1 = ptAttribResponder (2, 'cRespExtendBridge')
resp2 = ptAttribResponder (3, 'cRespStartDayNight2')

class grtpBridgeFix(ptResponder):

    def __init__(self):
        ptResponder.__init__(self)
        self.id = 5323001

        version = 1
        self.version = version
        print "__init__grtpBridgeFix v.", version

    def OnNotify(self,state,id,events):
        if (id == actClick.id):
            resp1.run(self.key)
            resp2.run(self.key)
            print "Trigger on"
