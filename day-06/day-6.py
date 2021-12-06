import re
from collections import Counter, defaultdict

with open('input', 'r') as f:
	puzzle_input = [int(n) for n in re.findall(r'\d+', f.readline())]

def update_fish(fish: list[int], iterations: int) -> list[int]:
    fish_counter = defaultdict(int, Counter(fish))
    total_fish = sum(fish_counter.values())

    for _ in range(iterations):
        fish_counter = defaultdict(int, {day-1: v for day, v in fish_counter.items()})
        
        new_fish = fish_counter[-1]
        fish_counter[-1] = 0
        fish_counter[8] += new_fish
        fish_counter[6] += new_fish
        total_fish += new_fish

    return total_fish

print(f'Part One: {update_fish(puzzle_input, 80)}')
print(f'Part Two: {update_fish(puzzle_input, 256)}')