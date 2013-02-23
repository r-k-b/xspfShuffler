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

## Non-Goals

## Open issues