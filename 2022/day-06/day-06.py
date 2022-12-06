with open('input', 'r') as f:
    puzzle_input = f.readline().strip()

curr: set[str] = set()
part_one_reached: bool = False

for i, c in enumerate(puzzle_input):
    if c in curr:
        curr = {c}
    else:
        curr.add(c)

    if not part_one_reached and len(curr) == 4:
        print(f'Part One: {i+1}')
        part_one_reached = True

    if len(curr) == 13:
        print(f'Part Two: {i+1}')
        break
