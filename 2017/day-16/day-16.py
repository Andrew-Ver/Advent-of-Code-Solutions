import re
from copy import deepcopy

with open('input', 'r') as f:
	contents = f.readline()
	data = contents.strip().split(',')

string = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

def dance(dance_moves: list, s: list) -> str:
	new_string = deepcopy(s)
	for mv in dance_moves:
		if mv.startswith('s'):
			n = int(re.search(r'\d+', mv).group())
			new_string = new_string[-n:] + new_string[:-n]
		elif mv.startswith('x'):
			a, b = list(map(int, re.findall(r'\d+', mv)))
			t = new_string[b]
			new_string[b] = new_string[a]
			new_string[a] = t
		elif mv.startswith('p'):
			a, b = re.findall(r'\w', mv[1:])
			pos_a = new_string.index(a)
			pos_b = new_string.index(b)
			new_string[pos_b] = a
			new_string[pos_a] = b
	return new_string

print(f'Answer for Part One: {"".join(dance(data, string))}')

#Part Two
def part_two(d: list, s: list) -> str:
	previous_states = []
	n = 0 #Number of iterations before the pattern repeats
	while True:
		s = dance(data, s)
		if s in previous_states:
			previous_states.append(s)
			break
		previous_states.append(s)
		n += 1
	for i in range(divmod(1000000000, n)[-1]-1):
		s = dance(data, s)
	return s

print(f'Answer for Part Two: {"".join(part_two(data, string))}')