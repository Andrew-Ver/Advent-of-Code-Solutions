import re
from collections import defaultdict

with open('input', 'r') as f:
	PUZZLE_INPUT = [ln.strip() for ln in f.readlines()]

def part_one() -> int:
	lights_on = set()
	for ln in PUZZLE_INPUT:
		command = re.search(r'(on|off|toggle)', ln).group()
		x_one, y_one, x_two, y_two = list(map(int, re.findall(r'\d+', ln)))
		lights_to_modify = {(x, y) for x in range(x_one, x_two+1) for y in range(y_one, y_two+1)}
		if command == 'on':
			lights_on.update(lights_to_modify)
		elif command == 'off':
			lights_on.difference_update(lights_to_modify)
		elif command == 'toggle':
			lights_to_turn_on = lights_to_modify.difference(lights_on)
			lights_on.difference_update(lights_to_modify)
			lights_on.update(lights_to_turn_on)
	return len(lights_on)

print(f'{part_one()} lights are left on (Part One)')

def part_two() -> int:
	'''
		turn on  => increase brightness by 1
		turn off => decrease brightness by 1
		toggle   => increase brightness by 2
	'''
	lights = defaultdict(int)

	for ln in PUZZLE_INPUT:
		command = re.search(r'(on|off|toggle)', ln).group()
		x_one, y_one, x_two, y_two = list(map(int, re.findall(r'\d+', ln)))
		lights_to_modify = {(x, y) for x in range(x_one, x_two+1) for y in range(y_one, y_two+1)}
		
		if command == 'on':
			for light in lights_to_modify:
				lights[light] += 1
		elif command == 'off':
			for light in lights_to_modify:
				if lights[light]:
					lights[light] -= 1
		elif command == 'toggle':
			for light in lights_to_modify:
				lights[light] += 2
	return sum(list(lights.values()))

print(f'Total Brightness of all lights: {part_two()} (Part Two)')

