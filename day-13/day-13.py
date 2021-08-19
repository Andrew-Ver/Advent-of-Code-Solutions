from collections import deque

P_INPUT = 1352

def is_openspace(x: int, y: int, p=P_INPUT) -> bool:
	b_repr = bin((x*x + 3*x + 2*x*y + y + y*y) + p)
	return b_repr.count('1') % 2 == 0

def is_valid(y, x, grid) -> bool:
	return (y >= 0) and (y < 500) and (x >= 0) and (x < 500)

area_grid = [['.' if is_openspace(y, x) else '#' for y in range(500)] for x in range(500)]

target = (39, 31)
curr_pos = (1, 1, 0)
queue = deque()
queue.append(curr_pos)
found = False
visited = set()
visited.add((curr_pos))

while queue:
	Y, X, STEPS = queue.popleft()
	if STEPS == 50:
		print(f'PART TWO: {len(visited)} {STEPS}')
	visited.add((Y, X))
	neighbours = [(y, x, STEPS+1) for (y, x) in [(Y-1, X), (Y, X+1), (Y+1, X), (Y, X-1)] if is_valid(y, x, area_grid)]
	if not len(neighbours):
		print(f'DEAD END')
		break

	if (Y, X) == target:
		print(f'FOUND THE NODE in {STEPS} steps')
		break

	visited.add((Y, X))
	for y, x, STEPS in neighbours:
		try:
			if area_grid[y][x] == '.':
				if (y, x) not in visited:
					queue.append((y, x, STEPS))
		except IndexError:
			pass
	