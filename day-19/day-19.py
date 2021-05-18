with open('input', 'r') as f:
	contents = f.readlines()
	data = [ln.rstrip('\n') for ln in contents]

def determine_new_direction(grid: list, curr_direction: str, row: int, pos: int) -> str:
	if curr_direction == 'N' or curr_direction == 'S':
		try:
			if grid[row][pos-1] == '-' or grid[row][pos-1].isalpha():
				return 'W'
			elif grid[row][pos+1] == '-' or grid[row][pos+1].isalpha():
				return 'E'
		except IndexError:
			pass
	elif curr_direction == 'W'or curr_direction == 'E':
		try:
			if grid[row-1][pos] == '|' or grid[row-1][pos].isalpha():
				return 'N'
			elif grid[row+1][pos] == '|' or grid[row+1][pos].isalpha():
				return 'S'
		except IndexError:
			pass

def traverse_path(g: list) -> list:
	step_count = 0
	letters_visited = []
	at_end = False
	row = 0; pos = g[0].index('|') 
	direction = 'S'
	all_letters_on_path = {g[r][p] for p in range(len(g[0])) for r in range(len(g)) if g[r][p].isalpha()} # End of Path
	while len(letters_visited) != len(all_letters_on_path):
		if direction == 'S':
			row += 1; step_count += 1
		elif direction == 'N':
			row -= 1; step_count += 1
		elif direction == 'W':
			pos -= 1; step_count += 1
		elif direction == 'E':
			pos += 1; step_count += 1
		if g[row][pos] == '+':
			direction = determine_new_direction(g, direction, row, pos)
		if g[row][pos].isalpha():
			letters_visited.append(g[row][pos])
	return letters_visited, step_count+1

part_one, part_two = traverse_path(data)

print(f'Answer for Part One: {"".join(part_one)}')
print(f'Answer for Part Two: {part_two}')