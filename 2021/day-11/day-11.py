import numpy as np

with open('input', 'r') as f:
	puzzle_input = np.array([[int(c) for c in ln.strip()] for ln in f.readlines()])

def update_grid_and_count_flashes(grid: np.numarray) -> tuple[np.numarray, int]:
    '''
        First increment each octopi in the grid, then each octopi greater than 9 "flashes".
        Each adjacent octopi is incremented by one and can also flash if greater than 9.
        Finally each octopi that flashed is reset to 0
    '''
    grid = grid.copy()
    rows, cols = grid.shape
    flashed_octopi: set[tuple[int, int]] = set()
    def increment_octopi(entire_grid: bool, coords: list[tuple[int, int]] = None) -> None:
        '''
            Either increment the entire grid by one or specific indices
        '''
        if entire_grid:
            for element in grid:
                element += 1
        else:
            for A, B in coords:
                grid[A][B] += 1

    def adjacent_neighbours(r: int, c: int) -> list[tuple[int, int]]:
        #Each adjacent neighbour(Diagonals included)
        return [(R, C) for R, C in [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c+1), (r+1, c+1), (r+1, c), (r+1, c-1), (r, c-1)] if (0 <= R < rows) and (0 <= C < cols)]

    def octopi_that_will_flash() -> list[tuple[int, int]]:
        idxs = np.where(grid > 9)
        return list(zip(idxs[0], idxs[1]))

    increment_octopi(True)
    octopi_to_flash = octopi_that_will_flash()
    while octopi_to_flash:
        A, B = octopi_to_flash.pop()
        flashed_octopi.add((A, B))
        increment_octopi(False, adjacent_neighbours(A, B))
        octopi_to_flash.extend([(A, B) for (A, B) in octopi_that_will_flash() if (A, B) not in flashed_octopi and (A, B) not in octopi_to_flash])

    #Flashed octopi reset to 0
    for a, b in flashed_octopi:
        grid[a][b] = 0

    return grid, len(flashed_octopi)

total_flashes = 0
steps = 0
total_size = puzzle_input.size

while True:
    puzzle_input, flashes = update_grid_and_count_flashes(puzzle_input)
    if steps == 100:
        print(f'Part One: {total_flashes}')
    total_flashes += flashes
    steps += 1
    if np.all(puzzle_input == 0):
        break

print(f'Part Two: {steps}')