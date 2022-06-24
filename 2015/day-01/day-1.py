import re

with open('input', 'r') as f:
	PUZZLE_INPUT = f.readline()
	
def part_one() -> int:
	up = len(re.findall(r'\(', PUZZLE_INPUT))
	down = len(re.findall(r'\)', PUZZLE_INPUT))
	return up-down

print(f'Santa needs to go to floor {part_one()} (Part One)')

def part_two() -> int:
	changes = {
		'(': 1,
		')': -1,
	}
	current_floor = 0
	for c in range(len(PUZZLE_INPUT)):
		current_floor += changes[PUZZLE_INPUT[c]]
		if current_floor < 0:
			return c+1

print(f'Character {part_two()} causes Santa to enter the basement (Part Two)')