# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *
from PlasmaVaultConstants import *
import os
import glob
import random
actTrigger = ptAttribActivator(1, 'Triggerer')
respOneShot = ptAttribResponder(2, 'Oneshot resp')
respStart = ptAttribResponder(3, 'Start responder')
respStop = ptAttribResponder(4, 'Stop responder')
soSoundObj = ptAttribSceneobject(5, 'Sound sceneobject')
strPath = ptAttribString(6, 'File path')
strSoundObj = ptAttribString(7, 'Sound component name')
CurrentFile = None
SoundObjIndex = 0
IsPlaying = 0
InitialSongName = 'sfx/psnlMusicPlayer.ogg'
sdlCurrentSongVar = 'psnlMusicBoxCurrentSongSelf'

class psnlMusicnew(ptModifier):


    def __init__(self):
        ptModifier.__init__(self)
        self.id = 1300001
        self.version = 1
        PtDebugPrint(('psnlMusicnew: init  version = %d' % self.version))


    def OnServerInitComplete(self):
        global SoundObjIndex
        if (not (os.access("MyMusic", os.F_OK))):
            os.mkdir("MyMusic")
        if (not (os.access(strPath.value, os.F_OK))):
            PtDebugPrint('psnlMusicnew:ERROR! simpleImager: Couldn\'t find the directory...creating', level=kErrorLevel)
            os.mkdir(strPath.value)
        SoundObjIndex = soSoundObj.value.getSoundIndex(strSoundObj.value)
        PtDebugPrint(('psnlMusicnew.OnServerInitComplete: using sound object index:' + str(SoundObjIndex)))
        self.InitMusicBoxSongList()
        ageSDL = PtGetAgeSDL()
        ageSDL[sdlCurrentSongVar] = ('',)


    def OnNotify(self, state, id, events):
        global IsPlaying
        if (not (state)):
            return
        if (id == actTrigger.id):
            respOneShot.run(self.key, events=events)
        elif (id == respOneShot.id):
            if IsPlaying:
                respStop.run(self.key)
            else:
                self.NextSong()
        elif (id == respStart.id):
            IsPlaying = 0
            self.NextSong()


    def FileCmp(self, x, y):
        return cmp(os.stat(y).st_ctime, os.stat(x).st_ctime)


    def PlaySong(self, filename):
        global CurrentFile
        global SoundObjIndex
        global IsPlaying
        if (not (os.path.exists(filename))):
            filename = InitialSongName
        CurrentFile = filename
        if (filename[-4:].lower() == '.ogg'):
            iscompressed = 1
        else:
            iscompressed = 0
        PtDebugPrint(('psnlMusicnew.PlaySong: Going to play: %s' % filename))
        soSoundObj.value.setSoundFilename(SoundObjIndex, filename, iscompressed)
        IsPlaying = 1
        respStart.run(self.key)
        ageSDL = PtGetAgeSDL()
        ageSDL[sdlCurrentSongVar] = (filename,)


    def NextSong(self):
        global CurrentFile
        wavlist = glob.glob((strPath.value + '/*.wav'))
        ogglist = glob.glob((strPath.value + '/*.ogg'))
        filelist = (wavlist + ogglist)
        filelist.sort(self.FileCmp)
        if (not (len(filelist))):
            filelist = self.GetMusicBoxSongList()
        if (not (len(filelist))):
            filelist = [InitialSongName]
        curIndex = 0
        try:
            if CurrentFile:
                curIndex = (filelist.index(CurrentFile) + 1)
        except ValueError:
            pass
        nextIndex = random.randint(0, (len(filelist) - 1))
        if (nextIndex == (curIndex - 1)):
            curIndex = nextIndex + 1
        else:
            curIndex = nextIndex
        if (curIndex >= len(filelist)):
            curIndex = -1
        if (curIndex >= 0):
            self.PlaySong(filelist[curIndex])
        else:
            PtDebugPrint('psnlMusicnew.NextSong: Stopping')
            CurrentFile = None
            ageSDL = PtGetAgeSDL()
            ageSDL[sdlCurrentSongVar] = ('',)


    def InitMusicBoxSongList(self):
        musicBoxChronFound = 0
        ageDataFolder = None
        ageVault = ptAgeVault()
        ageInfoNode = ageVault.getAgeInfo()
        ageInfoChildren = ageInfoNode.getChildNodeRefList()
        for ageInfoChildRef in ageInfoChildren:
            ageInfoChild = ageInfoChildRef.getChild()
            folder = ageInfoChild.upcastToFolderNode()
            if (folder and (folder.folderGetName() == 'AgeData')):
                ageDataFolder = folder
                ageDataChildren = folder.getChildNodeRefList()
                for ageDataChildRef in ageDataChildren:
                    ageDataChild = ageDataChildRef.getChild()
                    chron = ageDataChild.upcastToChronicleNode()
                    if (chron and (chron.getName() == 'MusicBoxSongs')):
                        musicBoxChronFound = 1
        if (not (ageDataFolder)):
            newFolder = ptVaultFolderNode(0)
            newFolder.folderSetName('AgeData')
            ageInfoNode.addNode(newFolder)
            PtAtTimeCallback(self.key, 0.5, 0)
        elif (not (musicBoxChronFound)):
            newNode = ptVaultChronicleNode(0)
            newNode.chronicleSetName('MusicBoxSongs')
            newNode.chronicleSetValue(InitialSongName)
            ageDataFolder.addNode(newNode)


    def OnTimer(self, id):
        self.InitMusicBoxSongList()


    def GetMusicBoxSongList(self):
        ageVault = ptAgeVault()
        ageInfoNode = ageVault.getAgeInfo()
        ageInfoChildren = ageInfoNode.getChildNodeRefList()
        for ageInfoChildRef in ageInfoChildren:
            ageInfoChild = ageInfoChildRef.getChild()
            folder = ageInfoChild.upcastToFolderNode()
            if (folder and (folder.folderGetName() == 'AgeData')):
                ageDataChildren = folder.getChildNodeRefList()
                for ageDataChildRef in ageDataChildren:
                    ageDataChild = ageDataChildRef.getChild()
                    chron = ageDataChild.upcastToChronicleNode()
                    if (chron and (chron.getName() == 'MusicBoxSongs')):
                        return chron.getValue().split(';')
        PtDebugPrint('Error: No music box list found')
        return []
