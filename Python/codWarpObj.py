# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *
from PlasmaKITypes import *
from PlasmaVaultConstants import *
from PlasmaNetConstants import *
from xPsnlVaultSDL import *
ObjClick = ptAttribActivator(1, 'Clickable Object')
Target = ptAttribSceneobject(2, 'Target Warp Dummy')

class codWarpObj(ptModifier,):
    __module__ = __name__

    def __init__(self):
        ptModifier.__init__(self)
        self.id = 8501001
        self.version = 1
        print '__init__codWarpObj v.',
        print self.version


    def OnFirstUpdate(self):
        pass


    def OnServerInitComplete(self):
        pass


    def OnNotify(self, state, id, events):
        print 'OnNotify id =',
        print id
        if (id == ObjClick.id):
            avatar = PtFindAvatar(events)
            avpos = avatar.position()
            targetpos = Target.sceneobject.position()
            x = targetpos.getX()
            y = targetpos.getY()
            z = targetpos.getZ()
            matrix = avatar.getLocalToWorld()
            matrix.translate(ptVector3((x - avpos.getX()), (y - avpos.getY()), (z - avpos.getZ())))
            avatar.netForce(1)
            avatar.physics.warp(matrix)


    def OnSDLNotify(self, VARname, SDLname, playerID, tag):
        pass
