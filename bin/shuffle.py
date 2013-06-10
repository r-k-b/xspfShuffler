#!/usr/bin/env python

import xml.etree.ElementTree as ET
import os, random, urllib

playlistFolder = 'playlists'

# Prevent ElementTree.write() from adding 'ns0:' prefixes,
# which VLC can't handle. 
ET.register_namespace('', 'http://xspf.org/ns/0/')
# Found that here:
# http://stackoverflow.com/questions/3895951/create-svg-xml-document-without-ns0-namespace-using-python-elementtree

ET.register_namespace('vlc', 'http://www.videolan.org/vlc/playlist/ns/0/')

MEDIA_LONG = 'a' # Programmes
MEDIA_MED = 'b' # Ad breaks
MEDIA_SHORT = 'c' # interstitials

def getSourceDirs():
    """
    This will accept commandline arguments or config file settings, and return
    a dict of directories from which to source the media files.
    For now it is hard-coded.
    """
    media = {}
    hardCodedSource = 'C:\\Python27\\projects\\xspfShuffler\\media\\'
    media[MEDIA_LONG] = os.path.join(hardCodedSource, 'a') # Programmes (long)
    media[MEDIA_MED] = os.path.join(hardCodedSource, 'b') # Ad breaks (medium)
    media[MEDIA_SHORT] = os.path.join(hardCodedSource, 'c') # interstitials (short)
    return media

def fillLists(mediaPaths):
    # fill lists from contents of paths
    mediaLists = {}
    for mediaType in mediaPaths:
        mediaLists[mediaType] = []
        for filename in os.listdir(mediaPaths[mediaType]):
            mediaLists[mediaType].append(filename)
            # non-applicable filetypes to be pruned here
    return mediaLists

def shuffleLists(mediaLists):
    for mediaType in mediaLists:
        if mediaType == MEDIA_LONG: # alphanumeric order
            mediaLists[mediaType].sort()
        else: # random order
            random.shuffle(mediaLists[mediaType])
    return mediaLists
    
def joinLists(mediaLists, mediaPaths):
    # Lists are already in proper order (sorted or shuffled).
    # outputList contains full paths with the filenames.
    outputList = []
    loopcounter = 0
    for mediaFile_long in mediaLists[MEDIA_LONG]:
        outputList.append(os.path.join(mediaPaths[MEDIA_LONG], mediaFile_long))
        for i in range(0,2):
            outputList.append(os.path.join(mediaPaths[MEDIA_MED],
                              mediaLists[MEDIA_MED][
                                  (loopcounter + i) % len(mediaLists[MEDIA_MED])
                              ]))
            outputList.append(os.path.join(mediaPaths[MEDIA_SHORT],
                              mediaLists[MEDIA_SHORT][
                                  (loopcounter + i) % len(mediaLists[MEDIA_SHORT])
                              ]))
        loopcounter += 2
    return outputList
    
def writeNewPlaylist(playlist, outputFile = None):
    # with thanks to muratkarakus7
    xPlaylistRoot = ET.Element('playlist')
    xPlaylistRoot.set('version', '1')
    xPlaylistRoot.set("xmlns", "http://xspf.org/ns/0/") # required?
    xPlaylistRoot.set("xmlns:vlc", "http://www.videolan.org/vlc/playlist/ns/0/") # required?
    xPlaylistTitle = ET.SubElement(xPlaylistRoot, "title")
    xPlaylistTitle.text = "xspfShuffler Generated Playlist"
    xPlaylistTrackList = ET.SubElement(xPlaylistRoot, "trackList")

    for mediaItem in playlist:
        #mediaItem = urllib.quote(str(mediaItem))
        xPlaylistTrackFile = ET.SubElement(xPlaylistTrackList, "track")
        xPlaylistTrackLocation = ET.SubElement(xPlaylistTrackFile, "location")
        xPlaylistTrackLocation.text = 'file:///' + mediaItem

    xPlaylistTree = ET.ElementTree(xPlaylistRoot)
    #ET.dump(xPlaylistTree)
   
def main():
    mediaPaths = getSourceDirs()
    
    # fill lists from contents of paths
    mediaLists = fillLists(mediaPaths)
    
    # jumble lists
    mediaLists = shuffleLists(mediaLists)

    #print mediaLists

    # merge lists in described order (refer SPEC.md)
    newList = joinLists(mediaLists, mediaPaths)

    #for thing in newList:
    #    print thing

    # write out new playlist to current folder
    writeNewPlaylist(newList)
    

if __name__ == "__main__":
    os.chdir('C:\\Python27\\projects\\xspfShuffler')
    main()

