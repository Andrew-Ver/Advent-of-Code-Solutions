import re
from collections import defaultdict, deque

key_string = 'xlqgujun'

#From Day 10, Part Two
def get_sparse_hash(input_lengths: list) -> list:
	lst = [i for i in range(256)]
	i = 0 
	skip_sz = 0
	for x in range(64):
		for length in input_lengths:
			if length + i <= len(lst):
				lst = lst[:i] + lst[i:(i+length)][::-1] + lst[i+length:]
			else:
				chunk_one = lst[i:]; chunk_two = lst[:(length-len(lst[i:]))]
				reversed_chunk = (chunk_one + chunk_two)[::-1]
				for x in range(len(reversed_chunk)):
					lst[(x+i)%len(lst)] = reversed_chunk[x]
			i = (i+length+skip_sz) % len(lst)
			skip_sz += 1
	return lst

def get_dense_hash(sparse: list) -> list:
	lst = []
	for i in range(0, len(sparse), 16):
		num = sparse[i]
		for j in range(i+1, i+16):
			num = num ^ sparse[j]
		lst.append(num)
	return lst

def part_one(k_str: str) -> int:
	squares_used = 0	
	for i in range(128):
		test = [ord(ch) for ch in key_string+'-'+str(i)] + [int(c) for c in ['17', '31', '73', '47', '23']]
		sparse = get_sparse_hash(test)
		dense = get_dense_hash(sparse)
		knot_hash = "".join([hex(n)[2:].zfill(2) for n in dense])
		squares_used += ''.join([bin(int(ch, 16))[2:].zfill(4) for ch in knot_hash]).count('1')
	return squares_used

print(f'{part_one(key_string)} squares used for Part One')


def find_connected_cells(grid: list, origin_r: int, origin_p: int) -> set:
	stack = deque()
	visited = []
	connected = []
	stack.append((origin_r, origin_p))
	'''
	Add the neighbours containing '1' to the stack, pop and check its neighbours until empty
	'''
	while len(stack) != 0:
		r, p = stack.pop()
		visited.append((r, p))
		connected.append((r, p))
		occupied_neighbours = [(r-1, p), (r+1, p), (r, p-1), (r, p+1)]
		for neighbour_r, neighbour_p in occupied_neighbours:
			if 127 >= neighbour_r >= 0 and 127 >= neighbour_p >= 0 and grid[neighbour_r][neighbour_p] == '1' and (neighbour_r, neighbour_p) not in visited:
				connected.append((neighbour_r, neighbour_p))
				stack.append((neighbour_r, neighbour_p))
	return set(connected)

def part_two(k_str: str) -> int:
	grid = []
	regions = defaultdict(set)
	checked = set()
	n = 1
	for i in range(128):
		test = [ord(ch) for ch in key_string+'-'+str(i)] + [int(c) for c in ['17', '31', '73', '47', '23']]
		sparse = get_sparse_hash(test)
		dense = get_dense_hash(sparse)
		knot_hash = "".join([hex(n)[2:].zfill(2) for n in dense])
		grid.append(''.join([bin(int(ch, 16))[2:].zfill(4) for ch in knot_hash]))
	for row in range(128):
		for pos in range(128):
			for m in re.finditer(r'1{1,}', grid[row]):
				if (row, m.start()) not in checked:
					connected_cells = find_connected_cells(grid, row, m.start())
					checked.update(connected_cells)
					regions[n].update(connected_cells)
					n += 1
	return regions

print(f'The total number of Regions is: {len(part_two(key_string))} (Part Two)')