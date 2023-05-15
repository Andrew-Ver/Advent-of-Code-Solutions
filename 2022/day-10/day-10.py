import re

with open('input', 'r') as f:
    puzzle_input: list[list[str]] = [re.findall(r'(\w+|-?\d+)', ln) for ln in f.readlines()]

curr_cycle: int = 0
X_register: int = 1
signal_sum: int = 0

needed_cycles: set[int] = {20, 60, 100, 140, 180, 220}

for cmd in puzzle_input:
    if cmd[0] == 'addx':
        for _ in range(2):
            curr_cycle += 1
            if curr_cycle in needed_cycles:
                signal_sum += (X_register * curr_cycle)
        X_register += int(cmd[1])
    else:
        curr_cycle += 1
        if curr_cycle in needed_cycles:
            signal_sum += (X_register * curr_cycle)

print(f'Part One: {signal_sum}')