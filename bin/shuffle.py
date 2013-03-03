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

def loadPlaylists():
    if not os.path.isdir(playlistFolder):
        print "Do you have a subdirectory named '{0}' ?".format(playlistFolder)
        raise IOError('Didn\'t find the expected subfolder named \'{0}\'.'.format(playlistFolder))
    
    try:
        listA = ET.parse(os.path.join(playlistFolder, 'ListA.xspf'))
        listB = ET.parse(os.path.join(playlistFolder, 'ListB.xspf'))
        listC = ET.parse(os.path.join(playlistFolder, 'ListC.xspf'))
    except (IOError, ET.ParseError) as err:
        print "Error: {0}: {1}".format(type(err), err)
        print ("Do you have valid VLC playlists named ListA.xspf, " 
            "ListB.xspf, and ListC.xspf in the subfolder?")
    
    return listA, listB, listC

def jumblePlaylist(playlist):
    playlist_root = playlist.getroot()
    playlist_length = len(playlist_root[1])
    playlist_offset = randint(0, playlist_length)
    print playlist_length, playlist_offset
    
    playlist_jumbledroot = playlist_root
    playlist_jumbledroot[1].clear()
    
    for newtrack in range(playlist_length):
        oldtrack = (newtrack + playlist_offset) % playlist_length
        print oldtrack, newtrack
        playlist_jumbledroot[1].append(playlist_root[1][oldtrack])
    
    playlist._setroot(playlist_jumbledroot)
    return playlist

def joinPlaylists(listA, listB, listC):
    pass
    
def writeNewPlaylist(playlist):
    pass
   
def main():
    listA, listB, listC = loadPlaylists()
    listD = joinPlaylists(listA, listB, listC)
    writeNewPlaylist(listD)

if __name__ == "__main__":
    os.chdir('C:\\Python27\\projects\\xspfShuffler')
    main()

# testing - disable these
a,b,c = loadPlaylists()
ar = a.getroot()
br = b.getroot()
cr = c.getroot()
a.findall('{http://xspf.org/ns/0/}extension/*')
a.findall('{http://xspf.org/ns/0/}tracklist/*') # WHY IS TRACKLIST EMPTY???
d = jumblePlaylist(a)
