import re

with open('input', 'r') as f:
	PUZZLE_INPUT = f.readline()

def part_one() -> int:
	position = {'X': 0, 'Y': 0}
	visited = set()
	for ch in PUZZLE_INPUT:
		visited.add((position['X'], position['Y']))
		if ch == '^':
			position['Y'] += 1
		elif ch == 'v':
			position['Y'] -= 1
		elif ch == '<':
			position['X'] -= 1
		elif ch == '>':
			position['X'] += 1
	return len(visited)

print(f'Santa visited at least {part_one()} houses at least once (Part One)')

def part_two() -> int:
	santa_pos = {'X': 0, 'Y': 0}
	robo_santa_pos = {'X': 0, 'Y': 0}
	visited = set()
	for c in range(0, len(PUZZLE_INPUT), 2):
		visited.add((santa_pos['X'], santa_pos['Y']))
		visited.add((robo_santa_pos['X'], robo_santa_pos['Y']))
		if PUZZLE_INPUT[c] == '^':
			santa_pos['Y'] += 1
		elif PUZZLE_INPUT[c] == 'v':
			santa_pos['Y'] -= 1
		elif PUZZLE_INPUT[c] == '<':
			santa_pos['X'] -= 1
		elif PUZZLE_INPUT[c] == '>':
			santa_pos['X'] += 1
		if PUZZLE_INPUT[c+1] == '^':
			robo_santa_pos['Y'] += 1
		elif PUZZLE_INPUT[c+1] == 'v':
			robo_santa_pos['Y'] -= 1
		elif PUZZLE_INPUT[c+1] == '<':
			robo_santa_pos['X'] -= 1
		elif PUZZLE_INPUT[c+1] == '>':
			robo_santa_pos['X'] += 1
	return len(visited)

print(f'Santa and Robot Santa visited at least {part_two()} houses at least once (Part Two)')
