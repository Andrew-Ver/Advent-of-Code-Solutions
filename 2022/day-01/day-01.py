most_calories: int = 0
top_three_elves: list[int] = []

with open('input', 'r') as f:
    curr_calories: int = 0
    for ln in f.readlines():
        if ln != '\n':
            curr_calories += int(ln)
        else:
            most_calories = max(curr_calories, most_calories)
            if len(top_three_elves) == 3 and top_three_elves[-1] < curr_calories:
                top_three_elves.pop()
                top_three_elves.append(curr_calories)
                top_three_elves.sort(reverse=True)
            elif len(top_three_elves) < 3:
                top_three_elves.append(curr_calories)
                top_three_elves.sort(reverse=True)
            curr_calories = 0
    # Handle last one
    most_calories = max(most_calories, curr_calories)
    if len(top_three_elves) == 3 and top_three_elves[-1] < curr_calories:
        top_three_elves.pop()
        top_three_elves.append(curr_calories)


print(f'Part One: {most_calories}')
print(f'Part Two: {sum(top_three_elves)}')