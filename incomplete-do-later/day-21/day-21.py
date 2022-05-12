from functools import lru_cache

p1_wins = 0
p2_wins = 0

@lru_cache
def rec_game(one_score, one_sq, two_score, two_sq, i=1, board=[i for i in range(1, 11)]) -> int:
    one_sq = board[(one_sq+(i+(i+1)+(i+2))-1) % len(board)]
    one_score += one_sq
    i += 3
    if one_score >= 1000:
        return (i-1) * two_score
    two_sq = board[(two_sq+(i+(i+1)+(i+2))-1) % len(board)]
    two_score += two_sq
    i += 3
    if two_score >= 1000:
        return (i-1) * one_score


    return rec_game(one_score, one_sq, two_score, two_sq, i)
'''
@lru_cache
def quantum_dice(one_score, one_sq, two_score, two_sq, i=1) -> int:
    board = [i for i in range(1, 11)]
    p1_wins = 0
    p2_wins = 0
    memo = {}
    def rec_game(one_s, o_sq, two_s, t_sq, i=1, sequence=[]):
        o_sq = board[(o_sq+(i+(i+1)+(i+2))-1) % len(board)]
        one_s += one_sq
        i += 3
        if one_s >= 21 or two_s >= 21:
            r
        t_sq = board[(t_sq+(i+(i+1)+(i+2))-1) % len(board)]
        two_s += two_sq
        i += 3
        if two_s >= 1000:
            return (i-1) * one_score
'''