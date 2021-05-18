import re
from collections import defaultdict

with open('input', 'r') as f:
	contents = f.readlines()
	data = [ln.strip() for ln in contents if ln != '\n']

def parse_input(instructions: list) -> dict:
	'''
	{'A': {'0': {'write': 1, 'move': 1, 'continue': 'B'} 
		   '1': {'write': 0, 'move': -1, 'continue': 'C'}} 
	'''
	new_instructions = defaultdict(dict)
	first_state = re.search(r'\s[ABCDEF]', instructions[0]).group().strip()
	checksum_after = int(re.search(r'\d+', instructions[1]).group())
	for i in range(len(instructions)):
		if instructions[i].startswith('In state'):
			letter = re.search(r'\s[ABCDEF]', instructions[i]).group().strip()
			new_instructions[letter]['0'] = {}
			new_instructions[letter]['0']['write'], new_instructions[letter]['0']['move'], new_instructions[letter]['0']['continue'] = int(re.search(r'\d', instructions[i+2]).group()), re.search(r'(right|left)', instructions[i+3]).group(), re.search(r'[ABCDEF]\.', instructions[i+4]).group().rstrip('.')
			new_instructions[letter]['1'] = {}
			new_instructions[letter]['1']['write'], new_instructions[letter]['1']['move'], new_instructions[letter]['1']['continue'] = int(re.search(r'\d', instructions[i+6]).group()), re.search(r'(right|left)', instructions[i+7]).group(), re.search(r'[ABCDEF]\.', instructions[i+8]).group().rstrip('.')
	return {'first_state': first_state, 'checksum_after': checksum_after, 'new_instructions': new_instructions}

def run_turing_machine(instructions: dict) -> int:
	runs = 0; cursor = 0; state = instructions['first_state']; checksum_after = instructions['checksum_after']
	instructions = instructions['new_instructions']
	tape = defaultdict(int)
	while runs < checksum_after:
		value = str(tape[cursor])
		#the tape registers can ONLY store 0 or 1
		tape[cursor] = instructions[state][value]['write']
		if instructions[state][value]['move'] == 'right':
			cursor += 1
		else:
			cursor -= 1
		state = instructions[state][value]['continue']
		runs += 1
	return list(tape.values()).count(1)

parsed_instructions = parse_input(data)
print(f'Diagnostic Checksum: {run_turing_machine(parsed_instructions)} (Part One)')