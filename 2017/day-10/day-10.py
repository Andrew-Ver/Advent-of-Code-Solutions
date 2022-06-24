import copy

with open('input', 'r') as f:
	contents = f.readline()
	data = [int(ln) for ln in contents.split(',')]


def part_one(input_lengths: list, lst_length: int, skip_sz: int) -> list:
	lst = [i for i in range(lst_length+1)]
	i = 0 
	for length in data:
		if length + i <= len(lst):
			lst = lst[:i] + lst[i:(i+length)][::-1] + lst[i+length:]
		else:
			chunk_one = lst[i:]; chunk_two = lst[:(length-len(lst[i:]))]
			reversed_chunk = (chunk_one + chunk_two)[::-1]
			# The sublist needs to wrap around
			for x in range(len(reversed_chunk)):
				lst[(x+i)%len(lst)] = reversed_chunk[x]
		i = (i+length+skip_sz) % len(lst)
		skip_sz += 1
	return lst

print(f'Part One Answer: {part_one(data, 255, 0)[0]*part_one(data, 255, 0)[1]}')

input_part_two = [ord(ch) for ch in contents.rstrip('\n')] + [int(c) for c in ['17', '31', '73', '47', '23']]

def get_spare_hash(input_lengths: list) -> list:
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

sparse_hash = get_spare_hash(input_part_two)
dense_hash  = get_dense_hash(sparse_hash)

print(f'Part Two Answer: {"".join([hex(n)[2:].zfill(2) for n in dense_hash])}')