with open('input', 'r') as f:
	contents = f.readlines()
	data = [list(map(int, ln.rstrip('\n').split())) for ln in contents]

print(f'Part One: {sum([max(arr)-min(arr) for arr in data])}')

def part_two(arr: list) -> int:
	arr = [sorted(i) for i in arr]
	results = []
	for subarr in arr:
		for j in subarr[::-1]:
			for i in subarr:
				if j % i == 0 and j != i:
					results.append(j//i)
	return sum(results)

print(f'Part Two: {part_two(data)}')