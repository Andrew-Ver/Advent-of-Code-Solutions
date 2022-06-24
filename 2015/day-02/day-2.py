import re
from collections import defaultdict
import math

with open('input', 'r') as f:
	contents = f.readlines()
	PUZZLE_INPUT = [[int(n) for n in (re.findall(r'\d+', ln))] for ln in contents]

def solution() -> tuple[int, int]:
	total_wrapping_paper = 0 
	total_ribbon = 0
	for present in PUZZLE_INPUT:
		l, w, h = present
		sides = [l*w, w*h, h*l]
		total_wrapping_paper += sum([2*side for side in sides]) + min(sides)
		sorted_dims = sorted([l, w, h])
		total_ribbon += math.prod([l, w, h]) + sum(sorted_dims[:2])*2
	return total_wrapping_paper, total_ribbon

part_one, part_two = solution()
print(f'The Elves need {part_one} sq ft of Wrapping Paper (Part One)')
print(f'The Elves need {part_two} sq ft of Ribbon (Part Two)')


