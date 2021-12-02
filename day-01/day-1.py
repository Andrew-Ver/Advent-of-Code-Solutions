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
prev = None

for i in range(len(puzzle_input)-2):
    if prev != None:
        if sum(puzzle_input[i:i+3]) > prev:
            part_two += 1
    prev = sum(puzzle_input[i:i+3])

print(f'Part One: {part_one}')
print(f'Part Two: {part_two}')