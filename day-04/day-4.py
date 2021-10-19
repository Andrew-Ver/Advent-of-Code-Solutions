import hashlib
import copy

PUZZLE_INPUT = 'iwrupvqb'

def answer() -> tuple[int, int]:
	i = 0
	five_zeroes = 0 
	while True:
		if five_zeroes == 0 and hashlib.md5(str.encode(PUZZLE_INPUT+str(i))).hexdigest().startswith('00000'):
			five_zeroes = copy.deepcopy(i)
		if hashlib.md5(str.encode(PUZZLE_INPUT+str(i))).hexdigest().startswith('000000'):
			return five_zeroes, i
		i += 1

part_one, part_two = answer()
print(f'{part_one} (Part One)')
print(f'{part_two} (Part Two)')