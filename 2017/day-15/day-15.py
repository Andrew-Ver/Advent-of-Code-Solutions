with open('input', 'r') as f:
	contents = f.readlines()
	data = [ln.strip() for ln in contents]

gen_a_starting_value = 703
gen_b_starting_value = 516

def generator_generator(current_value: int, factor: int, m=1) -> str:
	while True:
		current_value = (current_value * factor) % 2147483647
		if current_value % m == 0:
			yield f'{current_value:032b}'[16:]

part_one_count = 0 
gen_a = generator_generator(gen_a_starting_value, 16807)
gen_b = generator_generator(gen_b_starting_value, 48271)

for i in range(40000000):
	a = next(gen_a)
	b = next(gen_b)
	if a == b:
		part_one_count += 1

print(f'Answer for Part One: {part_one_count}')

gen_a_two = generator_generator(gen_a_starting_value, 16807, 4)
gen_b_two = generator_generator(gen_b_starting_value, 48271, 8)

part_two_count = 0 

for i in range(5000000):
	a = next(gen_a_two)
	b = next(gen_b_two)
	if a == b:
		part_two_count += 1

print(f'Answer for Part Two: {part_two_count}')