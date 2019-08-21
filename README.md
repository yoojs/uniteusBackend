# uniteus Backend Challenge

## Objective
Write a program that prints out a multiplication table of the first 10 primary numbers. 

The program must run from the command line and print one table to STDOUT. The first row 
and column of the table should have the 10 primes, with each cell containing the product
of the primes for the corresponding row and column.

## Notes
Lot of fun doing this challenge. Some notes on my implementation:

Ran on Python 2.7 because this is what I had, would run on Python 3 else-wise.
Algorithm for finding prime is super basic, just a 6k + 1 implementation, fast enough for the challenge however. 
Complexity for my finding prime function is fairly high could fix using myriad of methods to make faster.
Overall, my code is scalable to a point, where after trying to find a couple thousand prime numbers it would run slow.

my code runs to find 10 primary numbers at:
real	0m0.054s
user	0m0.012s
sys	0m0.013s

## How to run
Open terminal (in MacOSX)
move to folder where files exist
Download Python 2.7
and run "python backendCode.py -i 10"
in terminal

output should be:
	  |	2	  3	  5	  7	  11	13	17	19	23	29
	  _	_	  _	  _	  _	  _	  _ 	_	  _	  _	  _
2	  |	4	  6	  10	14	22	26	34	38	46	58
3	  |	6   9	  15	21	33	39	51	57	69	87
5   |	10	15	25	35	55	65	85	95	115	145
7   |	14	21	35	49	77	91	119	133	161	203
11	|	22	33	55	77	121	143	187	209	253	319
13	|	26	39	65	91	143	169	221	247	299	377
17	|	34	51	85	119	187	221	289	323	391	493
19	|	38	57	95	133	209	247	323	361	437	551
23	|	46	69	115	161	253	299	391	437	529	667
29	|	58	87	145	203	319	377	493	551	667	841
