# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaNetConstants import *
from codJournals import *
kPublicAgeLink = 6
PageStart = '<pb>'
ImgStart = '<img src=\"'
TransImgStart = '<img opacity=0.7 src=\"'
ImgEnd = '\" align=center link=%d blend=alpha>'
ImgEndNoLink = '\" align=center blend=alpha>'
ImgEndNoResize = '\" align=center link=%d blend=alpha resize=no>'
ImgEndNoLinkNoResize = '\" align=center blend=alpha resize=no>'
AlignCenter = '<p align=center>'
AlignLeft = '<p align=left>'
AlignRight = '<p align=right>'
MovieLinkStart = '<movie src=\"avi\\'
MovieLinkEnd = '.bik\" align=center link=%d resize=yes>'
AgeBooks = {'RosenJournal': ('<cover src=\"RosenCover\"><margin right=32 left=32>', '<font size=16 face=segoesc color=000000>', 0, 0, 'BkBook', 0.80000000000000004, 1.0),
            'StoryJournal01': ('<cover src=\"StoryCover01\"><margin right=32 left=32>', '<font size=16 face=Sunshine color=000000>', 0, 0, 'BkBook', 0.80000000000000004, 1.0),
            'StoryJournal01a': ('<cover src=\"StoryCover01a\"><margin right=32 left=32>', '<font size=16 face=Courier color=000000>', 0, 0, 'BkBook', 0.80000000000000004, 1.0),
            'StoryJournal02': ('<cover src=\"StoryCover02\"><margin right=32 left=32>', '<font size=16 face=Sunshine color=000000>', 0, 0, 'BkBook', 0.80000000000000004, 1.0),
            'StoryJournal02a': ('<cover src=\"StoryCover02a\"><margin right=32 left=32>', '<font size=16 face=Courier color=000000>', 0, 0, 'BkBook', 0.80000000000000004, 1.0)}
BookPages = {'RosenPage': RosenText,
             'StoryPage01': StoryText01,
             'StoryPage01a': StoryText01a,
             'StoryPage02': StoryText02,
             'StoryPage02a': StoryText02a}
LinkDestinations = {'RosenPage': (None, None, None, None),
                    'StoryPage01': (None, None, None, None),
                    'StoryPage01a': (None, None, None, None),
                    'StoryPage02': (None, None, None, None),
                    'StoryPage02a': (None, None, None, None)}
