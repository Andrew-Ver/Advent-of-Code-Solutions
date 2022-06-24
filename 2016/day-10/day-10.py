import re
from collections import defaultdict
import numpy

with open('input', 'r') as f:
	contents = f.readlines()
	data = [ln.strip() for ln in contents]

def solution(instructions=data) -> list:
	bots = defaultdict(set)
	output_bins = defaultdict(set)
	#Initial starting state of bots
	initial_chip_instructions = [ins for ins in instructions if re.search(r'goes to', ins)]
	for initial in initial_chip_instructions:
		val, bot = re.findall(r'(\d+|bot \d+)', initial)
		bots[bot].add(int(val))

	#bots cannot take action until they are holding 2 chips
	while not all([len(bots[b])==2 for b in bots.keys()]):
		for ins in [ins for ins in instructions if not re.search(r'goes to', ins)]:
			#gives low to (output n|bot n), gives high to (output n|bot n )
			# low is always first and high is always second
			bot_giving = re.search(r'bot \d+', ins[:7]).group()
			if len(bots[bot_giving]) < 2:
				pass
			else:
				receivers = re.findall(r'(bot \d+|output \d+)', ins[7:])
				low = min(bots[bot_giving]); high = max(bots[bot_giving])
				if receivers[0].startswith('output'):
					output_bins[receivers[0]].add(low)
				else:
					bots[receivers[0]].add(low)
				if receivers[1].startswith('output'):
					output_bins[receivers[1]].add(high)
				else:
					bots[receivers[1]].add(high)
	for b in bots.keys():
		if bots[b] == {61, 17}:
			return b, numpy.product([*output_bins['output 0'], *output_bins['output 1'], *output_bins['output 2']])

answer = solution()
print(f'Bot responsible for comparing value-61 and value-17 chips: {answer[0]} (Part One)')
print(f'Output 0, 1 and 2 multiplied together: {answer[1]} (Part Two)')

