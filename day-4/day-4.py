import re

with open('input', 'r') as f:
	contents = f.readlines()
	data = [ln.rstrip('\n').split() for ln in contents]

valid = 0
for phrase in data:
	unique_words = [phrase.count(word)==1 for word in phrase]
	if all(unique_words):
		valid += 1
print(f'Part One: {valid}')

part_two_valid = 0
for phrase in data:
	phrase = [''.join(sorted(word)) for word in phrase]
	non_anagrams = [phrase.count(word)==1 for word in phrase]
	if all(non_anagrams):
		part_two_valid += 1
print(f'Part Two: {part_two_valid}')