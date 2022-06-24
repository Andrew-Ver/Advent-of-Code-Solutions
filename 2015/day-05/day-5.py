import re

with open('input', 'r') as f:
	PUZZLE_INPUT = [ln.strip() for ln in f.readlines()]

def part_one() -> int:
	vowels = r'[aeiou]'
	two_letters_in_a_row = r'(\w)\1'
	
	return len([True for s in PUZZLE_INPUT if not re.search(r'(ab|cd|pq|xy)', s) and len(re.findall(vowels, s)) >= 3 and re.search(two_letters_in_a_row, s)])
	
print(f'{part_one()} string are nice. (Part One)')

def part_two() -> int:
	two_letters_repeated_without_overlapping = r'(\w\w).*\1'
	repeat_letter_with_character_inbetween = r'(\w).\1'

	return len([True for s in PUZZLE_INPUT if re.search(two_letters_repeated_without_overlapping, s) and re.search(repeat_letter_with_character_inbetween, s)])

print(f'{part_two()} strings are nice. (Part Two)')