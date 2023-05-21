from collections import deque

with open('input', 'r') as f:
    puzzle_input: list[list[int]] = [[ord(c) for c in ln.strip()] for ln in f.readlines()]
    # convert to dictionary
    puzzle_input_dict: dict = {}
    for r in range(len(puzzle_input)):
        for c in range(len(puzzle_input[0])):
            puzzle_input_dict[(r, c)] = puzzle_input[r][c]

            # The start has elevation of 'a'
            if puzzle_input_dict[(r, c)] == ord('S'):
                start: tuple[int, int] = (r, c)
                puzzle_input_dict[(r, c)] = ord('a')


def solution(start: tuple[int, int], puzzle_input_dict=puzzle_input_dict) -> int:
    rows: int = len(puzzle_input)
    cols: int = len(puzzle_input[0])

    END: int = ord('E')
    start_y, start_x = start

    def valid(y: int, x: int) -> bool:
        '''
            Helper function to determine if a square is a valid neighbour
        '''
        if not (0 <= y < rows) or not (0 <= x < cols) or (y, x) in visited:
            return False
        return True

    '''
        Iterative BFS
    '''
    visited: set[tuple[int, int]] = set()
    shortest_path_length = float('inf')
    q: list[tuple[int, int, int]] = deque()

    q.append((start_y, start_x, 1))

    while q:
        Y, X, length = q.popleft()
        curr_lvl: int = puzzle_input_dict[(Y, X)]

        visited.add((Y, X))

        neighbours = [(r, c) for r, c in [(Y-1, X), (Y, X+1), (Y+1, X), (Y, X-1)] if valid(r, c)]

        # Only proceed if current path length is <= shortest_so_far
        for r, c in neighbours:
            dest_elevation: int = puzzle_input_dict[(r, c)]

            if (curr_lvl == 122 and dest_elevation == END):
                shortest_path_length = min(shortest_path_length, length)

            # Can only climb downwards, or up to 1 level higher
            if curr_lvl+1 >= dest_elevation and dest_elevation != 69:
                q.append((r, c, length+1))
                visited.add((r, c))

    return shortest_path_length

# For Part One the only start position is 'S', for part two it's anything with elevation 'a'
print(f'Part One shortest path: {solution(start, puzzle_input_dict=puzzle_input_dict)}')

part_two_starts: list[tuple[int, int]] = [(y, x) for y, x in puzzle_input_dict if puzzle_input_dict[(y, x)] == ord('a')]
shortest_path_part_two = float('inf')

for start in part_two_starts:
    shortest_path_part_two = min(shortest_path_part_two, solution(start, puzzle_input_dict=puzzle_input_dict))

print(f'Part Two shortest path: {shortest_path_part_two}')