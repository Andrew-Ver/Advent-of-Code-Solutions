from collections import defaultdict

with open('input', 'r') as f:
    puzzle_input: list[list[int]] = [[int(n) for n in ln if n!='\n'] for ln in f.readlines()]

ROWS: int = len(puzzle_input)
COLS: int = len(puzzle_input[0])

PART_ONE_VISIBLE: int = 0

max_score = float('-inf')

for row in range(ROWS):
    for col in range(COLS):
        curr_tree_hgt: tuple[int] = puzzle_input[row][col]

        # if edge tree, visible
        if (row == 0 or col == 0 or row == ROWS-1 or col == COLS-1):
            PART_ONE_VISIBLE += 1
        else:
            '''
                Set of tuple (r, c, Direction) to set
            '''

            tallest_tree_west =  max((puzzle_input[row][:col]))
            tallest_tree_north = max((puzzle_input[r][col] for r in range(0, row)))
            tallest_tree_east =  max((puzzle_input[row][col+1:]))
            tallest_tree_south = max((puzzle_input[r][col] for r in range(row+1, ROWS)))

            if any((curr_tree_hgt > t for t in [tallest_tree_west, tallest_tree_north, tallest_tree_east, tallest_tree_south])):
                PART_ONE_VISIBLE += 1

print(f'Part One: {PART_ONE_VISIBLE} trees visible.')

print(f'Part two: {"Incomplete..."}')