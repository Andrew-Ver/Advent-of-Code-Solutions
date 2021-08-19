import re
import hashlib

PUZZLE_INPUT = 'abbhdwsy'

def part_one(PUZZLE_INPUT=PUZZLE_INPUT) -> str:
	password = ''
	n = 0 
	while len(password) != len(PUZZLE_INPUT):
		h = hashlib.md5((PUZZLE_INPUT + str(n)).encode()).hexdigest()
		if h.startswith('00000'):
			password += str(h)[5]
		n += 1
	return password

print(f'Password for Part One: {part_one()}')

def part_two(PUZZLE_INPUT=PUZZLE_INPUT) -> str:
	password = ['' for i in range(8)]
	n = 0 
	while not all(password):
		h = hashlib.md5((PUZZLE_INPUT + str(n)).encode()).hexdigest()
		if h.startswith('00000') and h[5].isnumeric() and 0 <= int(h[5]) <= 7:
			if not password[int(h[5])]:
				password[int(h[5])] = str(h)[6]
		n += 1
	return ''.join(password)

print(f'Password for Part Two: {part_two()}')