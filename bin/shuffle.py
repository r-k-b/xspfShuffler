#!/usr/bin/env python

import xml.etree.ElementTree as ET
import os

# Prevent ElementTree.write() from adding 'ns0:' prefixes,
# which VLC can't handle. 
ET.register_namespace('', 'http://xspf.org/ns/0/')
# Found that here:
# http://stackoverflow.com/questions/3895951/create-svg-xml-document-without-ns0-namespace-using-python-elementtree

try:
    os.chdir('playlists')
except WindowsError as err:
    print 'Error: {0}: {1}'.format(type(err), err)
    print "Do you have a subdirectory named 'playlists' ?"

try:
    listA = ET.parse('ListA.xspf')
    listB = ET.parse('ListB.xspf')
    listC = ET.parse('ListC.xspf')
except (IOError, ET.ParseError) as err:
    print 'Error: {0}: {1}'.format(type(err), err)
    print 'Do you have valid VLC playlists named ListA.xspf, ListB.xspf, and ListC.xspf ?'
    
