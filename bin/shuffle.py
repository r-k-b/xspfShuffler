#!/usr/bin/env python

import xml.etree.ElementTree as ET
import os

playlistFolder = 'playlists'

# Prevent ElementTree.write() from adding 'ns0:' prefixes,
# which VLC can't handle. 
ET.register_namespace('', 'http://xspf.org/ns/0/')
# Found that here:
# http://stackoverflow.com/questions/3895951/create-svg-xml-document-without-ns0-namespace-using-python-elementtree

def main():
    if not os.path.isdir(playlistFolder):
        print "Do you have a subdirectory named '{0}' ?".format(playlistFolder)
        raise IOError('Didn\'t find the expected subfolder named \'{0}\'.'.format(playlistFolder))
    
    try:
        listA = ET.parse(os.path.join(playlistFolder, 'ListA.xspf'))
        listB = ET.parse(os.path.join(playlistFolder, 'ListB.xspf'))
        listC = ET.parse(os.path.join(playlistFolder, 'ListCD.xspf'))
    except (IOError, ET.ParseError) as err:
        print "Error: {0}: {1}".format(type(err), err)
        print ("Do you have valid VLC playlists named ListA.xspf, " 
            "ListB.xspf, and ListC.xspf in the subfolder?")
        

if __name__ == "__main__":
    main()
