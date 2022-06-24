import re
from collections import defaultdict
import copy

with open('input', 'r') as f:
	contents = f.readlines()
	data = [ln.strip().split(':') for ln in contents]

firewall_layers = {int(d[0].strip()): {'current': 1, 'range': int(d[1].strip()), 'reverse': False} for d in data}

#Naive Approach Simulating the States
def new_firewall_state(layers: dict, runs=1) -> dict:
	new_scanner_positions = copy.deepcopy(layers)
	for i in range(runs):
		for scanner_pos in new_scanner_positions.keys():
			if new_scanner_positions[scanner_pos]['reverse'] == False:
				new_scanner_positions[scanner_pos]['current'] += 1
			else:
				new_scanner_positions[scanner_pos]['current'] -= 1
			if new_scanner_positions[scanner_pos]['current'] == 1 and new_scanner_positions[scanner_pos]['reverse'] == True:
				new_scanner_positions[scanner_pos]['reverse'] = False
			elif new_scanner_positions[scanner_pos]['current'] == new_scanner_positions[scanner_pos]['range'] and new_scanner_positions[scanner_pos]['reverse'] == False:
				new_scanner_positions[scanner_pos]['reverse'] = True
	return new_scanner_positions

def move_through_firewall(layers: dict) -> dict:
	l = copy.deepcopy(layers)
	trip_severity = 0
	caught = False
	for i in range(max(l.keys())+1):
		if i in l.keys() and l[i]['current'] == 1:
			trip_severity += (i*l[i]['range'])
			caught = True
		l = new_firewall_state(l)
	return {'trip_severity': trip_severity, 'caught': caught}

#
def part_one(layers: dict, delay=0) -> dict:
	severity = 0
	caught = False 
	for layer in layers.keys():
		if (layer+delay) % ((layers[layer]['range']*2)-2) == 0:
			severity += layer*layers[layer]['range']
			caught = True
	return {'severity': severity, 'caught': caught}

print(f'Trip Severity: {part_one(firewall_layers)["severity"]} (Part One)')

#Bruteforce solution for Part Two
def part_two(layers: dict) -> int:
	delay = 1
	while True:
		if part_one(layers, delay)['caught']:
			delay += 1
		else:
			return delay

print(f'You can pass through the firewall successfully with a minimum delay of {part_two(firewall_layers)} (Part Two)')
