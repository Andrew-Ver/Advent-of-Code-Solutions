with open('input', 'r') as f:
	contents = f.readlines()
	data = [ln.strip() for ln in contents]

def solution(lst=data) -> str:
	rearranged_input = [''.join([lst[n][i] for n in range(len(lst))]) for i in range(len(lst[0]))]
	part_one_message = [max(column, key=lambda x: column.count(x)) for column in rearranged_input]
	part_two_message = [min(column, key=lambda x: column.count(x)) for column in rearranged_input]

	return ''.join(part_one_message), ''.join(part_two_message)

print(f'Part One Message: {solution()[0]}')
print(f'Part Two Message: {solution()[1]}')