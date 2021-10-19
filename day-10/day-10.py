import re

PUZZLE_INPUT = '1113222113'

def solution(repeat: int) -> int:
	new_sequence = [PUZZLE_INPUT]
	for i in range(repeat):
		digit_counts = re.finditer(r'(\d)\1*', ''.join(new_sequence))
		new_sequence.clear()
		for occurance in digit_counts:
			#For each digit the new sequence is [occurances of digit][digit]
			new_sequence.extend([str(len(occurance.group())), occurance.group()[0]])
	return len(new_sequence)

print(f'The length of the result is {solution(repeat=40)} after 40 runs (Part One)')
print(f'The length of the result is {solution(repeat=50)} after 50 runs (Part Two)')