import re
from collections import *
from copy import deepcopy

crate_stacks: dict[list] = defaultdict(list)
instructions: list[tuple[int]] = []

# Parsing the input
with open('input', 'r') as f:
    crate_pattern: str = r'\[\w\]'

    for ln in f.readlines():
        if re.search(crate_pattern, ln):
            # Crate orientations
            for j in range(1, len(ln), 4):
                char: str = ln[j]
                if char.isalpha():
                    crate_stacks[(j//4)+1].append(char)

        elif re.search(r'move', ln):
            # Save each move instruction as tuple (n, A, B)
            # where n is the number of crates, and A, B are stacks to move from/to
            n, A, B = (int(i) for i in re.findall(r'\d+', ln))
            instructions.append((n, A, B))

# Reverse lists, so that first crate parsed is on top of the stack
# going down the file
for stack in crate_stacks.values():
    stack.reverse()

# copy of crate_stacks for part 2
crate_stacks_copy: dict[list] = deepcopy(crate_stacks)

for n, A, B in instructions:
    # For Part One
    sub_stack: list[str] = [crate_stacks[A].pop() for _ in range(n)]
    crate_stacks[B] += sub_stack

    # Part Two
    sub_stack_part_two: list[str] = [crate_stacks_copy[A].pop() for _ in range(n)]
    crate_stacks_copy[B] += reversed(sub_stack_part_two)


part_one: str = ''.join(crate_stacks[i+1][-1] for i in range(len(crate_stacks)))
print(f'Part One: {part_one}.')

part_two = ''.join(crate_stacks_copy[i+1][-1] for i in range(len(crate_stacks)))
print(f'Part Two: {part_two}')