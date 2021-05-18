import copy

with open('input', 'r') as f:
	contents = f.readline()
	data = [int(ln) for ln in contents.split('\t')]

seen_distributions = set()
cycles = 0
memory_blocks = copy.deepcopy(data)

while True:
	largest_blk_idx = memory_blocks.index(max(memory_blocks))
	for i in range(1, memory_blocks[largest_blk_idx]+1):
		memory_blocks[(largest_blk_idx+i) % len(memory_blocks)] += 1
		memory_blocks[largest_blk_idx] -= 1
	cycles += 1
	if tuple(memory_blocks) in seen_distributions:
		break
	else:
		seen_distributions.add(tuple(memory_blocks))
print(f'Part One: {cycles}')

part_two_seen_distributions = set()
part_two_seen_distributions.add(tuple(copy.deepcopy(memory_blocks)))
part_two_cycles = 0

while True:
	largest_blk_idx = memory_blocks.index(max(memory_blocks))
	for i in range(1, memory_blocks[largest_blk_idx]+1):
		memory_blocks[(largest_blk_idx+i) % len(memory_blocks)] += 1
		memory_blocks[largest_blk_idx] -= 1
	part_two_cycles += 1
	if tuple(memory_blocks) in part_two_seen_distributions:
		break
	else:
		part_two_seen_distributions.add(tuple(memory_blocks))
print(f'Part Two: {part_two_cycles}')