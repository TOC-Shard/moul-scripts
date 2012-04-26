# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *
from PlasmaKITypes import *
from PlasmaVaultConstants import *
from PlasmaNetConstants import *

#Global Constants
Pet = None
MyAvatar = None
SAvatars = []
SPets = []
kPetT = 1
kSPetT = 2
kReSpawnT = 3
kSendIDsT = 4
kResetLinkT = 5
YeeshaVal = 0


class xPetBrain(ptModifier):

    __module__ = __name__

    def __init__(self):
        ptModifier.__init__(self)
        self.id = 7483926
        self.version = 9
        print '__init__xPetBrain v.',
        print self.version
        self.Timer = 0
        self.linkIn = 0

    def getChronicleEntry(self):
        vault = ptVault()
        if type(vault) != type(None): #is the Vault online?
            entry = vault.findChronicleEntry('PetType')
            if (type(entry) == type(None)): #does entry exist?
                PtDebugPrint("DEBUG xPetBrain::getChronicleEntry - No entry found...creating")
                vault.addChronicleEntry('PetType', 0, 'PetCat')
                PetType = 'PetCat'
            else:
                PetType = entry.chronicleGetValue()
        else:
            PtDebugPrint("ERROR xPetBrain::getChronicleEntry - Vault offline?")

        return PetType

    def OnServerInitComplete(self):
        global MyAvatar
        global Pet
        global YeeshaVal

        AgeName = PtGetAgeName()
        PtDebugPrint("DEBUG xPetBrain::OnServerInitComplete - Age = %s" % AgeName)
        MyAvatar = PtGetLocalAvatar()
        if ((AgeName != 'Personal') and (AgeName != 'AvatarCustomization')): #Pet sits in Hut
            PtDebugPrint("xPetBrain::OnServerInitComplete - Getting psnlSDL")
            vault = ptVault()
            if type(vault) != type(None): #is the Vault online?
                psnlSDL = vault.getPsnlAgeSDL()
                if psnlSDL:
                    YeeshaPageVarCat = psnlSDL.findVar("YeeshaPage26") #Find CatVar
                    YeeshaPageVarCat = YeeshaPageVarCat.getInt()
                    PtDebugPrint("xPetBrain::OnServerInitComplete - Var found")
                else:
                    YeeshaPageVarCat = 0
                    PtDebugPrint("ERROR xPetBrain::OnServerInitComplete - no psnlSDL found")
            else:
                YeeshaPageVarCat = 0
                PtDebugPrint("ERROR xPetBrain::OnServerInitComplete - Vault offline?")

            YeeshaVal = YeeshaPageVarCat
            if (YeeshaPageVarCat == 1):
                PetType = self.getChronicleEntry()
                PtDebugPrint("xPetBrain::OnServerInitComplete - YeeshaPage active...enable Pet %s" % PetType)
                PtDebugPrint("xPetBrain::OnServerInitComplete - FindingPlayer")
                Petkey = MyAvatar.getKey() #Find SpawnPointKey
                try:
                    Petkey = PtLoadAvatarModel(PetType, Petkey, "My Avatar") #enable Pet
                except:
                    PtDebugPrint("ERROR xPetBrain::OnServerInitComplete - Custom Avatar not found...Spawning Cat")
                    Petkey = PtLoadAvatarModel("PetCat", Petkey, "My Avatar")
                Pet = Petkey.getSceneObject()
                PtAtTimeCallback(self.key, 0.1, kPetT)
                PtAtTimeCallback(self.key, 3.5, kSendIDsT)
            else:
                PtDebugPrint("xPetBrain::OnServerInitComplete - YeeshaPage not found or inactive...disable Pet %i" % YeeshaPageVarCat)

            if (len(PtGetPlayerList()) > 0):
                #If more Player than you are in this Age, they need your and the Pet's Key
                PtAtTimeCallback(self.key, 1, kSPetT)
                self.Timer = 1
                PtDebugPrint("xPetBrain::OnServerInitComplete - More Players are in...Sending my Respawn request")
                myID = PtGetClientIDFromAvatarKey(PtGetLocalAvatar().getKey())
                noteJ = ptNotify(self.key)
                noteJ.clearReceivers()
                noteJ.addReceiver(self.key)
                noteJ.setActivate(1)
                noteJ.netForce(1)
                noteJ.addVarKey('Join', MyAvatar.getKey())
                noteJ.send() #sending Join


    def ReSpawnPet(self):
        global SAvatars
        global SPets
        global Pet
        global MyAvatar
        global YeeshaVal

        if (YeeshaVal == 1):
            PtDebugPrint("DEBUG xPetBrain::ReSpawnPet - Someone joind the Age...Respawning all Avatars")
            i = 0
            while (i < len(SAvatars)):
                try:
                    PtUnLoadAvatarModel(SPets[i].getKey())
                except:
                    PtDebugPrint("ERROR xPetBrain::AvatarPage - Something goes wrong #118")
                i += 1
            SAvatars = []
            SPets = []
            PtUnLoadAvatarModel(Pet.getKey())
            Petkey = MyAvatar.getKey() #Find SpawnPointKey
            PetType = self.getChronicleEntry()
            try:
                Petkey = PtLoadAvatarModel(PetType, Petkey, "My Avatar") #enable Pet
            except:
                PtDebugPrint("ERROR xPetBrain::OnServerInitComplete - Custom Avatar not found...Spawning Cat")
                Petkey = PtLoadAvatarModel("PetCat", Petkey, "My Avatar")
            Pet = Petkey.getSceneObject()
            PtDebugPrint("xPetBrain::ReSpawnPet - Resending my Pet")
            myID = PtGetClientIDFromAvatarKey(PtGetLocalAvatar().getKey())
            noteP = ptNotify(self.key)
            noteP.clearReceivers()
            noteP.addReceiver(self.key)
            noteP.setActivate(1)
            noteP.netForce(1)
            noteP.addVarKey('Pet', Petkey)
            noteP.send() #sending PetKey
            PtDebugPrint("xPetBrain::ReSpawnPet - Resending my ID")
            noteA = ptNotify(self.key)
            noteA.clearReceivers()
            noteA.addReceiver(self.key)
            noteA.setActivate(1)
            noteA.netForce(1)
            noteA.addVarNumber('Avatar', myID)
            noteA.send() #sending AvatarKey
            PtDebugPrint("DEBUG xPetBrain::ReSpawnPet - Cleaning up complete")
        PtAtTimeCallback(self.key, 1, kResetLinkT)

    def OnNotify(self, state, id, events):
        global SAvatars
        global SPets
        global Pet
        global MyAvatar
        global YeeshaVal

        PtDebugPrint("xPetBrain::OnNotify - Receive a Notify: %s" % events[0][1])
        for event in events:
            if (event[0] == kVariableEvent):
                if (YeeshaVal == 1):
                    if ((event[1] == 'Pet') and (event[3] != Pet.getKey())): #receive PetKey
                        PtDebugPrint("xPetBrain::OnNotify - Get new Petkey")
                        #PetAva = event[1]
                        #AvatarID = int(event[3])
                        #SAvatar = ptSceneobject(PtGetAvatarKeyFromClientID(AvatarID), self.key)
                        #Petkey = SAvatar.getKey() #Find SpawnPointKey
                        #Petkey = PtLoadAvatarModel(PetAva, Petkey, "My Avatar") #enable Cat
                        Petkey = event[3]
                        SPets.append(Petkey.getSceneObject())
                else:
                    if (event[1] == 'Pet'):
                        PtDebugPrint("xPetBrain::OnNotify - Get new Petkey")
                        Petkey = event[3]
                        SPets.append(Petkey.getSceneObject())

                if ((event[1] == 'Avatar') and (event[3] != PtGetClientIDFromAvatarKey(MyAvatar.getKey()))): #receive AvatarKey
                    PtDebugPrint("xPetBrain::OnNotify - Get new Avatarkey %i" % event[3])
                    AvatarID = int(event[3])
                    SAvatars.append(ptSceneobject(PtGetAvatarKeyFromClientID(AvatarID), self.key))
                if ((event[1] == 'Join') and (event[3] != MyAvatar.getKey())):
                    PtDebugPrint("xPetBrain::OnNotify - Get Command to Respawn")
                    if (not(self.Timer)):
                        PtAtTimeCallback(self.key, 1, kSPetT)
                        self.Timer = 1
                    PtAtTimeCallback(self.key, 3, kReSpawnT)
                    self.linkIn = 1

    def BeginAgeUnLoad(self,avObj):
        global MyAvatar
        global Pet
        global SAvatars
        global SPets

        PtDebugPrint("DEBUG xPetBrain::BeginAgeUnLoad - Player leaving the age")
        if (avObj == MyAvatar):
            try:
                PtUnLoadAvatarModel(Pet.getKey()) #Unload Pet, so we don't have 2 Pets in next Age
            except:
                PtDebugPrint("xPetBrain::BeginAgeUnLoad - Something goes wrong. #201")
            i = 0
            while (i < len(SAvatars)):
                try:
                    PtUnLoadAvatarModel(SPets[i].getKey())
                except:
                    PtDebugPrint("ERROR xPetBrain::BeginAgeUnLoad - something goes wrong. #195")
                i += 1
            SAvatars = [] #reseting lists for next Age
            SPets = []

    def AnimControl(self):
        global Pet
        global MyAvatar

        if (Pet != MyAvatar):
            Pet.avatar.oneShot(MyAvatar.getKey(),0,1,'Idle',0,0)

        PtAtTimeCallback(self.key, 0.1, kPetT)

    def SAnimControl(self):
        global SPets
        global SAvatars

        if (not(self.linkIn)):
            i = 0
            if (len(SPets) != len(SAvatars)):
                PtDebugPrint("ERROR xPetBrain::SAnimControl - lenght dont match")
            if (len(SAvatars) > 0): #Are Players in?
                while (i < len(SPets)):
                    try:
                        dtct = PtGetClientIDFromAvatarKey(SAvatars[i].getKey()) #test if Player is already in the Age
                        if (dtct == -1): #Ghost Player - Player left the Age
                            PtUnLoadAvatarModel(SPets[i].getKey())
                            self.UpdateAvatarPetList(i)
                        SPets[i].avatar.oneShot(SAvatars[i].getKey(),300,1,'Idle',0,0)
                        i += 1
                    except:
                        self.UpdateAvatarPetList(i)

        PtAtTimeCallback(self.key, 1, kSPetT)

    def UpdateAvatarPetList(self, index):
        global SPets
        global SAvatars

        PtDebugPrint("xPetBrain::UpdateAvatarPetList - Leaving Player detected")
        i = 0
        SPets2 = []
        SAvatars2 = []
        while (i < len(SAvatars)):
            if (i != index):
                try:
                    SPets2.append(SPets[i])
                    SAvatars2.append(SAvatars[i])
                except:
                    PtDebugPrint("ERROR xPetBrain::UpdateAvatarPetList - something goes wrong. #202")
            i += 1

        SPets = SPets2
        SAvatars = SAvatars2

    def OnTimer(self, id):
        global Pet
        global MyAvatar
        global YeeshaVal

        if (id == kPetT):
            self.AnimControl()

        if (id == kSPetT):
            self.SAnimControl()

        if (id == kReSpawnT):
            self.ReSpawnPet()

        if (id == kSendIDsT):
            if (YeeshaVal == 1):
                myID = PtGetClientIDFromAvatarKey(MyAvatar.getKey())
                PtDebugPrint("xPetBrain::OnServerInitComplete - Sending my Pet")
                noteP = ptNotify(self.key)
                noteP.clearReceivers()
                noteP.addReceiver(self.key)
                noteP.setActivate(1)
                noteP.netForce(1)
                noteP.addVarKey('Pet', Pet.getKey())
                noteP.send() #sending PetKey
                PtDebugPrint("xPetBrain::OnServerInitComplete - Sending my ID")
                noteA = ptNotify(self.key)
                noteA.clearReceivers()
                noteA.addReceiver(self.key)
                noteA.setActivate(1)
                noteA.netForce(1)
                noteA.addVarNumber('Avatar', myID)
                noteA.send() #sending AvatarKey

        if (id == kResetLinkT):
            self.linkIn = 0
