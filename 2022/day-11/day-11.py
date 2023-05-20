import re
from Monkey import Monkey
from copy import deepcopy

with open('input', 'r') as f:
    puzzle_input = [ln.strip() for ln in f.readlines() if ln != '\n']


def parse_input(list: str) -> list[Monkey]:
    '''
        Return a list of Monkeys after parsing the input...
    '''
    monkeys: list[Monkey] = []

    for i in range(0, len(puzzle_input)-5, 6):
        starting_items: tuple[int] = [int(n) for n in re.findall(r'\d+', puzzle_input[i+1])]
        operation: str = re.search(r'old.+', puzzle_input[i+2]).group()
        divisor: int = int(re.search(r'\d+', puzzle_input[i+3]).group())
        throw: tuple[int] = tuple(int(n) for n in re.findall(r'\d+', puzzle_input[i+4]+puzzle_input[i+5]))

        monkeys.append(Monkey(starting_items, operation, divisor, throw))
    return monkeys

def throw_items(lst: list[tuple[int, int]], monkeys_list: list[Monkey]) -> list[Monkey]:
    for receiving, item in lst:
        monkeys_list[receiving].add_item(item)
    return monkeys_list

def calculate_monkey_business(monkeys_list) -> int:
    '''
        Calculated by multiplying the total inspections of the two monkeys with most
        inspections
    '''
    m = sorted(monkeys_list, key=lambda x: x.inspections, reverse=True)
    return m[0].inspections * m[1].inspections

'''
    Each round, have each monkey inspect all of its items
    and find the monkey each item should be thrown to
'''

def solve(m_list: list[Monkey], part: int=1) -> None:
    if part == 1:
        for round in range(20):
            for monkey in m_list:
                m_list = throw_items(monkey.find_throw_instructions(part), monkeys_list=m_list)
    elif part == 2:
        for round in range(10000):
            for monkey in m_list:
                monkeys_list = throw_items(monkey.find_throw_instructions(part), monkeys_list=m_list)

    print(f'Part {part}: {calculate_monkey_business(m_list)}')

monkeys_list = parse_input(puzzle_input)

solve(m_list=deepcopy(monkeys_list), part=1)
solve(m_list=deepcopy(monkeys_list), part=2)