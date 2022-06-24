import copy

with open('input', 'r') as f:
	contents = f.readlines()
	data = [int(ln) for ln in contents]

def part_one(instructions: list) -> int:
	instructions = copy.deepcopy(instructions)
	idx = 0
	steps_taken = 0
	while idx < len(instructions):
		prev = idx
		idx += instructions[idx]
		instructions[prev] += 1
		steps_taken += 1
	return steps_taken

print(f'Part One Steps required to reach exit: {part_one(data)}')

def part_two(instructions: list) -> int:
	instructions = copy.deepcopy(instructions)
	idx = 0
	steps_taken = 0
	while idx < len(data):
		prev = idx
		idx += instructions[idx]
		if instructions[prev] >= 3:
			instructions[prev] -= 1
		else:
			instructions[prev] += 1
		steps_taken += 1
	return steps_taken

print(f'Part Two Steps required to reach exit: {part_two(data)}')