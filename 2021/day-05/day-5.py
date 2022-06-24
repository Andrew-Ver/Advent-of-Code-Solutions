import re
from collections import Counter

with open('input', 'r') as f:
	puzzle_input = [[int(n) for n in re.findall(r'\d+', ln.strip())] for ln in f.readlines()]

#Part One
diagram_counts = Counter()

for ln in puzzle_input:
    X1, Y1, X2, Y2 = ln
    if X1 == X2:
        diagram_counts.update([(X1, i) for i in range(min(Y1, Y2), max(Y1+1, Y2+1))])
    elif Y1 == Y2:
        diagram_counts.update([(i, Y1) for i in range(min(X1, X2), max(X1+1, X2+1))])

print(f'Part One: {len([k for k, v in diagram_counts.items() if v >= 2])}')

#Part Two
diagram_counts = Counter()

for ln in puzzle_input:
    X1, Y1, X2, Y2 = ln
    if X1 == X2:
        diagram_counts.update([(X1, i) for i in range(min(Y1, Y2), max(Y1+1, Y2+1))])
    elif Y1 == Y2:
        diagram_counts.update([(i, Y1) for i in range(min(X1, X2), max(X1+1, X2+1))])
    else:
        if X2 <= X1 and Y2 >= Y1:
            diagram_counts.update([(a, b) for a, b in zip(range(X2, X1+1), range(Y2, Y1-1, -1))])

        elif X2 >= X1 and Y2 >= Y1:
            diagram_counts.update([(a, b) for a, b in zip(range(X1, X2+1), range(Y1, Y2+1))])

        elif X2 >= X1 and Y2 <= Y1:
            diagram_counts.update([(a, b) for a, b in zip(range(X1, X2+1), range(Y1, Y2-1, -1))])

        elif X2 <= X1 and Y2 <= Y1:
            diagram_counts.update([(a, b) for a, b in zip(range(X1, X2-1, -1), range(Y1, Y2-1, -1))])

print(f'Part Two: {len([k for k, v in diagram_counts.items() if v >= 2])}')