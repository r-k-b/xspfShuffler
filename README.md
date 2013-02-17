# xspfShuffler
Designed to take in 3 playlists, and output one playlist consisting of 
the 3 input playlists joined in a certain order.

Mostly for the purpose of creating a 'TV-like' experience from a 
collection of long, medium, and short videos. (i.e., 'Programmes', 
'ad breaks', and 'interstitials'). 

Designed specifically for VLC Media Player[1] and the .xspf[2] playlist file.

[1]: http://videolan.org
[2]: http://xspf.org/

## Author
rtzarius@gmail.com

## Licence
Note to Self: research and decide on a licence.

## Basic theory
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
