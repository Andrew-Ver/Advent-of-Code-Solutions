with open('input', 'r') as f:
	puzzle_input = [int(line.strip()) for line in f.readlines()]

part_one = 0
prev = None

for num in puzzle_input:
    if prev != None:
        if num > prev:
            part_one += 1
    prev = num

part_two = 0
prev = puzzle_input[:3]

for i in range(len(puzzle_input)):
    curr_window = (prev[1:] + [puzzle_input[i]])
    if sum(curr_window) > sum(prev):
        part_two += 1
    prev = curr_window

print(f'Part One: {part_one}')
print(f'Part Two: {part_two}')
