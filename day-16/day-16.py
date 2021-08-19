import re
from collections import defaultdict
from copy import deepcopy

with open('input', 'r') as f:
	contents = f.readlines()
	data = [ln.strip() for ln in contents]

INITIAL_STATE = list(map(int, list('11110010111001001')))
REQUIRED_LENGTH = 35651584 # For Part one, Part two requires length 35651584

def dragon_curve(initial_data: list) -> list:
	a = initial_data
	b = [1 if c == 0 else 0 for c in a[::-1]]
	return a + [0] + b

data = INITIAL_STATE 
while len(data) < REQUIRED_LENGTH:
	data = dragon_curve(data)
data = data[:REQUIRED_LENGTH]

def curve_checksum(dragon_curve_data: list) -> int: 
	checksum = []
	for i in range(0, len(dragon_curve_data), 2):
			if dragon_curve_data[i] == dragon_curve_data[i+1]:
				checksum.append(1)
			else:
				checksum.append(0)
	return checksum

while len(data) % 2 == 0:
	data = curve_checksum(data)

print(''.join([str(s) for s in data]))
