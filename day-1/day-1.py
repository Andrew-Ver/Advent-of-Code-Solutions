with open('input', 'r') as f:
	contents = f.readline()
	data = [int(ln) for ln in contents.rstrip('\n')]

data.append(data[0])

def part_one(ints: list) -> int:
	return sum([ints[i] for i in range(len(ints)-1) if ints[i] == ints[i+1]])

print(f'Part One: {part_one(data)}')

def part_two(ints: list) -> int:
	h = len(ints)//2
	return sum([ints[i] for i in range(len(ints)) if ints[i] == ints[(i+h)%(len(ints)-1)]])

print(f'Part Two: {part_two(data)}')