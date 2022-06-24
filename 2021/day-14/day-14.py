from collections import defaultdict
import re

with open('input', 'r') as f:
    puzzle_input = f.readlines()

polymer = {puzzle_input[0].strip()[i:i+2]: 1 for i in range(len(puzzle_input[0].strip())-1)}

insertion_rules = {}
for ln in puzzle_input[2:]:
    pre, new_c = re.findall(r'\w+', ln)
    insertion_rules[pre] = (pre[0]+new_c, new_c+pre[1])

def polymer_character_counts(initial_pair_counts: dict, rules: dict, steps: int) -> dict:
    new_polymer_pair_counts = initial_pair_counts.copy()
    need_to_add = list(initial_pair_counts)[0][0]

    for _ in range(steps):
        new = defaultdict(int)
        for pre, result in rules.items():
            if pre in new_polymer_pair_counts:
                count = new_polymer_pair_counts[pre]
                new[result[0]] += count
                new[result[1]] += count
        new_polymer_pair_counts = new

    total_letter_counts = defaultdict(int)
    l = list([(k, v) for k, v in new_polymer_pair_counts.items()])
    
    for letters, count in l:
        total_letter_counts[letters[1]] += count

    total_letter_counts[need_to_add] += 1
    return total_letter_counts

polymer_counts = polymer_character_counts(polymer, insertion_rules, 10).values()

print(f'Part One: {max(polymer_counts) - min(polymer_counts)}')

polymer_counts = polymer_character_counts(polymer, insertion_rules, 40).values()

print(f'Part Two: {max(polymer_counts) - min(polymer_counts)}')