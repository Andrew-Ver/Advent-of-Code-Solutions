import re
from collections import defaultdict

with open('input', 'r') as f:
	contents = f.readlines()
	data = [ln.strip() for ln in contents]

puzzle_input = 304

def spinlock_pattern(p: int, insertions=2017) -> int:
	lst = [0]
	curr = 0
	n = 1
	for i in range(insertions):
		curr = (curr+1 + p) % len(lst)
		lst.insert(curr+1, n)
		n += 1

	return lst[curr+2]

print(f'Answer for Part One: {spinlock_pattern(puzzle_input)}')


def part_two(p: int, insertions=50000000) -> int:
	length_of_list = 1
	after_zero = []
	curr = 0
	n = 1
	for i in range(insertions):
		curr = (curr+1 + p) % length_of_list
		if curr == 0:
			after_zero.append(n)
		n += 1; length_of_list += 1
	return after_zero[-1]

print(f'Answer for Part Two: {part_two(puzzle_input)}')

