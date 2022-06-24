import re

with open('input', 'r') as f:
	puzzle_input = [ln.strip() for ln in f.readlines()]

class Bingo_Board():
    def __init__(self, board: list[list[int]]) -> None:
        self.board = board
        self.rows = [set(board[r]) for r in range(5)]
        self.cols = [set([board[r][c] for r in range(5)])for c in range(5)]
    
    def __repr__(self) -> str:
        return f'Rows: {self.rows}\nCols: {self.cols}'
    
    def check_if_winner(self, numbers_called: set[int]) -> int:
        for row_n, row, in enumerate(self.rows):
            if row.issubset(numbers_called):
                return row_n
        for col_n, col in enumerate(self.cols):
            if col.issubset(numbers_called):
                return col_n
        return -1
    
    def sum_of_unmarked_numbers(self, numbers_called: set[int]) -> int:
        return sum([self.board[r][c] for r in range(5) for c in range(5) 
                            if self.board[r][c] not in numbers_called])

NUMBERS_CALLED = [int(n.group()) for n in re.finditer(r'\d+', puzzle_input[0])]

boards = []
for i in range(2, len(puzzle_input), 6):
    new_board = []
    for ln in puzzle_input[i:i+5]:
        new_board.append([int(n.group()) for n in re.finditer(r'\d+', ln)])
    boards.append(Bingo_Board(new_board))

def part_one(boards: list[list[int]], NUMBERS_CALLED: list[int]) -> int:
    current_numbers = set(NUMBERS_CALLED[:4])

    for n in NUMBERS_CALLED[4:]:
        current_numbers.add(n)
        for board in boards:
            if board.check_if_winner(current_numbers) != -1:
                return board.sum_of_unmarked_numbers(current_numbers) * n

def part_two(boards: list[list[int]], NUMBERS_CALLED: list[int]) -> int:
    #final score of the last winning board
    current_numbers = set(NUMBERS_CALLED[:4])

    for n in NUMBERS_CALLED[4:]:
        current_numbers.add(n)
        for board in boards:
            if board.check_if_winner(current_numbers) != -1:
                if len(boards) == 1:
                    return board.sum_of_unmarked_numbers(current_numbers) * n
                boards.remove(board)

print(f'Part One: {part_one(boards, NUMBERS_CALLED)}')

print(f'Part Two: {part_two(boards, NUMBERS_CALLED)}')
