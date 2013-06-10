#!/usr/bin/env python

import xml.etree.ElementTree as ET
import os
from random import randint

playlistFolder = 'playlists'

# Prevent ElementTree.write() from adding 'ns0:' prefixes,
# which VLC can't handle. 
ET.register_namespace('', 'http://xspf.org/ns/0/')
# Found that here:
# http://stackoverflow.com/questions/3895951/create-svg-xml-document-without-ns0-namespace-using-python-elementtree

ET.register_namespace('vlc', 'http://www.videolan.org/vlc/playlist/ns/0/')

def getSourceDirs():
    """
    This will accept commandline arguments or config file settings, and return
    a dict of directories from which to source the media files.
    For now it is hard-coded.
    """
    media = {}
    hardCodedSource = 'C:\\Python27\\projects\\xspfShuffler\\media\\'
    media['a'] = os.path.join(hardCodedSource, 'a') # Programmes (long)
    media['b'] = os.path.join(hardCodedSource, 'b') # Ad breaks (medium)
    media['c'] = os.path.join(hardCodedSource, 'c') # interstitials (short)
    return media

def joinLists(listA, listB, listC):
    pass
    
def writeNewPlaylist(playlist):
    pass
   
def main():
    mediaPaths = getSourceDirs()
    
    # fill lists from contents of paths

    # jumble lists

    # merge lists in described order
    joinLists()

    # write out new playlist to current folder
    writeNewPlaylist()
    

if __name__ == "__main__":
    os.chdir('C:\\Python27\\projects\\xspfShuffler')
    main()

