# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaTypes import *
from PlasmaKITypes import *
from PlasmaNetConstants import *
import xLinkingBookDefs
actClickableObject = ptAttribActivator(1, 'Act: Clickable Object')
strObject = ptAttribString(2, 'Object String')
Behavior = ptAttribBehavior(3, 'Avatar link animation (optional)')
ourBook = None
bkLinks = []
ageLinkStruct = None
kLinkID = 1
publicAges = []
kPublicAgeLink = 6
kPublicAgesMOUL = ['city', 'Neighborhood', 'Neighborhood02', 'GreatTreePub', 'GuildPub-Cartographers', 'GuildPub-Greeters', 'GuildPub-Maintainers', 'GuildPub-Messengers', 'GuildPub-Writers', 'philRelto', 'Kveer']
modPageDefs = 'codPageDefs'
ageBooks = ['RosenJournal', 'StoryJournal01', 'StoryJournal01a', 'StoryJournal02', 'StoryJournal02a']
bookPages = [['RosenPage'], ['StoryPage01'], ['StoryPage01a'], ['StoryPage02'], ['StoryPage02a']]
parentAge = 'Neighborhood'
kLinkDelay = 3.5
vOpenSource = false

class codBookGUI(ptModifier):
    __module__ = __name__
    def __init__(self):
        ptModifier.__init__(self)
        self.id = 3719432
        version = 27
        minor = 4
        self.version = version
        self.me = self.__class__.__name__
        self.PageDefs = __import__(modPageDefs)
        PtDebugPrint(('__init__codBookGUI v%d.%d' % (version, minor)))


    def OnNotify(self, state, id, events):
        global ourBook
        global bkLinks
        if ((id == actClickableObject.id) and state):
            print ('%s: OnNotify: Someone clicked on object %s' % (self.me, strObject.value))
            if PtWasLocallyNotified(self.key):
                print 'It was you'
                for (a, b) in zip(ageBooks, bookPages):
                    print ('Trying book %s with page(s) %s' % (a, b))
                    if (strObject.value == a):
                        print 'Match found! Start opening book...'
                        self.IOpenBook(a, b)
                        break
                    else:
                        print 'No match'
        else:
            for event in events:
                if ((event[0] == PtEventType.kBook) and PtWasLocallyNotified(self.key)):
                    if (event[1] == PtBookEventTypes.kNotifyImageLink):
                        print ('BookNotify: Linking panel id=%d, event=%d' % (event[2], event[1]))
                        ourBook.hide()
                        if (event[2] == 0):
                            print 'Warning: No link id, define proper link destination or use non-clickable image'
                        elif (event[2] >= xLinkingBookDefs.kFirstLinkPanelID):
                            for i in range(0, len(bkLinks)):
                                if (event[2] == bkLinks[i][0]):
                                    try:
                                        self.IlinkToAge(bkLinks[i][1], bkLinks[i][2], bkLinks[i][3], bkLinks[i][4], bkLinks[i][5])
                                    except Exception, detail:
                                        print ('ERROR: Unable to initialize link - %s' % detail)
                                    break
                    elif (event[1] == PtBookEventTypes.kNotifyShow):
                        print ('BookNotify: Show book, event=%d' % event[1])
                        PtToggleAvatarClickability(0)
                    elif (event[1] == PtBookEventTypes.kNotifyHide):
                        print ('BookNotify: Hide book, event=%d' % event[1])
                        PtToggleAvatarClickability(1)
                    elif (event[1] == PtBookEventTypes.kNotifyNextPage):
                        print ('BookNotify: To next page %d, event=%d' % (ourBook.getCurrentPage(), event[1]))
                    elif (event[1] == PtBookEventTypes.kNotifyPreviousPage):
                        print ('BookNotify: To previous page %d, event=%d' % (ourBook.getCurrentPage(), event[1]))
                    elif (event[1] == PtBookEventTypes.kNotifyCheckUnchecked):
                        print ('BookNotify: Relto page toggle, event=%d' % event[1])
                    elif (event[1] == PtBookEventTypes.kNotifyClose):
                        print ('BookNotify: Close book, event=%d' % event[1])
                elif (event[0] == kVariableEvent):
                    AvatarID = int(event[3])
                    Avatar = ptSceneobject(PtGetAvatarKeyFromClientID(AvatarID), self.key)
                    print ('Notify: Avatar %d started to link, show animation' % AvatarID)
                    Behavior.run(Avatar)


    def OnTimer(self, id):
        global ageLinkStruct
        if (id == kLinkID):
            if (type(ageLinkStruct) != type(None)):
                print ('%s: OnTimer: Really linking now...' % self.me)
                linkMgr = ptNetLinkingMgr()
                linkMgr.linkToAge(ageLinkStruct)


    def gotPublicAgeList(self, ages):
        global publicAges
        try:
            for age in ages:
                publicAges.append(age[0])
        except IndexError:
            pass


    def IOpenBook(self, ageBook, bkPages = None):
        global bkLinks
        global ourBook
        print ('%s: IOpenBook: Page(s) requested %s' % (self.me, bkPages))
        if (type(bkPages) == type(None)):
            print 'ERROR: no pages defined'
            return
        if (not ((ageBook in self.PageDefs.AgeBooks))):
            print ('ERROR: Definition %s does not exist in AgeBooks' % ageBook)
            return
        bkParams = self.PageDefs.AgeBooks[ageBook]
        (bkCover, bkFont, startOpen, forceOwned, bookGUI, width, height) = bkParams
        PageDef = (bkCover + bkFont)
        if (not (startOpen)):
            if (not (self.IsThereACover(PageDef))):
                print 'Warning: Missing cover, forcing book open'
                startOpen = 1
        PageCount = xLinkingBookDefs.kFirstLinkPanelID
        bkLinks = []
        for bkPage in bkPages:
            if (not ((bkPage in self.PageDefs.LinkDestinations))):
                print ('Warning: %s skipped, definition does not exist in LinkDestinations' % bkPage)
                continue
            pgParams = self.PageDefs.LinkDestinations[bkPage]
            (bkAge, spawnPoint, spTitle, linkRule) = pgParams
            alink = 1
            if ((type(bkAge) != type(None)) and forceOwned):
                print ('Ownership check for %s book' % bkAge)
                vault = ptVault()
                ainfo = ptAgeInfoStruct()
                ainfo.setAgeFilename(bkAge)
                alink = vault.getOwnedAgeLink(ainfo)
            if alink:
                print ('Showing %s, link destination %s' % (bkPage, bkAge))
                if (type(bkAge) != type(None)):
                    t = (PageCount, bkPage, bkAge, spawnPoint, spTitle, linkRule)
                    bkLinks.append(t)
                    PageDef = ((PageDef + (self.PageDefs.BookPages[bkPage] % PageCount)) + '<pb>')
                else:
                    PageDef = ((PageDef + self.PageDefs.BookPages[bkPage]) + '<pb>')
                PageCount = (PageCount + 1)
            else:
                print ('No owner of age %s so we are not showing %s' % (bkAge, bkPage))
        if (PageCount == xLinkingBookDefs.kFirstLinkPanelID):
            print 'No pages created...'
            return
        else:
            TotalCount = (PageCount - xLinkingBookDefs.kFirstLinkPanelID)
        print ('%d item(s) created, linking page(s): %d' % (TotalCount, len(bkLinks)))
        PageDef = PageDef[:-4]
        ourBook = ptBook(PageDef, self.key)
        ourBook.setSize(width, height)
        ourBook.setGUI(bookGUI)
        ourBook.show(startOpen)
        if len(bkLinks):
            ageList = []
            for i in range(0, len(bkLinks)):
                if (bkLinks[i][5] == kPublicAgeLink):
                    ageList.append(bkLinks[i][2])
            if len(ageList):
                self.IGetPublicAges(ageList)


    def IsThereACover(self, bookHtml):
        idx = bookHtml.find('<cover')
        if (idx >= 0):
            return 1
        return 0


    def IlinkToAge(self, bookPage, ageName, spawnPoint, spTitle, linkRule = PtLinkingRules.kBasicLink):
        global publicAges
        global ageLinkStruct
        print ('%s: ILinkToAge: Link request from page %s to age %s' % (self.me, bookPage, ageName))
        if ((type(ageName) == type(None)) or (len(ageName) == 0)):
            print 'ERROR: Cannot link to age without name'
            return
        if ((type(spawnPoint) == type(None)) or (len(spawnPoint) == 0)):
            print 'No spawnpoint defined, checking special actions...'
            self.IDoSpecialAction(bookPage)
            return
        als = ptAgeLinkStruct()
        ainfo = ptAgeInfoStruct()
        ainfo.setAgeFilename(ageName)
        ainfo.setAgeInstanceName(self.IConvertAgeInstanceName(ageName))
        als.setAgeInfo(ainfo)
        if ((type(spTitle) == type(None)) or (len(spTitle) == 0)):
            if ((linkRule == PtLinkingRules.kOriginalBook) or PtIsSinglePlayerMode()):
                if (spawnPoint == 'LinkInPointDefault'):
                    spTitle = 'Default'
                else:
                    print 'Warning: Empty spawnpoint title not allowed, check your link destinations!'
                    return
            else:
                print 'Empty spawnpoint title allowed, continue linking'
                spTitle = ''
        if (linkRule == PtLinkingRules.kChildAgeBook):
            als.setParentAgeFilename(parentAge)
        elif (linkRule == kPublicAgeLink):
            if (not (PtIsSinglePlayerMode())):
                if (not (len(publicAges))):
                    print 'No public ages found, link aborted'
                    return
                als = None
                ageInstances = []
                for i in range(0, len(publicAges)):
                    if (publicAges[i].getAgeFilename() == ageName):
                        ageInstances.append(publicAges[i])
                if len(ageInstances):
                    als = self.IGetPublicLink(ageInstances)
                if (type(als) == type(None)):
                    print 'Missing age link structure, link aborted'
                    return
            linkRule = PtLinkingRules.kBasicLink
        als.setLinkingRules(linkRule)
        spPoint = ptSpawnPointInfo(spTitle, spawnPoint)
        als.setSpawnPoint(spPoint)
        ageLinkStruct = als
        print ('Linking to age %s, spawnpoint %s with title %s, using linkingrule %d' % (ageName, spawnPoint, spTitle, linkRule))
        if (type(Behavior.value) != type(None)):
            myID = PtGetClientIDFromAvatarKey(PtGetLocalAvatar().getKey())
            note = ptNotify(self.key)
            note.clearReceivers()
            note.addReceiver(self.key)
            note.setActivate(1)
            note.addVarNumber('Avatar', myID)
            note.send()
            PtAtTimeCallback(self.key, kLinkDelay, kLinkID)
        else:
            PtAtTimeCallback(self.key, 0.10000000000000001, kLinkID)


    def IGetPublicAges(self, ageList):
        global publicAges
        print ('%s: IGetPublicAges: %s' % (self.me, ageList))
        publicAges = []
        if (not (self.HasPublicAges())):
            print 'ERROR: Public ages not supported in this Uru version!'
            return
        if vOpenSource:
            for age in ageList:
                PtGetPublicAgeList(age, self)
                if (age not in kPublicAgesMOUL):
                    print ('Warning: Age %s is usually not public in MOUL Open Source' % age)
        else:
            for age in ageList:
                PtGetPublicAgeList(age, self)
                if ((age != 'city') and (age != 'Neighborhood')):
                    print ('Warning: Age %s is usually not public in UU' % age)


    def IGetPublicLink(self, instances, highest = 0):
        curGUID = instances[0].getAgeInstanceGuid()
        curInstance = 0
        if (not (highest)):
            for i in range(0, len(instances)):
                if (instances[i].getAgeInstanceGuid() < curGUID):
                    curGUID = instances[i].getAgeInstanceGuid()
                    curInstance = i
        else:
            for i in range(0, len(instances)):
                if (instances[i].getAgeInstanceGuid() > curGUID):
                    curGUID = instances[i].getAgeInstanceGuid()
                    curInstance = i
        try:
            als = ptAgeLinkStruct()
            als.getAgeInfo().copyFrom(instances[curInstance])
            print ('%s: IGetPublicLink: Age link structure found' % self.me)
            return als
        except Exception, detail:
            print ('%s: IGetPublicLink: Age link structure not found - %s' % (self.me, detail))
            return None


    def IConvertAgeInstanceName(self, ageName):
        if (ageName == 'Personal'):
            return 'Relto'
        if (ageName == 'Cleft'):
            return 'D\'ni-Riltagamin'
        if (ageName == 'BahroCave'):
            return 'D\'ni-Rudenna'
        if (ageName == 'BaronCityOffice'):
            return 'Ae\'gura'
        if (ageName == 'city'):
            return 'Ae\'gura'
        if (ageName == 'Garden'):
            return 'Eder Kemo'
        if (ageName == 'Gira'):
            return 'Eder Gira'
        if (ageName == 'Garrison'):
            return 'Gahreesen'
        if (ageName == 'Neighborhood02'):
            return 'DRC Neighborhood'
        if (ageName == 'RestorationGuild'):
            return 'Watcher\'s Guild'
        if (ageName == 'AhnySphere01'):
            return 'Sphere 1'
        if (ageName == 'AhnySphere02'):
            return 'Sphere 2'
        if (ageName == 'AhnySphere03'):
            return 'Sphere 3'
        if (ageName == 'AhnySphere04'):
            return 'Sphere 4'
        if (ageName == 'Descent'):
            return 'D\'ni-Tiwah'
        if (ageName == 'EderDelin'):
            return 'Eder Delin'
        if (ageName == 'EderTsogal'):
            return 'Eder Tsogal'
        if (ageName == 'GreatTreePub'):
            return 'The Watcher\'s Pub'
        if (ageName == 'Ercana'):
            return 'Er\'cana'
        if (ageName == 'Pahts'):
            return 'Ahra Pahts'
        if (ageName == 'Andy_Nexus'):
            return 'Andy\'s Nexus'
        if (ageName == 'Dots_Office'):
            return 'Dot\'s Office'
        if (ageName == 'The_Company_Nexus'):
            return 'The Company Nexus'
        if (ageName == 'KveerMOUL'):
            return 'K\'veer'
        if (ageName == 'KirelMOUL'):
            return 'Kirel'
        if (ageName == 'AhnonayMOUL'):
            return 'Ahnonay'
        if (ageName == 'MystMystV'):
            return 'Myst'
        if (ageName == 'MarshScene'):
            return 'Great Marsh'
        if (ageName == 'MountainScene'):
            return 'Rowan Green'
        return ageName


    def HasPublicAges(self):
        if vOpenSource:
            print 'HasPublicAges: Open Source = true'
            return true
        if PtIsSinglePlayerMode():
            print 'HasPublicAges: Offline = false'
            return false
        try:
            PtForceCursorShown()
        except:
            print 'HasPublicAges: UU = true'
            return true
        print 'HasPublicAges: Alcugs = false'
        return false


    def IDoSpecialAction(self, bookPage):
        if (bookPage == 'CleftSpecial'):
            print ('Special action found for %s' % bookPage)
        else:
            print ('No special action for %s' % bookPage)
