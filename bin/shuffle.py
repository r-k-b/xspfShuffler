#!/usr/bin/env python

import xml.etree.ElementTree as ET
import os, random, urllib, yaml

playlistFolder = 'playlists'

MEDIA_LONG = 'a' # Programmes
MEDIA_MED = 'b' # Ad breaks
MEDIA_SHORT = 'c' # interstitials

def getConfiguration(configOption):
    """
    This will accept commandline arguments or config file settings, and return:
    - a dict of directories from which to source the media files, or
    - the destination directory for the generated playlist file.
    Command-line argument parsing to be added.
    """
    configFile = 'xspfShuffler.config' # should be in cwd?
    try:
        with open(configFile) as f:
            config = yaml.safe_load(f)
    except IOError as e:
        raise IOError(
            'Couldn\'t open the config file ({0}).'.format(configFile))
    
    if configOption == 'mediaPaths':
        media = {}
        media[MEDIA_LONG] = config['media_dir_long'] # Programmes (long)
        media[MEDIA_MED] = config['media_dir_med'] # Ad breaks (medium)
        media[MEDIA_SHORT] = config['media_dir_short'] # interstitials (short)
        return media

    if configOption == 'outputFolder':
        outputFolder = config['output_xspf_dir']
        return outputFolder

    # shouldn't get to here
    raise NameError(
        """configOption passed to getConfiguration() was not recognised.
        configOption value: {0}""".format(configOption))

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
    # Pattern: A B C B C A B C B C A B C B C...
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
    if outputFile == None:
        outputFile = os.path.join('.', 'testOutput.xspf')
    xPlaylistTree.write(outputFile)
   
def main():
    mediaPaths = getConfiguration('mediaPaths')
    outputFolder = getConfiguration('outputFolder')
    
    # fill lists from contents of paths
    mediaLists = fillLists(mediaPaths)
    
    # jumble lists
    mediaLists = shuffleLists(mediaLists)

    # merge lists in described order (refer SPEC.md)
    newList = joinLists(mediaLists, mediaPaths)

    # write out new playlist to current folder
    writeNewPlaylist(newList)
    

if __name__ == "__main__":
    os.chdir('C:\\Python27\\projects\\xspfShuffler')
    main()

