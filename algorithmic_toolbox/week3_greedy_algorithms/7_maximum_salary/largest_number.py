#Uses python3
"""For two numbers X and Y, the comparator compares XY with YX and 
the greater number will come first in sorted order.
For example: X = 15, Y = 4, XY = 154 and YX = 415. Y > X then."""

import sys

def largest_number(a):
	extended = []
	result = []
	n = len(max(a)) + 1

	for i in a:
		aux_var = str(i) * n
		extended.append((aux_var[:n:], i))
	
	extended.sort(reverse=True)

	for i in extended:
		result.append(i[1])


	res = ""
	for x in result:
	    res += x
	return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
