import re
from itertools import permutations

with open('input', 'r') as f:
	puzzle_input = [[re.findall(r'\w+', ln.split('|')[0]), re.findall(r'\w+', ln.split('|')[1])] for ln in f.readlines()]

unique_segments = {2: 1, 4: 4, 3: 7, 7: 8}

part_one_count = 0

for ln in puzzle_input:
	for output_value in ln[1]:
		length = len(output_value)
		if length in unique_segments:
			part_one_count += 1

print(f'Part One: {part_one_count}')

'''
	PART TWO 
'''

def find_valid_permutation(line: list[str]) -> dict:
	def check_permutations(segment_displays_permutation: dict, ln: list[str]) -> bool:
		'''
			Check if the permutation of letter mappings is valid
		'''
		segment_validated = set()
		for word in ln:
			for segment in [segment_display for segment_display in  segment_displays_permutation if segment_display not in segment_validated]:
				if len(segment.difference(word)) == 0 and len(set(word).difference(segment)) == 0:
					segment_validated.add(segment)
					break	
		return len(segment_validated) == 10

	chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
	for p in set(permutations(chars, 7)):
		segment_displays = {
							'abcefg': '0',
							'cf': '1',
							'acdeg': '2',
							'acdfg': '3',
							'bcdf': '4',
							'abdfg': '5',
							'abdefg': '6',
							'acf': '7',
							'abcdefg': '8',
							'abcdfg': '9',
							}
		mappings = {}
		for i, char in enumerate(p):
			mappings[chars[i]] = char
		
		segment_displays = {frozenset([mappings[c] for c in k]):v for k, v in segment_displays.items()}
		if check_permutations(segment_displays, line):
			break
	return {''.join(sorted(k)): v for k, v in segment_displays.items()}

part_two_output_total = 0

for line in puzzle_input:
	mapping = find_valid_permutation(line[0])
	part_two_output_total += int(''.join([mapping[''.join(sorted(val))] for val in line[1]]))

print(f'Part Two: {part_two_output_total}')