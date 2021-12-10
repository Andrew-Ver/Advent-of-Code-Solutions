from collections import defaultdict

with open('input', 'r') as f:
	puzzle_input = [ln.strip() for ln in f.readlines()]

def check_brackets(s: str) -> str:
    stack = []
    bracket_pairs = {')': '(',
                     '}': '{',
                     ']': '[',
                     '>': '<',  
                    }
    for c in s:
        if c in bracket_pairs and stack[-1] != bracket_pairs[c]:
            return c
        elif c in bracket_pairs and stack[-1] == bracket_pairs[c]:
            stack.pop()
        else:
            stack.append(c)
    return stack

error_count = defaultdict(int)
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
incomplete_lines = set()

for ln in puzzle_input:
    bracket = check_brackets(ln)
    if len(bracket) == 1 and bracket[0] in {')', '}',']', '>'}:
        error_count[bracket] += 1
    else:
        incomplete_lines.add(''.join(bracket))

part_one_total = 0

for error, count in error_count.items():
    part_one_total += (scores[error] * count)

print(f'Part One: {part_one_total}')

def calculate_completion_score(unclosed_brackets: str) -> int:
    score = 0
    points = {'(': 1, '[': 2, '{': 3, '<': 4}
    for bracket in unclosed_brackets[::-1]:
        score *= 5
        score += points[bracket]
    return score

bracket_completion_scores = sorted([calculate_completion_score(ln) for ln in incomplete_lines])

print(f'Part Two: {bracket_completion_scores[(len(bracket_completion_scores)-1)//2]}')