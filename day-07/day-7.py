import re
from collections import defaultdict

with open('input', 'r') as f:
	contents = f.readlines()
	data = [ln.strip() for ln in contents]

tower_structure = defaultdict(dict)
#parsing
for i in data:
	pillars = re.findall(r'[a-z]{4,}', i)
	wgt = re.search(r'[0-9]{1,}', i)
	if len(pillars) == 1:
		tower_structure[pillars[0]]['weight'] = int(wgt.group())
		tower_structure[pillars[0]]['subtowers'] = []
	else:
		tower_structure[pillars[0]]['subtowers'] = pillars[1:]
		tower_structure[pillars[0]]['weight'] = int(wgt.group())
		
all_subtowers = set()
for t in [twr for twr in tower_structure.keys() if len(tower_structure[twr]['subtowers'])>0]:
	all_subtowers.update(tuple(tower_structure[t]['subtowers']))

part_one_answer = ''.join(set(tower_structure.keys()).difference(all_subtowers))
print(f'Name of bottom program: {part_one_answer} (Part One)')

towers_with_subtowers = [twr for twr in tower_structure.keys() if len(tower_structure[twr]['subtowers'])>0]

def subtower_weight(bottom_program: str, wgt: int) -> int:
	weight = 0 
	if len(tower_structure[bottom_program]['subtowers']) == 0:
		return tower_structure[bottom_program]['weight']
	else:
		for subtower in tower_structure[bottom_program]['subtowers']:
			weight += subtower_weight(subtower, tower_structure[subtower]['weight'])
	return wgt + weight

def part_two(bottom_program: str, req=0) -> int:
	weights = {st: subtower_weight(st, tower_structure[st]['weight']) for st in tower_structure[bottom_program]['subtowers']}
	required_wgt = max(list(weights.values()),key=list(weights.values()).count)
	unbalanced_disc = None
	for disc in tower_structure[bottom_program]['subtowers']:
		if weights[disc] != required_wgt:
			unbalanced_disc = disc
	sub_towers = [tower_structure[s]['subtowers'] for s in tower_structure[bottom_program]['subtowers'] if len(tower_structure[s]['subtowers'])>0]
	if unbalanced_disc == None:
		r = max(list(weights.values()),key=list(weights.values()).count)
		total = sum(list(weights.values()) + [tower_structure[bottom_program]['weight']])
		for d in weights.values():
			if d != r:
				return r
		return tower_structure[bottom_program]['weight'] + (req-total)
	else:
		return part_two(unbalanced_disc, required_wgt)

print(f'The weight would need to be {part_two(part_one_answer)} to balance the tower')
