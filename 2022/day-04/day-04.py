import re

part_one: int = 0
part_two: int = 0

with open('input', 'r') as f:
    for elf_A1, elf_A2, elf_B1, elf_B2 in [(int(n) for n in re.findall(r'\d+', ln)) for ln in f.readlines()]:
        if (elf_A1 <= elf_B1 and (elf_B2 <= elf_A2)) or ((elf_B1 <= elf_A1) and (elf_A2 <= elf_B2)):
            part_one += 1
        # if any overlaps for part 2
        if (elf_A1 <= elf_B1 <= elf_A2) or (elf_B1 <= elf_A1 <= elf_B2):
            part_two += 1

print(f'Part One: {part_one}\nPart Two: {part_two}')