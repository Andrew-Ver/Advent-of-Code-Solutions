from copy import deepcopy

with open('input', 'r') as f:
	contents = f.readlines()
	grid = [ln.strip() for ln in contents]

#We only need to keep track of initial "infected" nodes per the input, as this is an infinite grid
infected = {(r, p) for r in range(len(grid)) for p in range(len(grid[r])) if grid[r][p] == '#'}
infected_two = deepcopy(infected)

def advance_one_step(current_direction: str, turn: str, curr_Y: int, curr_X: int, state=None) -> list:
	'''
	current_direction (str): direction the virus is facing on grid
	turn (str): direction to turn per the rules
	curr_Y (int): current Y coord
	curr_X (int): current X coord
	state optional (str): for Part Two "weakened"/"flagged"
	returns new Y, X and direction
	'''
	new_direction = current_direction
	if state == 'weakened':
		if current_direction == 'N':
			curr_Y -= 1
		elif current_direction == 'E':
			curr_X += 1
		elif current_direction == 'S':
			curr_Y += 1
		elif current_direction == 'W':
			curr_X -= 1
	elif state == 'flagged':
		if current_direction == 'N':
			curr_Y += 1; new_direction = 'S'
		elif current_direction == 'E':
			curr_X -= 1; new_direction = 'W'
		elif current_direction == 'S':
			curr_Y -= 1; new_direction = 'N'
		elif current_direction == 'W':
			curr_X += 1; new_direction = 'E'
	else:	
		if current_direction == 'N':
			if turn == 'R':
				curr_X += 1; new_direction = 'E' 
			elif turn == 'L':
				curr_X -= 1; new_direction = 'W'
		elif current_direction == 'E':
			if turn == 'R':
				curr_Y += 1; new_direction = 'S'
			elif turn == 'L':
				curr_Y -= 1; new_direction = 'N'
		elif current_direction == 'S':
			if turn == 'R':
				curr_X -= 1; new_direction = 'W'
			elif turn == 'L':
				curr_X += 1; new_direction = 'E'
		elif current_direction == 'W':
			if turn == 'R':
				curr_Y -= 1; new_direction = 'N'
			elif turn == 'L':
				curr_Y += 1; new_direction = 'S'
		
	return (curr_Y, curr_X, new_direction)

def perform_bursts_of_activity(infected_nodes: set, bursts_to_perform=10000) -> int:
	infection_bursts = 0
	facing = 'N'
	#We only need to keep track of nodes that are "unclean"
	Y, X = (len(grid)-1)//2, (len(grid[0])-1)//2
	for _ in range(bursts_to_perform):
		if (Y, X) in infected:
			infected_nodes.remove((Y, X))
			Y, X, facing = advance_one_step(facing, 'R', Y, X)
		else:
			infected_nodes.add((Y, X))
			Y, X, facing = advance_one_step(facing, 'L', Y, X)
			infection_bursts += 1
	return infection_bursts

print(f'Out of 10 000 bursts of activity, {perform_bursts_of_activity(infected)} caused a node to become infected (Part One)')

# Part Two
def part_two_perform_bursts_of_activity(infected_nodes: set, bursts_to_perform=10000000) -> int:
	infection_bursts = 0
	weakened_nodes = set(); flagged_nodes = set()
	facing = 'N'
	Y, X = (len(grid)-1)//2, (len(grid[0])-1)//2
	for _ in range(bursts_to_perform):
		if (Y, X) not in infected_nodes and (Y, X) not in weakened_nodes and (Y, X) not in flagged_nodes:
			weakened_nodes.add((Y, X))
			Y, X, facing = advance_one_step(facing, 'L', Y, X)
		elif (Y, X) in weakened_nodes:
			weakened_nodes.remove((Y, X))
			infected_nodes.add((Y, X))
			Y, X, facing = advance_one_step(facing, None, Y, X, 'weakened')
			infection_bursts += 1
		elif (Y, X) in infected_nodes:
			infected_nodes.remove((Y, X))
			flagged_nodes.add((Y, X))
			Y, X, facing = advance_one_step(facing, 'R', Y, X)
		elif (Y, X) in flagged_nodes:
			flagged_nodes.remove((Y, X))
			Y, X, facing = advance_one_step(facing, None, Y, X, 'flagged')
	return infection_bursts

print(f'\nOut of 10 000 000 bursts of activity with the new rules, {part_two_perform_bursts_of_activity(infected_two)} caused a node to become Infected. (Part Two)')