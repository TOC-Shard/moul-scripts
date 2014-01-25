# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *
import string
stringVarName1 = ptAttribString(1, 'Age SDL Var Name 1')
stringShowStates1 = ptAttribString(2, 'States in which shown 1')
stringVarName2 = ptAttribString(3, 'Age SDL Var Name 2')
stringShowStates2 = ptAttribString(4, 'States in which shown 2')
stringVarName3 = ptAttribString(5, 'Age SDL Var Name 3')
stringShowStates3 = ptAttribString(6, 'States in which shown 3')
stringVarName4 = ptAttribString(7, 'Age SDL Var Name 4')
stringShowStates4 = ptAttribString(8, 'States in which shown 4')
stringVarName5 = ptAttribString(9, 'Age SDL Var Name 5')
stringShowStates5 = ptAttribString(10, 'States in which shown 5')
AgeStartedIn = None

VARList = [stringVarName1, stringVarName2, stringVarName3, stringVarName4, stringVarName5]
VARListShow = [stringShowStates1, stringShowStates2, stringShowStates3, stringShowStates4, stringShowStates5]
VARListADD = ["self.enabledStateList1", "self.enabledStateList2", "self.enabledStateList3", "self.enabledStateList4", "self.enabledStateList5"]

class TOCxAgeSDLIntShowHideMore(ptMultiModifier):


    def __init__(self):
        ptMultiModifier.__init__(self)
        self.id = 8501011
        self.version = 1
        self.enabledStateList1 = []
        self.enabledStateList2 = []
        self.enabledStateList3 = []
        self.enabledStateList4 = []
        self.enabledStateList5 = []
        self.SDLList = 0
        self.Active = True


    def OnFirstUpdate(self):
        global AgeStartedIn
        AgeStartedIn = PtGetAgeName()

        for j in VARList:
            if (j.value != ''):
                self.SDLList += 1
        PtDebugPrint('TOCxAgeSDLIntShowHideMore.OnFirstUpdate():\tSDLList: %s' % self.SDLList)

        k = 0
        while k < self.SDLList:
            if ((type(VARList[k].value) == type('')) and (VARList[k].value != '')):
                try:
                    VARListADD[k] = VARListShow[k].value.split(',')
                    for i in range(len(VARListADD[k])):
                        VARListADD[k][i] = int(VARListADD[k][i].strip())
                except:
                    PtDebugPrint('ERROR: TOCxAgeSDLIntShowHideMore.OnFirstUpdate():\tERROR: couldn\'t process start state list')
            else:
                PtDebugPrint('ERROR: TOCxAgeSDLIntShowHideMore.OnFirstUpdate():\tERROR: missing SDL var name')
            k += 1


    def OnServerInitComplete(self):
        self.SDLInvolved()


    def OnSDLNotify(self, VARname, SDLname, playerID, tag):
        if (VARname in VARList.value):
            self.SDLInvolved()


    def EnableObject(self):
        PtDebugPrint(('DEBUG: TOCxAgeSDLIntShowHideMore.EnableObject:  Attempting to enable drawing and collision on %s...' % self.sceneobject.getName()))
        self.sceneobject.draw.enable()
        self.sceneobject.physics.suppress(false)


    def DisableObject(self):
        PtDebugPrint(('DEBUG: TOCxAgeSDLIntShowHideMore.DisableObject:  Attempting to disable drawing and collision on %s...' % self.sceneobject.getName()))
        self.sceneobject.draw.disable()
        self.sceneobject.physics.suppress(true)

        
    def SDLInvolved(self):
        if (AgeStartedIn == PtGetAgeName()):
            ageSDL = PtGetAgeSDL()

            i = self.SDLList -1
            while i >= 0:
                if (self.Active == True):
                    try:
                        SDLvalue = ageSDL[VARList[i].value][0]
                    except:
                        PtDebugPrint(('ERROR: TOCxAgeSDLIntShowHideMore.OnServerInitComplete():\tERROR: age sdl read failed, SDLvalue = 0 by default. %s = %s' % (VARList[i].value, VARList[i].value[0])))
                        
                    if (SDLvalue in VARListADD[i]):
                        self.Active = True
                        PtDebugPrint(('DEBUG: TOCxAgeSDLIntShowHideMore.OnServerInitComplete():\tSDL %s has the desired variable %s = TRUE' % (VARList[i].value, VARListADD[i])))
                    else:
                        self.Active = False
                        PtDebugPrint(('DEBUG: TOCxAgeSDLIntShowHideMore.OnServerInitComplete():\tSDL %s has NOT the desired variable %s = FALSE | Value is %s' % (VARList[i].value, VARListADD[i], SDLvalue)))
                else:
                    PtDebugPrint(('DEBUG: TOCxAgeSDLIntShowHideMore.OnServerInitComplete():\tBREAK'))
                    break
                i -= 1

            if (self.Active == True):
                self.EnableObject()
            else:
                self.DisableObject()
