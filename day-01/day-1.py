import re
from collections import defaultdict

with open('input', 'r') as f:
	contents = f.readline()
	data = contents.split()

def solution(directions=data) -> list:
	Y_POS = 0; X_POS = 0; facing_direction = 0
	visited = set()
	first_location_visited_twice = ()
	for d in directions:
		direction, steps = re.findall(r'([A-Z]|\d+)', d)
		if direction == 'R':
			facing_direction = (facing_direction + 90) % 360
		elif direction == 'L':
			facing_direction = (facing_direction - 90) % 360
		for _ in range(int(steps)):
			if facing_direction == 0:
				Y_POS -= 1
			elif facing_direction == 90:
				X_POS += 1
			elif facing_direction == 180:
				Y_POS += 1
			elif facing_direction == 270:
				X_POS -= 1
			if (Y_POS, X_POS) in visited and not first_location_visited_twice:
				first_location_visited_twice = abs(Y_POS) + abs(X_POS)
			else:
				visited.add((Y_POS, X_POS))
	return (abs(Y_POS) + abs(X_POS)), first_location_visited_twice

print(f'Part One: {solution()[0]} Part Two: {solution()[1]}')
