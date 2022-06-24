from copy import deepcopy
from collections import deque

with open('input', 'r') as f:
    puzzle_input = [ln.rstrip().zfill(11)+'##' if len(ln) < 13 else ln.rstrip() for ln in f.readlines()]

hallway_squares = [(r, c) for r in range(len(puzzle_input)) for c in range(len(puzzle_input[0])) if puzzle_input[r][c] == '.']
amphipod_start_squares = [(r, c) for r in range(len(puzzle_input)) for c in range(len(puzzle_input[0])) if puzzle_input[r][c].isalpha()]
ROOM_ENTRANCES = {(1, 3), (1, 5), (1, 7), (1, 9)}
DEST_COL = {'A': 3, 'B': 5, 'C': 7, 'D': 9}

def available_moves(amphipod: list[str, int, int], occupied_positions: set[int, int], visited: set[tuple[int, int]]) -> set[tuple[int, int]]:
    '''
        Returns a set of available positions for a given amphipod, will only return the final destination if it is available
    '''
    X, Y = amphipod[1], amphipod[2]
    destination_col = DEST_COL[amphipod[0]]
    if (X, Y) == (3, destination_col):
        return set()
    else:
        def bfs(A, B) -> set:
            avail = set()
            q = [(a, b) for a, b in [(A-1, B), (A+1, B), (A, B-1), (A, B+1)] 
                        if (a, b) in hallway_squares and (a, b) not in occupied_positions and (a, b) not in avail]
            while q:
                A, B = q.pop()
                if (A, B) not in ROOM_ENTRANCES:
                    avail.add((A, B))
                neighbours = [(A-1, B), (A+1, B), (A, B-1), (A, B+1)]
                for a, b in neighbours:
                        if ((a, b) in hallway_squares or (a, b) in {(2, destination_col), (3, destination_col)}) and (a, b) not in occupied_positions and ((a, b) not in avail and (a, b) not in q):
                            q.append((a, b))
            return avail.difference(visited)
        avail = bfs(X, Y)
        if (3, destination_col) in avail:
            return {(3, destination_col)}
        return avail.difference(visited)

def all_in_correct_position(a_list: list[tuple[str, int, int]]) -> bool:
    for a in a_list:
        s, x, y = a[1], a[0][0], a[0][1]
        if y != DEST_COL[s]:
            return False
    return True

'''
    (Current amphipod position, its label, previous move)
'''
#Initial amphipods
amphipods = [[(X, Y), puzzle_input[X][Y], {(X, Y)}, 0] for X, Y in amphipod_start_squares]
occupied_positions = {a[0] for a in amphipods}
minimum_energy_used = float('inf')

# Amphipods stored as:
# [(X_pos, Y_Pos)]
# Label: str
# Previous X_pos, Y_pos
# Steps used (to be later summed up according to label)

queue = []
for i, amph in enumerate(amphipods):
    orig_X, orig_Y = amph[0]
    s = amph[1]
    all_positions = {a[0] for a in amphipods}
    for avail_X, avail_Y in available_moves((s, orig_X, orig_Y), all_positions, amph[2]):
        c = deepcopy(amphipods)
        c[i] = [(avail_X, avail_Y), s, c[i][2], c[i][-1]+(abs(orig_X-avail_X)+abs(orig_Y-avail_Y))]
        c[i][2].add((avail_X, avail_Y))
        queue.append(c)
count = 0
while queue:
    amphipods = queue.pop()
    #if count % 1000 == 0:
    #    print(f'Curr: {amphipods}\n')
    none_avail = True
    if all_in_correct_position(amphipods):
        print(f'Reached the end!!!')
    else:
        for i, amph in enumerate(amphipods):
            orig_X, orig_Y = amph[0]
            s = amph[1]
            previously_visited = amph[2]
            all_positions = {a[0] for a in amphipods}

            available_spots = available_moves((s, orig_X, orig_Y), all_positions, amph[2])
            for avail_X, avail_Y in available_spots:
                if (avail_X, avail_Y) not in amph:
                    c = deepcopy(amphipods)
                    c[i] = [(avail_X, avail_Y), s, c[i][2], abs(orig_X-avail_X)+abs(orig_Y-avail_Y)]
                    c[i][2].add((avail_X, avail_Y))
                    #print(f'Orig: {amphipods} vs c {c}')
                    queue.append(c)
    count += 1