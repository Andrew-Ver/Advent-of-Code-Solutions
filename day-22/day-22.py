from math import inf
from typing import Optional
from collections import defaultdict
import random
import re

with open('input') as f:
    boss_HP, boss_DMG = [int(n) for n in re.findall(r'\d+', ' '.join(f.readlines()))]

class Player():
    def __init__(self, hitpoints: int = 50, mana: int = 500, armour: int = 0):
        self.mana = mana
        self.armour = armour
        self.hitpoints = hitpoints
        self.recharge_turns = 0
        self.shield_turns = 0
        self.effects = set()
        self.available_spells = {
            'Magic Missile': defaultdict(lambda:0, {'mana': 53, 'damage': 4}),
            'Drain': defaultdict(lambda:0, {'mana': 73, 'damage': 2, 'heal': 2}),
            'Poison': defaultdict(lambda:0, {'mana': 173, 'turns': 6, 'damage': 3}),
            'Shield': defaultdict(lambda:0, {'mana': 113, 'turns': 6, 'armor': 7}),
            'Recharge': defaultdict(lambda:0, {'mana': 229, 'turns': 5, 'mana_per_turn': 101}),
        }
    def cast_spell(self, spell: str) -> dict[int]:
        return self.available_spells[spell]
    
    def is_dead(self) -> bool:
        return (self.hitpoints <= 0) or (self.mana <= 0)

    def update_buff_benefit(self) -> None:
        if self.recharge_turns:
            self.mana += 101
            self.recharge_turns -= 1
        if self.shield_turns:
            self.armour = 7
            self.shield_turns -= 1
        else:
            self.armour = 0
            self.effects = set()

    def enough_mana(self, spell: str) -> bool:
        return (self.mana - self.available_spells[spell]['mana'] >= 0)
        
class Boss():
    def __init__(self, hitpoints: int, damage: int):
        self.hitpoints = hitpoints
        self.damage = damage
        self.poisoned_turns = 0
        self.effects = set()

    def attack(self) -> int:
        return -self.damage

    def update_debuff_effect(self) -> None:
        if self.poisoned_turns:
            self.hitpoints -= 3
            self.poisoned_turns -= 1
        else:
            self.effects = set()

def battle_status(player: Player, boss: Boss) -> str:
    if player.is_dead():
        return 'Dead'
    elif boss.hitpoints <= 0:
        return 'Won'
    else:
        return None

lowest_mana_spent = float(+inf)

for _ in range(10000):
    player = Player()
    boss = Boss(hitpoints=boss_HP, damage=boss_DMG)
    mana_used_in_battle = 0

    while battle_status(player, boss) not in ['Dead' or 'Won']:
        def end_battle_conditions() -> bool:
            '''The battle ends either when one of the characters has died, or if the player hasn't won and has no mana for his spells on his turn
                The player could also win from poison damage on the boss before he has to choose a spell, and the boss can die on his turn from poison before
                he can attack
            '''
            return (battle_status(player, boss) in ['Dead' or 'Won']) or (mana_used_in_battle >= lowest_mana_spent)
        
        def player_and_boss_effects(p: Player, b: Boss) -> None:
            '''Uses up a "tick" of both character's effects, if any.'''
            p.update_buff_benefit()
            b.update_debuff_effect()

        player_and_boss_effects(player, boss)

        if end_battle_conditions():
            break
        try:
            # Choose a random spell for the playter to cast if its effects aren't active, and they have enough mana for it
            random_spell = random.choice([spell for spell in list(player.available_spells) if spell not in player.effects and spell not in boss.effects and player.enough_mana(spell)])
        except IndexError:
            #Player has run out of mana for any spells, and therefore lost
            break

        mana_used_in_battle += player.available_spells[random_spell]['mana']
        player.mana -= player.available_spells[random_spell]['mana']
        spell_stats = player.cast_spell(random_spell)
        player.hitpoints += spell_stats['heal']
        boss.hitpoints -= spell_stats['damage']

        if random_spell == 'Poison':
            boss.poisoned_turns += 6
            boss.effects.add('Poison')
        elif random_spell == 'Shield':
            player.shield_turns += 6
            player.effects.add('Shield')
        elif random_spell == 'Recharge':
            player.recharge_turns += 5
            player.effects.add('Recharge')
        
        player_and_boss_effects(player, boss)
        
        if end_battle_conditions():
            break
        
        # Boss's attack
        player.hitpoints -= max(1, (boss.attack() - player.armour))
        if end_battle_conditions():
            break
    
    if battle_status(player, boss) == 'Won':
        lowest_mana_spent = min(lowest_mana_spent, mana_used_in_battle)

print(f'Minimum mana spent to win: {lowest_mana_spent} (Part One)')

