import re
from collections import defaultdict, deque

with open('input', 'r') as f:
	contents = f.readline()
	data = contents.strip()

def calculate_score(string: str) -> int:
	stack = deque()
	group_count = 0 
	score = 0 
	i = 0 
	characters_within_garbage = 0
	while i != len(string):
		if string[i] == '{' and '<' not in stack:
			stack.append('{')
		elif string[i] == '!':
			i += 1
		elif string[i] == '<' and '<' not in stack:
			stack.append('<')
			curr = '<'
		elif string[i] == '>' and string[i-1] != '!' or string[i] == '>' and string[i-2:i] == '!!':
			stack.remove('<')
		elif string[i] == '}' and '<' not in stack:
			score += stack.count('{')
			stack.remove('{')
			group_count += 1
		elif '<' in stack:
			characters_within_garbage += 1
		i += 1
	return score, characters_within_garbage

part_one_answer, part_two_answer = calculate_score(data)
print(f'Total Score for all groups in input: {part_one_answer} (Part One)')
print(f'Total Garbage Characters in input:   {part_two_answer} (Part Two)')