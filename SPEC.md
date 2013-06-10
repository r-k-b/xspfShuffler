# xspfShuffler

## Overview
- Folder 'A' contains 'long' videos ('Programmes').  
	Nominal duration > 10 minutes.
- Folder 'B' contains 'medium length' videos ('Interstitials')  
	Nominal 2 minutes < duration < 10 minutes.
- Folder 'C' contains 'short' videos ('Ad breaks').  
	Nominal duration < 2 minutes.
- ListA is a list of media files from Folder 'A' sorted to alphanumeric order, then translated by a random amount.
- ListB is a list of media files from Folder 'B' sorted in random order.
- ListC is a list of media files from Folder 'C' sorted in random order.
- Iterate **once** through ListA, and repeatedly through ListB and ListC, appending copies to new outputList in the following repeating order:
	> A C B C B C 
- List 'outputList' is converted to xspf format and written to disk.

## Scenarios
###Scenario A: 
1. User has three folders of videos (as described in Overview)
2. User runs shuffle.py, either:
	- Passing in the three folders (ListA, ListB, ListC) as arguments, or
	- Passing no arguments, and having shuffle.py try to find the three folders automatically (from config file?)	
3. shuffle.py creates the xspf file representing List D, in the current directory. (named like 'tvplaylist_2013-12-31-091059.xspf' ?)
4. VLC is started, and passed the new playlist file.
5. Process is repeated from step 3 each time VLC is to be started (daily?)
6. Process is repeated from step 1 each time any of the three initial playlists are modified. 

## Non-Goals
- Graphical UI.
- ...

## Open issues
...