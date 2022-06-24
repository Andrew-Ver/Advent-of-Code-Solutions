import re
from collections import defaultdict
from itertools import permutations

with open('input', 'r') as f:
	PUZZLE_INPUT = [ln.strip() for ln in f.readlines()]

happiness_graph = defaultdict(dict)

for rule in PUZZLE_INPUT:
	person_A, change, happiness_change, person_B = re.findall(r'(gain|lose|[A-Z]\w+|-?\d+)', rule)
	if change == 'gain':
		happiness_change = int(happiness_change)
	else:
		happiness_change = int('-'+happiness_change)
	happiness_graph[person_A][person_B] = happiness_change

def solution(part: int, graph: dict = happiness_graph) -> int:
	best_happiness = 0 
	if part == 1:
		perms = list(permutations(happiness_graph.keys(), 8))
	elif part == 2:
		happiness_graph['Me'] = {person: 0 for person in happiness_graph.keys()}
		everyone_except_me = {p for p in happiness_graph.keys() if p != 'Me'}
		for i in everyone_except_me:
			happiness_graph[i]['Me'] = 0
		perms = list(permutations(list(happiness_graph.keys()), 9))
	for arrangement in perms:
		total_happiness = 0
		for i in range(len(arrangement)):
			if i == 0:
				total_happiness += happiness_graph[arrangement[i]][arrangement[-1]]
				total_happiness += happiness_graph[arrangement[i]][arrangement[i+1]]
			else:
				total_happiness += happiness_graph[arrangement[i]][arrangement[i-1]]
				total_happiness += happiness_graph[arrangement[i]][arrangement[(i+1)%len(arrangement)]]
		best_happiness = max(best_happiness, total_happiness)
	return best_happiness

print(f'The total change in happiness for the optimal seating arrangement is {solution(part=1)} (Part One)')
print(f'{solution(part=2)} (Part Two)')
