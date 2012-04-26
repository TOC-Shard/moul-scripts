# -*- coding: utf-8 -*-
def ReadJournal(filename):
    try:
        file = open(filename, 'r')
        filecontents = file.read()
        file.close()
        return filecontents
    except Exception, detail:
        print 'codJournals: ',
        print detail
        return 'WHAT THE FUCK!!! This really should not happen.'

RosenText = ReadJournal('dat/BookResources/cod--RosenJournal.txt')
StoryText01 = ReadJournal('dat/BookResources/cod--StoryJournal01.txt')
StoryText01a = ReadJournal('dat/BookResources/cod--StoryJournal01a.txt')
StoryText02 = ReadJournal('dat/BookResources/cod--StoryJournal02.txt')
StoryText02a = ReadJournal('dat/BookResources/cod--StoryJournal02a.txt')
