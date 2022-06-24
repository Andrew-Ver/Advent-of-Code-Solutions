with open('input', 'r') as f:
	puzzle_input = [[int(c) for c in ln.strip()] for ln in f.readlines()]

def grid_low_points(heightmap: list[list[int]]) -> list[int, set[tuple[int, int]]]:
    def is_lowest_point(R: int, C: int) -> bool:
        adjacent_squares = [(row, col) for row, col in [(R-1, C), (R+1, C), (R, C-1), (R, C+1)] if (0 <= row < rows) and (0 <= col < cols)]
        for Y, X in adjacent_squares:
            if heightmap[Y][X] <= heightmap[R][C]:
                return False
        return True

    risk_levels_sum = 0
    low_point_positions = set()
    rows = len(heightmap)
    cols = len(heightmap[0])

    for r in range(rows):
        for c in range(cols):
            if is_lowest_point(r, c):
                risk_levels_sum += (1 + heightmap[r][c])
                low_point_positions.add((r, c))
    return risk_levels_sum, low_point_positions

risk_levels_sum, low_point_positions = grid_low_points(puzzle_input)

print(f'Part One: {risk_levels_sum}')

def find_basin_size_DFS(low_point_Y: int, low_point_X: int, grid: list[list[int]]) -> int:
    def valid(y, x, pos_hgt) -> bool:
        '''
            Neighbour must be smaller, not explored and < 9
        '''
        if (y, x) in explored:
            return False
        elif (y, x) in to_explore:
            return False
        elif not (0 <= y < len(grid)):
            return False
        elif not (0 <= x < len(grid[0])):
            return False
        elif grid[y][x] <= pos_hgt or grid[y][x] == 9:
            return False
        return True

    explored = set()
    to_explore = [(low_point_Y, low_point_X)]
    basin_positions = []

    while to_explore:
        Y, X = to_explore.pop()
        explored.add((Y, X))
        basin_positions.append(grid[Y][X])

        valid_neighbours = [(row, col) for row, col in [(Y-1, X), (Y+1, X), (Y, X-1), (Y, X+1)] if valid(row, col, grid[Y][X])]
        to_explore.extend(valid_neighbours)
    
    return len(basin_positions)

basin_sizes = []

for a, b in low_point_positions:
    basin_sizes.append(find_basin_size_BFS(a, b, puzzle_input))

print(sorted(basin_sizes))
