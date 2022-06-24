import re
from collections import defaultdict

with open('input', 'r') as f:
	contents = f.readlines()
	data = [ln.strip() for ln in contents]

discs = defaultdict(dict)

for ln in data:
	num, positions, initial_time, starting_pos = re.findall(r'(Disc #\d+|\d+)', ln)
	discs[num]['positions'] = int(positions); discs[num]['starting_pos'] = int(starting_pos); discs[num]['rank'] = int(num[-1])

def solution(discs=discs) -> int:
	# (disc_order_number + time_waited + start_position) % total_positions will give the disc's position
	# after waiting a certain amount of time
	time = 0 
	disc_list = [sum([discs[d]['rank'], discs[d]['starting_pos'], time]) % discs[d]['positions'] for d in discs]
	while not all([d == 0 for d in disc_list]):
		time += 1
		disc_list = [(discs[d]['rank']+discs[d]['starting_pos']+time) % discs[d]['positions'] for d in discs]
	return time

print(f'The minimum amount of time required is: {solution()} (Part One)')

#Part Two simply requires adding a new disc with 11 positions, starting at pos 0 and one second underneath the previous one.
discs['Disc #7']['positions'] = 11; discs['Disc #7']['rank'] = 7
discs['Disc #7']['starting_pos'] = 0

print(f'The minimum time required for part two: {solution()} (part Two)')