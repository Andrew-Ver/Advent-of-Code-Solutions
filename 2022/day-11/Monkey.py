from collections import deque

class Monkey:
    ID = 0
    divisor_product: int = 1

    def __init__(self, held_items: list[int], operation: str, divisor: int, throw: tuple[int]) -> None:
        self.ID = Monkey.ID
        Monkey.ID += 1
        self.inspections: int = 0
        self.held_items: deque[int] = deque(held_items)
        self.operation: str = operation
        self.divisor = divisor
        Monkey.divisor_product *= divisor
        self.throw: tuple[int] = tuple(throw)

    def __repr__(self) -> str:
        return f'Monkey {self.ID} currently holding: {self.held_items}, with {self.inspections} total item inspections.'

    def find_throw_instructions(self, part) -> list[tuple[int, int]]:
        '''
            Returns a list of tuples of (monkey_to_throw_to: int, new_worry_level: int)
        '''
        throw_list: list[tuple[int, int]] = []

        def determine_monkey(item: int) -> int:
            '''
                Return number of monkey the item should be thrown to.
            '''
            if (item == 0) or not (item % self.divisor):
                return self.throw[0]
            return self.throw[1]

        while self.held_items:
            old = self.held_items.popleft()
            # Use eval() to find new "worry level"... unsafe usually
            # but is fine here due to known input
            new = eval(self.operation)

            # don't divide by 3 and round down if Part 2...
            if part == 1:
                new = int(new/3)

            new %= Monkey.divisor_product
            throw_list.append((determine_monkey(new), new))
            self.inspections += 1

        return throw_list

    def add_item(self, item: int) -> None:
        self.held_items.append(item)

if __name__ == '__main__':
    pass