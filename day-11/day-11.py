import re
from collections import defaultdict
import copy

with open('input', 'r') as f:
	contents = f.readline()
	data = contents.rstrip('\n').split(',')

def path_final_position(steps: list) -> dict:
	''' https://www.redblobgames.com/grids/hexagons/
		North: R-1, Q. North-East: R-1, Q+1. South-East: Q+1, R. 
		South: R+1, Q. South-West: R+1, Q-1. North-East: R, Q-1 
	'''
	pos = defaultdict(int)
	for step in steps:
		if step == 'n':
			pos['r'] -= 1
		elif step == 'ne':
			pos['r'] -= 1
			pos['q'] += 1
		elif step == 'se':
			pos['q'] += 1
		elif step == 's':
			pos['r'] += 1
		elif step == 'sw':
			pos['r'] += 1
			pos['q'] -= 1
		elif step == 'nw':
			pos['q'] -= 1
	return pos

def minimum_steps_required(needed_coords: dict) -> int:
	''' https://www.redblobgames.com/grids/hexagons/
		North: R-1, Q. North-East: R-1, Q+1. South-East: Q+1, R. 
		South: R+1, Q. South-West: R+1, Q-1. North-East: R, Q-1 
	'''
	return abs(needed_coords['r']) + (abs(needed_coords['q']) - abs(needed_coords['r']))

def position_for_each_step(steps: list) -> list:
	#Furthest the child got from the origin
	lst_of_positions = set()
	pos = {'r': 0, 'q': 0}
	for step in steps:
		if step == 'n':
			pos['r'] -= 1
		elif step == 'ne':
			pos['r'] -= 1
			pos['q'] += 1
		elif step == 'se':
			pos['q'] += 1
		elif step == 's':
			pos['r'] += 1
		elif step == 'sw':
			pos['r'] += 1
			pos['q'] -= 1
		elif step == 'nw':
			pos['q'] -= 1
		lst_of_positions.add(tuple(pos.items()))
	return lst_of_positions

required_coordinates = path_final_position(data)
answer_part_one = minimum_steps_required(required_coordinates)
print(f'Minimum steps required to the destination: {answer_part_one} (Part One)')

#Part Two
furthest_steps_away = max([minimum_steps_required({p[0]: p[1] for p in pos}) for pos in position_for_each_step(data)])
print(f'The most steps away from the starting position: {furthest_steps_away} (Part Two)')