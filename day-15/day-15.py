import re
from queue import PriorityQueue

with open('input', 'r') as f:
    puzzle_input = [[int(n) for n in re.findall(r'\d', ln)] for ln in f.readlines()]

def lowest_total_risk(grid: list[list[int]]) -> int:
    '''
        https://stackabuse.com/dijkstras-algorithm-in-python/
    '''
    node_costs = {(r, c): float('inf') for r in range(len(grid)) for c in range(len(grid[0]))}
    node_costs[(0, 0)] = 0

    end_Y, end_X = len(grid)-1, len(grid[0])-1
    
    seen = set()
    pq = PriorityQueue()
    pq.put((0, (0, 0)))

    while not pq.empty():
        dist, (Y, X) = pq.get()
        seen.add((Y, X))

        for A, B in [(Y, X) for Y, X in [(Y-1, X), (Y+1, X), (Y, X-1), (Y, X+1)] if (0 <= Y <= end_Y) and (0 <= X <= end_X)]:
            if (A, B) not in seen:
                old_cost = node_costs[(A, B)]
                new_cost = node_costs[(Y, X)] + grid[A][B]
                if new_cost < old_cost:
                    pq.put((new_cost, (A, B)))
                    node_costs[(A, B)] = new_cost
    
    return node_costs[(end_Y, end_X)]

print(f'Part One: {lowest_total_risk(puzzle_input)}')

def part_two_grid(grid: list[list[int]]) -> list[list[int]]:
    '''
        Extend the grid to 5x in width and length
    '''
    new_grid = grid.copy()
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for a in range(1, 5):
            new_row = [new_grid[i][(j-cols)]+1 if (new_grid[i][(j-cols)]+1) <= 9 else 1  for j in range(a*cols, (a*cols+cols))]
            new_grid[i] = new_grid[i] + new_row
    
    for i in range(rows, rows*5):
        new_grid.append([new_grid[i-rows][j]+1 if (new_grid[i-rows][j]+1) <= 9 else 1 for j in range(len(new_grid[-1]))])

    return new_grid

extended_grid = part_two_grid(puzzle_input)

print(f'Part Two: {lowest_total_risk(extended_grid)}')