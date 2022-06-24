import re
from collections import defaultdict

with open('input', 'r') as f:
	contents = f.readlines()
	data = [ln.strip() for ln in contents]

registers = defaultdict(int)
max_held_part_two = set()

for ln in data:
	instruction, condition = ln.split(' if ')
	r, instruct, v = re.findall(r'([a-z]{1,}|\(inc|dec\)|-?\d{1,})', instruction)
	register_to_check, condition_comp, value = re.findall(r'([a-z]{1,}|\(|>=|<=|!=|<|>|==|\)|-?\d{1,})', condition)
	if condition_comp == '>':
		if registers[register_to_check] > int(value)   and instruct == 'inc':
			registers[r] += int(v)
		elif registers[register_to_check] > int(value) and instruct == 'dec':
			registers[r] -= int(v)
	elif condition_comp == '<':
		if registers[register_to_check] < int(value)   and instruct == 'inc':
			registers[r] += int(v)
		elif registers[register_to_check] < int(value) and instruct == 'dec':
			registers[r] -= int(v)
	elif condition_comp == '!=':
		if registers[register_to_check] != int(value)   and instruct == 'inc':
			registers[r] += int(v)
		elif registers[register_to_check] != int(value) and instruct == 'dec':
			registers[r] -= int(v)
	elif condition_comp == '<=':
		if registers[register_to_check] <= int(value)   and instruct == 'inc':
			registers[r] += int(v)
		elif registers[register_to_check] <= int(value) and instruct == 'dec':
			registers[r] -= int(v)
	elif condition_comp == '>=':
		if registers[register_to_check] >= int(value)   and instruct == 'inc':
			registers[r] += int(v)
		elif registers[register_to_check] >= int(value) and instruct == 'dec':
			registers[r] -= int(v)
	elif condition_comp == '==':
		if registers[register_to_check] == int(value)   and instruct == 'inc':
			registers[r] += int(v)
		elif registers[register_to_check] == int(value) and instruct == 'dec':
			registers[r] -= int(v)
	max_held_part_two.add(max(registers.values()))

print(f'Largest Value held in any register: {max(registers.values())} (Part One)')
print(f'Largest Value held in any register throughout the process: {max(max_held_part_two)} (Part Two)')