import re

with open('input', 'r') as f:
    puzzle_input: list[tuple[str, int]] = [(re.search(r'\w', ln).group(), int(re.search(r'\d+', ln).group())) for ln in f.readlines()]

def solution(n_nodes: int, puzzle_input=puzzle_input):
    def move_head(pos: tuple[int], direction: str) -> tuple[int, int]:
        '''
            New head position after one step based on direction
        '''
        Y, X = pos
        movement: dict[str, tuple[int]] = {'R': (Y, X+1),
                                           'D': (Y+1, X),
                                           'L': (Y, X-1),
                                           'U': (Y-1, X)}
        return movement[direction]

    def move_tail(head_position: tuple[int], tail_position: tuple[int]) -> tuple[int]:
        diff_y: int = (head_position[0] - tail_position[0])
        diff_x: int = (head_position[1] - tail_position[1])
        Y, X = tail_position

        # Left/right movement
        movement: dict[str, tuple[int]] = {
            (0, 2): (Y, X+1),
            (0, -2): (Y, X-1),
            (-2, 0): (Y-1, X),
            (2, 0): (Y+1, X),
            # For part two
            (2, 2): (Y+1, X+1),
            (2, -2): (Y+1, X-1),
            (-2, 2): (Y-1, X+1),
            (-2, -2): (Y-1, X-1),
        }

        if (diff_y, diff_x) in movement:
            return movement[(diff_y, diff_x)]

        # Handle Diagonal movements
        # ex. Difference of (2, 1) => (1, 1)
        if diff_y == 2:
            return (Y+1, X+diff_x)
        elif diff_y == -2:
            return (Y-1, X+diff_x)
        elif diff_x == 2:
            return (Y+diff_y, X+1)
        elif diff_x == -2:
            return(Y+diff_y, X-1)
        return (tail_position)

    tail_visited: set[int] = set()
    # The first one will the "head", the rest are the tails following
    # the next node in list
    node_positions: list[tuple[int]] = [(0, 0) for _ in range(n_nodes)]

    for d, amount in puzzle_input:
        for _ in range(amount):
            '''
                Move the head independent of other nodes,
                other nodes i move in relation to node i-1
            '''
            for i in range(len(node_positions)):
                if i == 0:
                    node_positions[i] = move_head(pos=node_positions[i], direction=d)
                else:
                    node_positions[i] = move_tail(head_position=node_positions[i-1], tail_position=node_positions[i])

            tail_visited.add(node_positions[-1])

    return len(tail_visited)

print(f'Part One: {solution(2)}.')
print(f'Part Two: {solution(10)}')