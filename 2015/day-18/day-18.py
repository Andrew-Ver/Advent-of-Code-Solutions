from copy import deepcopy

with open('input', 'r') as f:
	PUZZLE_INPUT = [ln.strip() for ln in f.readlines()]

INITIAL_ON_LIGHTS = {(y, x)  for y in range(len(PUZZLE_INPUT)) for x in range(len(PUZZLE_INPUT[y])) if PUZZLE_INPUT[y][x] == '#' }

def neighbours_that_are_on(on_lights: set, light_y: int, light_x: int) -> int:
	#neighbour lights which intersect with lights already on
	return len(on_lights.intersection({(light_y-1, light_x), (light_y, light_x+1), (light_y+1, light_x), (light_y, light_x-1), (light_y-1, light_x+1), (light_y+1, light_x+1), (light_y+1, light_x-1), (light_y-1, light_x-1)}))

def update_lights_on(on_lights: set) -> set:
	new_on_lights = set()
	for y, x in {(y, x) for y in range(100) for x in range(100)}:
		if (y, x) in on_lights:
			if neighbours_that_are_on(on_lights, y, x) in {2, 3}:
				new_on_lights.add((y, x))
		else:
			if neighbours_that_are_on(on_lights, y, x) == 3:
				new_on_lights.add((y, x))
	return new_on_lights

lights_set = deepcopy(INITIAL_ON_LIGHTS)

### Part One
for i in range(100):
	lights_set = update_lights_on(lights_set)

print(f'Number of lights on after 100 steps: {len(lights_set)} (Part One)')

### Part Two
lights_set_part_two = deepcopy(INITIAL_ON_LIGHTS)
#four corners must always stay on for part two
four_corners = {(0, 99), (99, 0), (99, 99), (0, 0)}
lights_set_part_two.update(four_corners)

def update_lights_on_part_two(on_lights: set, four_corners=four_corners) -> set:
	new_on_lights = set()
	new_on_lights.update(four_corners)
	#The lights in the 4 corners must always stay on for Part Two
	for y, x in {(y, x) for y in range(0, 100) for x in range(0, 100) if (y, x) not in four_corners}:
		if (y, x) in on_lights:
			if neighbours_that_are_on(on_lights, y, x) in [2, 3]:
				new_on_lights.add((y, x))
		else:
			if neighbours_that_are_on(on_lights, y, x) == 3:
				new_on_lights.add((y, x))
	return new_on_lights

for i in range(100):
	lights_set_part_two = update_lights_on_part_two(lights_set_part_two)

print(f'Number of lights on after 100 steps (with four corners always on): {len(lights_set_part_two)} (Part Two)')