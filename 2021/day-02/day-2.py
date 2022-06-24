import re

with open('input', 'r') as f:
	puzzle_input = [line.strip() for line in f.readlines()]

def answer(part: int, commands = list[str]) -> int:
    X_pos = 0
    depth = 0
    aim   = 0
    for ln in puzzle_input:
        command, X = re.findall(r'(forward|down|up|\d)', ln)
        X = int(X)
        if command == 'forward':
            if part == 1:
                X_pos += X
            else:
                X_pos += X
                depth += (aim*X)
        elif command == 'down':
            if part == 1:
                depth += X
            else:
                aim += X
        elif command == 'up':
            if part == 1:
                depth -= X
            else:
                aim -= X
    if part == 1:
        return (X_pos * depth)
    return X_pos * depth

print(f'Part One: {answer(1, puzzle_input)}')
print(f'Part Two: {answer(2, puzzle_input)}')