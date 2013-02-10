from Plasma import *

LockedAges = ['EderDelin', 'EderTsogal']

def IsAdmin():
    if PtIsInternalRelease():
        return True
    else:
        return False

def IsLockedAge():
    if IsAdmin(): return False
    if PtGetAgeName() in LockedAges: return True
    return False
