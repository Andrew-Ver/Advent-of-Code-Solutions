from functools import reduce

with open('input', 'r') as f:
    puzzle_input: list[list[int]] = [[int(n) for n in ln if n!='\n'] for ln in f.readlines()]

def part_one(puzzle_input=puzzle_input) -> int:
    ans: int = 0
    ROWS: int = len(puzzle_input)
    COLS: int = len(puzzle_input[0])

    for row in range(ROWS):
        for col in range(COLS):
            curr_tree_hgt: tuple[int] = puzzle_input[row][col]
            # if edge tree, visible
            if (row == 0 or col == 0 or row == ROWS-1 or col == COLS-1):
                ans += 1
            else:
                '''
                    Set of tuple (r, c, Direction) to set
                '''
                tallest_tree_west =  max((puzzle_input[row][:col]))
                tallest_tree_north = max((puzzle_input[r][col] for r in range(0, row)))
                tallest_tree_east =  max((puzzle_input[row][col+1:]))
                tallest_tree_south = max((puzzle_input[r][col] for r in range(row+1, ROWS)))

                if any((curr_tree_hgt > t for t in [tallest_tree_west, tallest_tree_north, tallest_tree_east, tallest_tree_south])):
                    ans += 1
    return ans

def part_two(puzzle_input=puzzle_input) -> int:
    '''
        Bruteforce... 🤷🤷
    '''
    best_scenic_score: int = 0

    ROWS: int = len(puzzle_input)
    COLS: int = len(puzzle_input[0])

    tree_dict: dict[tuple[int, int]] = {(y, x): puzzle_input[y][x] for x in range(COLS) for y in range(ROWS)}

    def find_score_in_direction(v: int, trees: list[tuple[int, int]], tree_dict=tree_dict) -> int:
        scenic_score: int = 0

        for y, x in trees:
            scenic_score += 1
            if tree_dict[(y, x)] >= v:
                break
        return scenic_score

    for r in range(1, ROWS-1):
        for c in range(1, COLS-1):

            north: list[tuple[int, int]] = [(y, c) for y in range(r-1, -1, -1)]
            east: list[tuple[int, int]]  = [(r, x) for x in range(c+1, COLS)]
            south: list[tuple[int, int]] = [(y, c) for y in range(r+1, ROWS)]
            west: list[tuple[int, int]]  = [(r, x) for x in range(c-1, -1, -1)]

            scenic_score: int = reduce(lambda a, b: (a*b), [find_score_in_direction(tree_dict[(r, c)], s) for s in [north, east, south, west]])
            best_scenic_score = max(scenic_score, best_scenic_score)

    return best_scenic_score

print(f'Part One: {part_one()} trees visible.')
print(f'Part two: {part_two()} best scenic score.')