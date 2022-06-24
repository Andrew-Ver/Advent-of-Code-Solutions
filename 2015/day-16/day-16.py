import re
from collections import defaultdict

with open('input', 'r') as f:
	PUZZLE_INPUT = [ln.strip() for ln in f.readlines()]

#From the input prompt
correct_aunt = "children: 3 cats: 7 samoyeds: 2 pomeranians: 3 akitas: 0 vizslas: 0 goldfish: 5 trees: 3 cars: 2 perfumes: 1"
correct_aunt = {descr: int(quantity) for descr, quantity in zip(re.findall(r'[a-z]+', correct_aunt), re.findall(r'\d+', correct_aunt))}

known_aunts = defaultdict(lambda: defaultdict(int))

for ln in PUZZLE_INPUT:
	sue_n, attributes, quantities = re.search(r'Sue \d+', ln).group(), re.findall(r'[a-z]+', ln[7:]), list(map(int, re.findall(r'\d+', ln[9:])))
	 
	for attribute, quantity in zip(attributes, quantities):	
		known_aunts[sue_n][attribute] = quantity

#Part One
for known_aunt in known_aunts.keys():
	known_attributes = [known_aunts[known_aunt][attr] == correct_aunt[attr] for attr in known_aunts[known_aunt].keys()]
	if all(known_attributes):
		print(f'The Aunt that got you the gift is {known_aunt} Part One')	
		break

#Part Two
for known_aunt in known_aunts.keys():
	known_attributes = [known_aunts[known_aunt][attr] == correct_aunt[attr] for attr in known_aunts[known_aunt].keys() if attr not in ['cats', 'trees', 'pomeranians', 'goldfish']]
	#Wrong input possibly? 
	if all(known_attributes) and known_aunts[known_aunt]['trees'] > correct_aunt['trees'] and known_aunts[known_aunt]['goldfish'] < correct_aunt['goldfish']:
		print(f'The REAL Aunt that got you the gift is {known_aunt} Part Two')	
		break