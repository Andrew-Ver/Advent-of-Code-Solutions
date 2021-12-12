from collections import defaultdict
import re

with open('input', 'r') as f:
    puzzle_input = [ln.strip() for ln in f.readlines()]

cave_map = defaultdict(list)

for ln in puzzle_input:
    A, B = re.findall(r'\w+', ln)
    if B != 'start':
        cave_map[A].append(B)
    if B != 'end' and A != 'start':
        cave_map[B].append(A)

def solution(part: int) -> int:
    unique_paths = []
    to_explore = [(['start']+[p], False) for p in cave_map['start']]

    while to_explore:
        cave_path, visited_twice_already = to_explore.pop()
        curr_cave = cave_path[-1]

        if curr_cave == 'end':
            unique_paths.append(cave_path)
        connected = []
        #In part one you can only visit each small cave once, in part two a SINGLE small cave can be visited twice.
        for cave in cave_map[curr_cave]:
            if part == 1:
                if cave.isupper() or cave not in cave_path:
                    connected.append(cave)
            elif part == 2:
                if cave.isupper() or (cave.islower() and cave not in cave_path):
                    connected.append((cave, visited_twice_already))
                elif cave.islower() and cave in cave_path and not visited_twice_already:
                    connected.append((cave, True))
        if part == 1:
            to_explore.extend([(cave_path+[connected_cave], visited_twice_already) for connected_cave in connected])
        elif part == 2:
            to_explore.extend([(cave_path+[connected_cave], visit_status) for connected_cave, visit_status in connected])

    return len(unique_paths)

print(f'Part One, Unique paths visiting each small cave a maximum of one time: {solution(1)}')

print(f'Part Two, Unique paths if you can visit a single small cave TWICE: {solution(2)}')
