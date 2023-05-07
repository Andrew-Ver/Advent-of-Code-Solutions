import re

with open('input', 'r') as f:
    puzzle_input: list[tuple[str, int]] = [(re.search(r'\w', ln).group(), int(re.search(r'\d+', ln).group())) for ln in f.readlines()]

head_X = head_Y = tail_X = tail_Y = 0

visited: set[int] = set()

def difference(x_1: int, y_1: int, x_2: int, y_2: int) -> tuple[int]:
    return (x_1-x_2, y_1-y_2)

head_X, head_Y = (0, 4)
tail_X, tail_Y = (1, 5)

print(difference(head_X, head_Y, tail_X, tail_Y))

for direction, steps in puzzle_input:
    for _ in range(steps):
        if direction == 'U':
            head_Y -= 1
        elif direction == 'D':
            head_Y += 1
        elif direction == 'L':
            head_X -= 1
        elif direction == 'R':
            head_X += 1

        x_diff, y_diff = difference(head_X, head_Y, tail_X, tail_Y)

        # Move up/down/left/right
        if (not x_diff and y_diff == 2):
            tail_Y += 1
        elif (not x_diff and y_diff == -2):
            tail_Y -= 1
        elif (x_diff == 2 and not y_diff):
            tail_X += 1
        elif (x_diff == -2 and not y_diff):
            tail_X -= 1

        # Move diagnonally
        elif (x_diff and y_diff):



            visited.add((tail_X, tail_Y))