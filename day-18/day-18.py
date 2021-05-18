import re
from collections import defaultdict, deque

with open('input', 'r') as f:
	contents = f.readlines()
	data = [ln.strip() for ln in contents]

def part_one(commands: list) -> list:
	registers = defaultdict(int)
	sounds_played = []
	c = 0 
	while 0 <= c and c <= len(commands):
		cmd_list = re.findall(r'(snd|set|add|mul|mod|rcv|jgz|[a-z]|-?\d+)', commands[c])
		if len(cmd_list) == 2:
			x = cmd_list[1]
			if cmd_list[0] == 'snd':
				sounds_played.append(registers[x])
				c += 1
			elif cmd_list[0] == 'rcv':
				if registers[x]:
					return sounds_played[-1]
				c += 1
		elif len(cmd_list) == 3:
			x, y = cmd_list[1:]
			if re.search(r'-?\d+', y):
				y = int(y)
			else:
				y = registers[y]
			if cmd_list[0] == 'set':
				registers[x] = y
				c += 1
			elif cmd_list[0] == 'add':
				registers[x] += y
				c += 1
			elif cmd_list[0] == 'mul':
				registers[x] *= y
				c += 1
			elif cmd_list[0] == 'mod':
				registers[x] %= y
				c += 1
			elif cmd_list[0] == 'jgz':
				if registers[x] > 0:
					c += y
				else:
					c += 1
	return sounds_played[-1]


print(f'Answer for Part One: {part_one(data)}')

