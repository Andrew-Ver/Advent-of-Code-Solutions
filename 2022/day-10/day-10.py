import re

with open('input', 'r') as f:
    puzzle_input: list[list[str]] = [re.findall(r'(\w+|-?\d+)', ln) for ln in f.readlines()]

curr_cycle: int = 0
X_register: int = 1
signal_sum: int = 0

needed_cycles: set[int] = {20, 60, 100, 140, 180, 220}
drawing = [[' ' for c in range(40)] for r in range(6)]

for cmd in puzzle_input:
    '''
        For Part Two, if the current X-register is within range of
        X-1 <= curr_cycle <= X+1, draw '#'
    '''
    if cmd[0] == 'addx':
        for _ in range(2):
            row, col = divmod(curr_cycle, 40)
            if (X_register-1 <= col <= X_register+1):
                drawing[row][col] = '#'

            curr_cycle += 1

            # For Part One
            if curr_cycle in needed_cycles:
                signal_sum += (X_register * curr_cycle)
        X_register += int(cmd[1])

    else:
        row, col = divmod(curr_cycle, 40)
        if (X_register-1 <= col <= X_register+1):
            drawing[row][col]

        curr_cycle += 1

        # For Part One
        if curr_cycle in needed_cycles:
            signal_sum += (X_register * curr_cycle)

    row, col = divmod(curr_cycle, 40)
    if (X_register-1 <= col <= X_register+1):
        drawing[row][col] = '#'


print(f'Part One: {signal_sum}')

print(f'Part Two(Drawing):')
for ln in drawing:
    print(' '.join(ln))