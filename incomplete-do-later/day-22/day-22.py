import re

with open('input', 'r') as f:
    puzzle_input = [[int(m) if m.isnumeric() or m.startswith('-') else m for m in re.findall(r'(on|off|-?\d+)', ln)] for ln in f.readlines()]

cuboid_ranges: dict[tuple[int, int], str] = {tuple(step[1:]): step[0] for step in puzzle_input}

def answer(cube_ranges: dict) -> int:
    cubes_on: int = 0
    visited_ranges: set[tuple[int, int, int]] = set()

    for coords, light in cube_ranges.items():
        if light == 'on':
            X1, X2, Y1, Y2, Z1, Z2 = coords
            cubes_on += (X2-X1+1) * (Y2-Y1+1) * (Z2-Z1+1)
            visited_ranges.update((X1, X2, Y1, Y2, Z1, Z2))


one = (10, 12, 10, 12, 10, 12)
two = (11, 13, 11, 13, 11, 13)

print(one[1] - two[0], one[0] - two[1])
print(one[3] - two[2], one[2] - two[3])
print(one[5] - two[4], one[4] - two[5])