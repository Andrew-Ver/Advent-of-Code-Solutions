from itertools import combinations

with open('input', 'r') as f:
	container_sizes = [int(ln.strip()) for ln in f.readlines()]
	
total_combinations = 0
shortest_combinations = len(container_sizes)

for combination in [[c for c in list(combinations(container_sizes, i)) if sum(c) == 150] for i in range(len(container_sizes)+1)]:
	combination_length = len(combination)	
	total_combinations += combination_length
	if combination_length < shortest_combinations and combination_length != 0:
		shortest_combinations = combination_length
	
print(f'Part One: {total_combinations} (Part One)')
print(f'Shortest combination: {shortest_combinations} (Part Two)')
