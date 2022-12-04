import collections
import itertools
import re

with open('input', 'r') as f:
    puzzle_input = [re.search(r'\w+', ln).group() for ln in f.readlines()]
priority_sum = 0
part_b = 0

for w in range(0, len(puzzle_input), 3):
    A, B, C = puzzle_input[w:w+3]

    common = set(A).intersection(B, C)
    c = ord(list(common)[0])

    if c >= 96:
        part_b += c-96
    else:
        part_b += c-64+26

    '''
    for c in B:
        if c in A:
            if c == c.lower():
                priority_sum += ord(c)-96
                print(f'lowercase: {ord(c)} {c}')
                break
            elif c == c.upper():
                priority_sum += ord(c)-64+26
                print(f'uppercase: {c} -  {ord(c)}')
                break

    '''

print(priority_sum)
print(part_b)