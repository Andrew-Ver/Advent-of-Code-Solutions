import re
from collections import defaultdict
from itertools import combinations_with_replacement
import math

with open('input', 'r') as f:
	PUZZLE_INPUT = [ln.strip() for ln in f.readlines()]

ingredients_list = defaultdict(dict)

for ln in PUZZLE_INPUT:
	ingredient, capacity, durability, flavor, texture, calories = re.findall(r'([A-Z]\w+|-?\d+)', ln)
	ingredients_list[ingredient]['capacity'] = int(capacity)
	ingredients_list[ingredient]['durability'] = int(durability)
	ingredients_list[ingredient]['flavor'] = int(flavor)
	ingredients_list[ingredient]['texture'] = int(texture)
	ingredients_list[ingredient]['calories'] = int(calories)

def solution(ingredients_list: dict = ingredients_list, calories_required: int = None) -> int:
	'''Find the best score out of each combination of possible recipes 
		Example: 44 tsps of butterscotch, 56 tsps cinnamon:
	    A capacity of 44*-1 + 56*2 = 68
	    A durability of 44*-2 + 56*3 = 80
	    A flavor of 44*6 + 56*-2 = 152
	    A texture of 44*3 + 56*-1 = 76
	    68 * 80 * 152 * 76 = 62842880
	'''
	best_score = 0 
	attributes = ['capacity', 'durability', 'flavor', 'texture', 'calories']
	all_possible_recipes = combinations_with_replacement([ingredient for ingredient in ingredients_list.keys()], 100)
	for recipe in all_possible_recipes:
		if not calories_required:
			score = [sum([recipe.count(ingredient) * ingredients_list[ingredient][attr] for ingredient in ingredients_list.keys()]) for attr in attributes[:-1]]
		else:
			score = [sum([recipe.count(ingredient) * ingredients_list[ingredient][attr] for ingredient in ingredients_list.keys()]) for attr in attributes]
		#If any of the properties have a negative total the result is 0 
		if calories_required and score[-1] != 500:
			score = 0
		elif any([s < 0 for s in score[:-1]]):
			score = 0
		else:
			if not calories_required:
				score = math.prod(score)
			else:
				score = math.prod(score[:-1])
		best_score = max(best_score, score)
	return best_score

print(f'Best Score without considering calories: {solution()} (Part One)')

print(f'Best Score with the constraint of 500 calories: {solution(calories_required=500)} (Part Two)')