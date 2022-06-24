import re
from string import ascii_lowercase

with open('input', 'r') as f:
	contents = f.readlines()
	data = [ln.strip() for ln in contents]

alphabet = ascii_lowercase

def part_one(rooms=data) -> int:
	sector_id_sum = 0
	
	for room_id in rooms:
		checksum = ''.join(re.search(r'\[\w+\]', room_id).group()[1:-1])
		sector_id = int(re.search(r'\d+', room_id).group())
		encrypted_letters = re.findall(r'[a-z]', room_id[:-7])
		letters_ranked_by_occurance = sorted([l for l in sorted(list(set(encrypted_letters)))], key=lambda x: encrypted_letters.count(x), reverse=True)
		if checksum == ''.join(letters_ranked_by_occurance[:5]):
			sector_id_sum += sector_id
	return sector_id_sum

print(f'Part One: {part_one()}')

def part_two(rooms=data) -> int:
	for room_id in rooms:
		checksum = ''.join(re.search(r'\[\w+\]', room_id).group()[1:-1])
		sector_id = int(re.search(r'\d+', room_id).group())
		encrypted_letters = re.findall(r'[a-z\-]', room_id[:-7])
		new_words = ''
		for letter in encrypted_letters:
			if letter == '-':
				new_words += ' '
			else:
				new_words += alphabet[(alphabet.index(letter)+sector_id)%26]
		if 'northpole' in new_words:
			return sector_id
			
print(f'Part Two: {part_two()}')