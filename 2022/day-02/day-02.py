with open('input', 'r') as f:
    puzzle_input: list[tuple[str]] = [(ln.split()) for ln in f.readlines()]

shape_scores: dict = {a: b for a, b in zip('XYZ', range(1,4))}

'''
    Wins:
        rock vs paper
        paper vs scissors
        scissors vs rock
'''

def part_one(puzzle_input=puzzle_input, shape_scores=shape_scores) -> int:
    total_score: int = 0
    wins: set[tuple] = {('X', 'Y'), ('Y', 'Z'), ('Z', 'X')}

    for opp, you in puzzle_input:
        # convert to X, Y, Z for comparison
        opp = chr(ord(opp)+23)
        # tie
        if opp == you:
            total_score += 3
        # win
        elif (opp, you) in wins:
            total_score += 6
        # lose
        else:
            total_score += 0
        total_score += shape_scores[you]
    return total_score

def part_two(puzzle_input=puzzle_input) -> int:
    total_score: int = 0

    rps_dict: dict[dict] = {
        'X': {'X': 'Z', 'Y': 'X', 'Z': 'Y'},
        'Y': {'X': 'X', 'Y': 'Y', 'Z': 'Z'},
        'Z': {'X': 'Y', 'Y': 'Z', 'Z': 'X'},
    }

    '''
        For part two,
            X means you need to lose, Y means tie, and Z means win.
    '''

    g = {'X': 0, 'Y': 3, 'Z': 6}

    for opp, required in puzzle_input:
        opp = chr(ord(opp)+23)

        total_score += shape_scores[rps_dict[opp][required]]
        total_score += g[required]
    return total_score

print(f'PART ONE: {part_one()}')
print(F'PART TWO: {part_two()}')