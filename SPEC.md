# xspfShuffler

## Overview
- List 'A' is an ordered list of 'long' videos ('Programmes').  
	Nominal duration > 10 minutes.
- List 'B' is an unordered list of 'medium length' videos ('Interstitials')  
	Nominal 2 minutes < duration < 10 minutes.
- List 'C' is an unordered list of 'short' videos ('Ad breaks').  
	Nominal duration < 2 minutes.
- List A2 is list A translated by a random amount.
- List B2 is list B sorted in random order.
- List C2 is list C sorted in random order.
- Iterate **once** through list A2, and repeatedly through lists B2 and C2, appending copies to new list D in the following repeating order:
	> A C B C B C 
- List D is converted to xspf format and saved.

## Scenarios
###Scenario A: 
1. User has three groups of videos (as described in Overview)
2. User uses VLC to create an xspf playlist for each group, saves the xspf files in the working directory
3. User runs shuffle.py, either:
	- Passing in the three xspf files in order (ListA, ListB, ListC) as arguments, or
	- Passing no arguments, and having shuffle.py try to load the three files directly -- will look for ListA.xspf, ListB.xspf, and ListC.xspf
	  (This may change. Also, what about picking files by date suffix?)
4. shuffle.py creates the xspf file representing List D, in the current directory. (named 'tvplaylist.xspf' ?)
5. VLC is started, and passed the new playlist file.
6. Process is repeated from step 3 each time VLC is to be started (daily?)
7. Process is repeated from step 1 each time any of the three initial playlists are modified. 

## Non-Goals
- Graphical UI.
- ...

## Open issues
...