# -*- coding: utf-8 -*-
#==============================================================================#
#                                                                              #
#    Offline KI                                                                #
#                                                                              #
#    Copyright (C) 2004-2011  The Offline KI contributors                      #
#    See the file AUTHORS for more info about the contributors (including      #
#    contact information)                                                      #
#                                                                              #
#    This program is free software: you can redistribute it and/or modify      #
#    it under the terms of the GNU General Public License as published by      #
#    the Free Software Foundation, either version 3 of the License, or         #
#    (at your option) any later version, with or (at your option) without      #
#    the Uru exception (see below).                                            #
#                                                                              #
#    This program is distributed in the hope that it will be useful,           #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#    GNU General Public License for more details.                              #
#                                                                              #
#    Please see the file COPYING for the full GPLv3 license, or see            #
#    <http://www.gnu.org/licenses/>                                            #
#                                                                              #
#    Uru exception: In addition, this file may be used in combination with     #
#    (non-GPL) code within the context of Uru.                                 #
#                                                                              #
#==============================================================================#
import string
import os
from Plasma import *
from PlasmaTypes import *
from PlasmaKITypes import *
from PlasmaVaultConstants import *
from PlasmaNetConstants import *
from xPsnlVaultSDL import *
import xUserKI

import re

helpBook = None # needs to be a global variable?!?

fontCaption = "font size=16 face=Arial"
fontText = "font size=12 face=Arial"
fontCommandText = "font size=10 face=Courier"

commandWidth = 59 # font size 12: max. 47 characters; size 10: max. 59 characters
commandIndent = 5

syntax = '''Each argument is enclosed by < and >. Arguments enclosed by <[ and ]> are optional. From a list of optional arguments, you can only skip the last ones, because the KI has to know which ones you skipped - don't skip one argument and use another one coming after it, that is not possible. You can also get the syntax description in-game by passing "help" as first and only argument.

A "color" is either specified by a simple name like "white" or by three values for the red, green and blue part, e.g. "0.5 0.9 0.1". The "player name" is the name of an avatar in the same or another age, but without spaces - use "me" to run the command on yourself. An "object name" is the name of a scene object or a player in the age you are in. Accordingly, a "list of players" or a "list of objects" is a space-separated list of items of the corresponding type, with the additional possibility to use "all" as shortcut for everyone in the current age except for yourself. For lists of objects, you can also specify a pre-defined object list of the current age - see "/list objectlists". If such a list is optional, it defaults to the objects you have under control in flymode. If flymode is disabled, it defaults to your own avatar.

Since Mystler ported these commands for the TOC-MOUL server, some might be broken.'''

commands = '''=== Avatar appearance and animation commands ===

*/afk <[afk-message]>
*/sit
*/wave
*/sneeze
*/clap
*/laugh
*/lol
*/rotfl
*/dance
*/yes
*/no
*/yawn
*/cheer
*/thanks
*/thx
*/cry
*/cries
*/dontknow
*/shrug
*/dunno
*/point
*/amazed
*/askquestion
*/beckonbig
*/beckonsmall
*/blowkiss
*/bow
*/callme
*/cower
*/crazy
*/cringe
*/crossarms
*/doh
*/flinch
*/groan
*/kneel
*/leanleft
*/leanright
*/lookaround
*/okay
*/overhere
*/peer
*/salute
*/scratchhead
*/shakefist
*/shoo
*/slouchsad
*/stop
*/talkhand
*/tapfoot
*/taunt
*/thumbsdown
*/thumbsdown2
*/thumbsup
*/thumbsup2
*/wavebye
*/wavelow
*/winded
*/hug
*/unhug
*/suitup
*/removeki
*/removereltobook
*/haircolor <color>
*/skincolor <color>
*/eyecolor <color>
*/wave2
*/wtf
*/crazy
*/startdance and /stopdance
*/crawl (toggle)
*/aeroplane (toggle)
*/swim (toggle)
*/swimfast (toggle)
*/attack <target> (co-op anim)

=== Chat commands ===

*/p <nickname> <message>
*/shout <message>
*/neighbors <message>
*/buddies <message>
*/reply
*/startlog
*/stoplog
*/clearchat
*/addbuddy
*/removebuddy
*/ignore
*/unignore

=== Avatar warp and cheat commands ===

*/respawn or /sav or /a
*/goto <place> (type "/goto list" or "/goto listall" to see where you can go)
*/spawn
*/jump <height>
*/float <[list of objects]> ("me" by default)
*/nofloat <[list of objects]> ("me" by default)
*/call <[Urwin|Monkey]> (works only in Negilahn and Payiferen)

=== Admin, age developer and control commands ===

*/fogcolor <color> or /fcol <color>
*/fogdensity <start> <end> <density> or /fdens <start> <end> <density>
*/anim <name of animation> (type "/anim list" to see the pre-defined animations, but you can also directly call an animation by its name, for example "MaleBow")
*/struct <name of a struct> <[struct mode]>
*/printstruct <list of objects>
*/tour <tour name> <[camera name]> <[interval]>
*/tourstop
*/observe <[object]> <[camera name]> <[offset for camera behind avatar]> <[camera height offset]> <[target height offset]>
*/entercam <camera name>
*/leavecam <camera name>
*/printcam <[camera name]>

=== Object control ===

*/xyz <relative x coordinate> <relative y coordinate> <relative z coordinate> <[list of objects]>
*/x <relative x coordinate> <[list of objects]>
*/y <relative y coordinate> <[list of objects]>
*/z <relative z coordinate> <[list of objects]>
*/ghost <[list of objects]>
*/unghost <[list of objects]>
*/normalize <[list of objects]>
*/repos <[list of objects]>
*/location <[list of objects]>
*/scale <scale factor> <[list of objects]>|<scale x> <scale y> <scale z> <[list of objects]>
*/rot <angle> <[axis (x|y|z)]> <[list of objects]>

=== Other commands ===

*/me
*/hood
*/nexus
*/stopcam
*/gocam
*/loadcolumns <filename> - works only in Jalak
*/savecolumns <filename> - works only in Jalak
*/info
*/savecolumns <[filename]>
*/loadcolumns <[filename]>
*/loadscript <filename>
*/loopstart <interval> <command>|<interval> <count> <command>
*/loopstop
*/m <command 1> & <command 2> & ... & <command n>
*/enablefp
*/clearcam
*/getfissure
*/reltostars
*/noreltostars
*/quit
*/hideki <hide time>
*/list <list to show>
*/pet <[Raven|Cat]> (Opa's Pet Relto Page found in CoD needed!)
*/enablegps - Enable KI GPS (Need to complete first 2 marker missions!)
*/kilight <time in seconds> - Light the KI (Defaults to 60 seconds)
*/export - Export current opened KI element

=== Global shortcuts ===

*F1 - 1st/3rd person
*F2 - Open KI
*F3 - Relto book
*F4 - Settings
*F5 - Take picture
*F6 - Create text note
*F7 - Add marker
*F8 - Create new marker mission
*Ctrl+1 - /wave
*Ctrl+2 - /laugh
*Ctrl+3 - /clap
*Ctrl+4 - /dance
*Ctrl+5 - Chat gesture
*Ctrl+6 - /sneeze
*Ctrl+7 - /sit
*Ctrl+Pause or Ctrl+Num - Run next command of file loaded using /loadscript (key may depend on keyboard layout)'''

# Helper function
def breakLine(line, firstBreak = True):
    # adds linebreaks so that each line does not exceed the maximum width. If possible, breaks at a space between words.
    width = commandWidth
    if not firstBreak: width = width-commandIndent
    if len(line) <= width: return line
    skip = 0
    i = width
    while i >= 0 and line[i] != ' ': i = i-1
    if i <= 0: i = width # have at least one character per line
    else: skip = 1 # skip the space that we are separating at
    return line[:i] + '\n' + ' '*commandIndent + breakLine(line[i+skip:], False)

def formatLine(match):
    return '\n' + breakLine(match.group(1))

def formatCommands(commands):
    # format lines
    commands = re.sub("\\n\\*([^\\n]+)", formatLine, commands)
    # format captions
    return re.sub("=== ([^\\n]+) ===", "<pb><%s>\\1<%s>" % (fontCaption, fontCommandText), commands)

# Main function
def OnCommand(ki, arg, cmnd, args, playerList, silent):
    if (cmnd == 'help'):
        # Build help Text
        helpText = "<%s>Offline KI Help System: Syntax\n" % fontCaption
        helpText += "<%s>\n%s" % (fontText, syntax)
        helpText += formatCommands(commands)
        # show it
        global helpBook
        xUserKI.KIManager.ToggleMiniKI()
        helpBook = ptBook(helpText, ki.key)
        helpBook.show(1)
        PtToggleAvatarClickability(0) # as we pass "ki.key" above, this is re-enabled in xKI, OnNotify
        return True
    if (cmnd == 'list'):
        (valid, listName) = xUserKI.GetArg(ki, cmnd, args, 'list to show',
            lambda args: len(args) == 1, lambda args: args[0])
        if not valid: return True
        try:
            import xUserKIData
        except:
            ki.DisplayErrorMessage('The Offline KI data module is missing, so there are no %s available' % listName)
            return True
        # now show the list
        age = PtGetAgeName()
        lists = { 'warppoints': xUserKIData.WarpPoints,
            'tours': xUserKIData.CameraTours,
            'cameras': xUserKIData.CameraShortcuts,
            'objectlists': xUserKIData.ObjectLists,
            'structs': xUserKIData.StructLists }
        if listName in lists:
            if not silent:
                if age in lists[listName]:
                    ki.AddChatLine(None, 'There are the following %s in this age: %s' % (listName, xUserKI.JoinList(lists[listName][age])), 0)
                else:
                    ki.AddChatLine(None, 'There are no %s in this age' % listName, 0)
        else:
            ki.DisplayErrorMessage('Choose one of the following lists to show: %s' % xUserKI.JoinList(lists))
        return True
    return False
