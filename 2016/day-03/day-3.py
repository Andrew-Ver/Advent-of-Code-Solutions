import re

with open('input', 'r') as f:
	contents = f.readlines()
	data = [list(map(int, re.findall(r'\d+', ln))) for ln in contents]

def part_one(lst=data) -> int:
	valid = 0
	for ln in lst:
		a, b, c = ln
		if a + b > c and b + c > a and a + c > b:
			valid += 1
	return valid
print(f'Part One: {part_one()}')

def part_two(lst=data) -> int:
	valid = 0
	for ln in range(0, len(lst), 3):
		triangle_one = [lst[ln][0], lst[ln+1][0], lst[ln+2][0]]
		triangle_two = [lst[ln][1], lst[ln+1][1], lst[ln+2][1]]
		triangle_three = [lst[ln][2], lst[ln+1][2], lst[ln+2][2]]
		for tri in [triangle_one, triangle_two, triangle_three]:
			a, b, c = tri
			if a + b > c and b + c > a and a + c > b:
				valid += 1
	return valid

print(f'Part Two: {part_two()}')