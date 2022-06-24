import re
from itertools import permutations

with open ('input', 'r') as f:
    puzzle_input = f.readline().strip()

req_X_1, req_X_2, req_Y_1, req_Y_2 = [int(n) for n in re.findall(r'-?\d+', puzzle_input)]

def try_velocities(X_vel: int, Y_vel: int, req_A=req_X_1, req_B=req_X_2, req_C=req_Y_1, req_D=req_Y_2) -> bool:
    curr_X_Pos, curr_Y_Pos = 0, 0
    i = 0

    while True:
        curr_X_Pos += max(0, X_vel-i)
        curr_Y_Pos += (Y_vel-i)
        i += 1    
        if (req_A <= curr_X_Pos <= req_B) and (req_C <= curr_Y_Pos <= req_D):
            return True
        elif curr_X_Pos > req_B or curr_Y_Pos < req_C:
            return False

highest_Y = float('-inf')
count = 0

for x, y in permutations(range(-200, 201), 2):
    max_X, max_Y = (x*(x+1)//2), (y*(y+1)//2)
    if not (max_X < req_Y_1 or max_Y < req_Y_1) and not (x > req_X_2):
        result = try_velocities(x, y)
        if result:
            highest_Y = max(highest_Y, max_Y)
            count += 1

for x, y in ((i, i) for i in range(-200, 201)):
    result = try_velocities(x, y)
    if result:
        count += 1

print(f'Part One: {highest_Y}\nPart Two: {count}')


