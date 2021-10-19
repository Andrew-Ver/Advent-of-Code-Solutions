from collections import defaultdict
from functools import reduce

#https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

PUZZLE_INPUT = 34000000
houses_delivered = defaultdict(int)
part_one_found = False
part_two_found = False
house_number = 0

while not (part_one_found and part_two_found):
	house_number += 1
	f = factors(house_number)
	presents = sum({elf * 10 for elf in f})
	elves_delivering = {elf: 0 for elf in f if houses_delivered[elf] <50}
	for elf in elves_delivering:
		houses_delivered[elf] += 1
	presents_part_two = sum({elf * 11 for elf in elves_delivering})

	if presents >= PUZZLE_INPUT and not part_one_found:
		print(f'{house_number} (Part One)')
		part_one_found = True
	if presents_part_two >= PUZZLE_INPUT//10 and not part_two_found:
		print(f'{house_number*10} (Part Two)')
		part_two_found = True
		