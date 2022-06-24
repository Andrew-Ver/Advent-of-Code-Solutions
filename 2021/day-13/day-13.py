import re
import numpy as np

with open('input', 'r') as f:
    coords = []
    fold_instructions = []
    ln = f.readline()
    coord_ln = r'(\d+),\d+'
    fold_ln = r'[yx]=\d+'
    while ln:
        if re.match(coord_ln, ln):
            coords.append([int(i) for i in re.findall(r'\d+', ln)])
        elif (fold_ins_found := re.search(fold_ln, ln)):
            a, b = (fold_ins_found.group().split('='))
            fold_instructions.append((a, int(b)))
        ln = f.readline()
    coords = np.array(coords)

def apply_fold(dot_coords: np.numarray, ins_A: str, ins_B: int) -> list[np.numarray, int]:
    max_X = np.max(dot_coords[:, 0])
    max_Y = np.max(dot_coords[:, 1])

    if ins_A == 'y':
        rows = np.where(coords[:,1] > ins_B)
        for i in rows[0]:
            X, Y = dot_coords[i]
            dot_coords[i] = [X, abs(max_Y-Y)]

    elif ins_A == 'x':
        rows = np.where(coords[:,0] > ins_B)
        for i in rows[0]:
            X, Y = dot_coords[i]
            dot_coords[i] = [abs(max_X-X), Y]
    
    return dot_coords, len(np.unique(dot_coords, axis=0))

#print(f'Part One: {apply_fold(coords, fold_instructions[0][0], fold_instructions[0][1])[1]}')

for a, b in fold_instructions:
    coords, uniq = apply_fold(coords, a, b)

for a, b in coords:
    print(a, b)