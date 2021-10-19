import re

with open('input', 'r') as f:
	PUZZLE_INPUT = [ln.strip() for ln in f.readlines()]

def part_one() -> int:
	total_characters = 0
	string_value_characters = 0
	for string in PUZZLE_INPUT:
		total_characters += len(string)
		#Count each regular str value, '\x[ch][ch]' and '\' escaped char as 1
		string_value_characters += len(re.findall(r'(\w|\\x..|\\.)', string))
	return (total_characters - string_value_characters)

print(f'{part_one()} (Part One)')

def part_two() -> int:
	total_characters = 0
	coded_string_characters = 0
	for string in PUZZLE_INPUT:
		total_characters += len(string)
		# add 2 for the inherent quotation marks on each string
		# add 1 for each \ and " in string
		quotation_marks = len(re.findall(r'"', string))
		backslashes = len(re.findall(r'\\', string))
		coded_string_characters += (2+len(string) + quotation_marks + backslashes)
	return coded_string_characters - total_characters

print(f'{part_two()} (Part Two)')