with open('input', 'r') as f:
	contents = f.readlines()
	data = [ln.strip() for ln in contents]


def part_one(instructions=data) -> str:
	keypad = [[i for i in range(n, n+3)] for n in range(1, 10, 3)]
	bathroom_code = ''
	Y, X = 1, 1
	for ins in instructions:
		for d in ins:
			if d == 'U':
				Y = max((Y-1), 0)
			elif d == 'D':
				Y = min((Y+1), 2)
			elif d == 'R':
				X = min((X+1), 2)
			elif d == 'L':
				X = max((X-1), 0)
		bathroom_code += str(keypad[Y][X])
	return bathroom_code

print(f'Part One: {part_one()}')

def part_two(instructions=data) -> str:
	keypad = ['00100', '02340', '56789', '0ABC0', '00D00']
	bathroom_code = ''
	Y, X = 2, 0
	for ins in instructions:
		for d in ins:
			try:
				if d == 'U' and keypad[Y-1][X] != '0':
					Y = max((Y-1), 0)
				elif d == 'D' and keypad[Y+1][X] != '0':
					Y = min((Y+1), 5)
				elif d == 'R' and keypad[Y][X+1] != '0':
					X = min((X+1), 5)
				elif d == 'L' and keypad[Y][X-1] != '0':
					X = max((X-1), 0)
			except IndexError:
				pass
		bathroom_code += str(keypad[Y][X])
	return bathroom_code
print(f'Part Two: {part_two()}')