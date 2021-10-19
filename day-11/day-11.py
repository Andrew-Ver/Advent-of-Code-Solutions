import re
import string 

alphabet = string.ascii_lowercase
PUZZLE_INPUT = 'hepxcrrq'
input_string = [alphabet.index(char) for char in PUZZLE_INPUT]


def check_passwd(passwd: str) -> bool:
	if re.search(r'[iol]', passwd) or not len(set(re.findall(r'(.)\1', passwd))) >= 2:
		return False
	if any([passwd[i:i+3] in alphabet for i in range(len(passwd)-2)]):
		return True

def solution() -> str:
	found = False
	new_valid_passwds = []
	while not found and len(new_valid_passwds) < 2:
		input_string[7] = (input_string[7]+1)%26
		if input_string[7] == 0:
			i = 6
			input_string[i] = (input_string[i]+1)%26
			while input_string[i] == 0:
				i -= 1
				input_string[i] =(input_string[i]+1)%26
		if check_passwd(''.join([alphabet[i] for i in input_string])):
			new_valid_passwds.append(''.join([alphabet[i] for i in input_string]))
	return new_valid_passwds

part_one, part_two = solution()

print(f'{part_one} is the next valid password (Part One)')
print(f'{part_two} is the second next valid password (Part Two)')
