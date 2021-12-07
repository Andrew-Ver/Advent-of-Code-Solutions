import re

with open('input', 'r') as f:
	puzzle_input = [int(n) for n in re.findall(r'\d+', f.readline())]

lowest_so_far = float('inf')
total = 0

for n in set(puzzle_input):
    for number in puzzle_input:
        total += abs(n - number)
        if total > lowest_so_far:
            break
    lowest_so_far = min(lowest_so_far, total)
    total = 0

print(f'Part One: {lowest_so_far}')

def trianglular_number(n):
    return n * (n+1) // 2

lowest_so_far = float('inf')
total = 0

for n in set(puzzle_input):
    for number in puzzle_input:
        total += trianglular_number(abs(n - number))
        if total > lowest_so_far:
            break
    lowest_so_far = min(lowest_so_far, total)
    total = 0

print(f'Part Two: {lowest_so_far}')