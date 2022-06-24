import re
from collections import defaultdict
from itertools import *
from math import ceil

with open('input', 'r') as f:
	PUZZLE_INPUT = [ln.strip() for ln in f.readlines()]

boss = {stat: amount for stat, amount in zip(['Hit Points', 'Damage', 'Armor'], [int(i) for i in re.findall(r'\d+', ''.join(PUZZLE_INPUT[:3]))])}

weapon_shop  = defaultdict(dict)
armor_shop   = defaultdict(dict)
ring_shop    = defaultdict(dict)

for wep in PUZZLE_INPUT[5:10]:
	name, cost, dmg, armor = re.findall(r'([A-Z]\w+|\d+)', wep)
	weapon_shop[name]['cost'], weapon_shop[name]['dmg'], weapon_shop[name]['armor'] = [int(item) for item in [cost, dmg, armor]]
for ar in PUZZLE_INPUT[12:17]:
	name, cost, dmg, armor = re.findall(r'([A-Z]\w+|\d+)', ar)
	armor_shop[name]['cost'], armor_shop[name]['dmg'], armor_shop[name]['armor'] = [int(item) for item in [cost, dmg, armor]]
for ring in PUZZLE_INPUT[19:25]:
	name = re.search(r'(Damage|Defense)\s\+\d', ring).group()
	cost, dmg, armor = re.findall(r'\d+', ring[11:])
	ring_shop[name]['cost'], ring_shop[name]['dmg'], ring_shop[name]['armor'] = [int(item) for item in [cost, dmg, armor]]

#Flatten lists for itertools.product()
armor_combinations = [c for i in range(0, 2) for c in combinations(armor_shop.keys(), i)]
ring_combinations  = [c for i in range(0, 3) for c in combinations(ring_shop.keys(), i)]

def stats_from_equipment(equipment: list) -> dict:
	stats = {'hitpoints': 100, 'dmg': 0, 'armor': 0, 'cost': 0}
	weapon, armor, rings = equipment
	stats['dmg'] += weapon_shop[weapon]['dmg']; stats['cost'] += weapon_shop[weapon]['cost']
	if armor:
		stats['armor'] += armor_shop[armor[0]]['armor']; stats['cost'] += armor_shop[armor[0]]['cost']
	for ring in rings:
		stats['dmg'] += ring_shop[ring]['dmg']; stats['cost'] += ring_shop[ring]['cost']; stats['armor'] += ring_shop[ring]['armor']
	return stats

lowest_cost = 300
highest_cost_part_two = 0

for equipment_combination in product(list(weapon_shop.keys()), armor_combinations, ring_combinations):
	my_stats = stats_from_equipment(equipment_combination)
	to_kill_me = ceil(my_stats['hitpoints'] / max((boss['Damage'] - my_stats['armor']), 1))
	to_kill_boss = ceil(boss['Hit Points'] / max((my_stats['dmg'] - boss['Armor']), 1))
	
	if to_kill_boss <= to_kill_me:
		lowest_cost = min(lowest_cost, my_stats['cost'])
	if to_kill_boss > to_kill_me:
		highest_cost_part_two = max(highest_cost_part_two, my_stats['cost'])

print(f'Minimum Cost for equipment to defeat boss: {lowest_cost} (Part One)')

print(f'Highest Cost for equipment to still lose to the boss: {highest_cost_part_two} (Part Two)')