import json
import re

with open('input', 'r') as f:
	PUZZLE_INPUT = f.readline()

part_one = sum(list(map(int, re.findall(r"-?\d+", PUZZLE_INPUT))))
print(f'{part_one} is the sum of all numbers in the document (Part One)')

def part_two(obj): 
	if isinstance(obj, int):
		return obj
	elif isinstance(obj, list):
		return sum(part_two(n) for n in obj)
	elif isinstance(obj, dict):
		if 'red' in obj.values():
			return 0
		else:
			return (sum(part_two(o) for o in obj.values()))
	return 0
	
print(f'{part_two(json.loads(PUZZLE_INPUT))} (Part Two)')