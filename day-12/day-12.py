import re
from collections import defaultdict

with open('input', 'r') as f:
	contents = f.readlines()
	data = [ln.strip() for ln in contents]

pipe_communication = defaultdict(list)

for ln in data:
	matches = re.findall(r'\d+', ln)
	pipe_communication[matches[0]] = matches[1:]

def part_one(pipe_connections: list, origin_pipe: str, alrdy_checked=set()) -> bool:	
	if '0' in pipe_connections+[origin_pipe] or contains_zero.intersection(pipe_connections):
		contains_zero.add(origin_pipe)
		contains_zero.update(pipe_connections)
		return True
	else:
		for c in [pipe for pipe in pipe_connections if pipe not in alrdy_checked]:
			alrdy_checked.add(c)
			connected.extend(pipe_communication[c])
			if part_one(pipe_communication[c], c, alrdy_checked):
				contains_zero.add(origin_pipe)
				contains_zero.update(pipe_connections)
				return True
	return False

def part_two(pipe_connections: list, origin_pipe: str, alrdy_checked=set()) -> set:	
	all_connections = set(pipe_connections+[origin_pipe])
	if not all_connections.difference(alrdy_checked):
		return all_connections
	else:
		for p in [pipe for pipe in pipe_connections if pipe not in alrdy_checked]:
			alrdy_checked.update([origin_pipe]+pipe_connections)
			connected_part_two.extend(pipe_communication[p])
			all_connections.update(part_two(pipe_communication[p], p, alrdy_checked))
	return all_connections

contains_zero = set()

pipes_related_to_zero = 0
for i in pipe_communication.keys():
	connected = [] 
	if part_one(pipe_communication[i], i):
		contains_zero.update(connected)
		pipes_related_to_zero += 1

print(f'Total programs connected to program ID 0: {pipes_related_to_zero} (Part One)')

#Part Two
connected_part_two = []
pipe_groups = {p: frozenset(part_two(pipe_communication[p], p)) for p in pipe_communication.keys()}
unique_groups = set()

group_count = 0 

for pipe in pipe_groups.keys():
	connected_part_two = []
	if unique_groups.intersection(pipe_groups[pipe]):
		unique_groups.update(pipe_groups[pipe])
	else:
		group_count += 1
		unique_groups.update(pipe_groups[pipe])

print(f'The total number of groups is {group_count} (Part Two)')