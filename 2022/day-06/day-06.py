from collections import deque

with open('input', 'r') as f:
    puzzle_input = f.readline().strip()


def solution(s: str, length: int) -> int:
    last_four: deque[str] = deque()
    last_four_set: set[str] = set()

    for i, c in enumerate(s):
        last_four.append(c)
        last_four_set.add(c)

        if len(last_four) > length:
            '''
                If the first character in queue is only present once,
                remove it from the set
            '''
            first: str = last_four.popleft()
            if first not in last_four:
                last_four_set.remove(first)

        if len(last_four_set) == length:
            return i+1

print(f'Part One: {solution(puzzle_input, 4)}')
print(f'Part One: {solution(puzzle_input, 14)}')