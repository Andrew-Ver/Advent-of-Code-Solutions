import re
from collections import defaultdict

with open('input', 'r') as f:
    puzzle_input = [re.findall(r'\S+', ln) for ln in f.readlines()]

curr_dir: list[str] = ['/']
folder_hierarchy: defaultdict(set) = defaultdict(int)

for ln in puzzle_input[1:]:
    if ln[0] == '$':
        cmd = ln[1]
        if len(ln) == 3:
            if ln[2] == '..':
                curr_dir.pop()
            else:
                curr_dir.append(ln[2])
    else:
        size, name = ln
        if size.isnumeric():
            # Loop through all folders above and add to their total size
            for i in range(len(curr_dir)):
                path: list[str] = curr_dir[:i+1]
                folder_hierarchy['/'.join(path)[1:]] += int(size)


# Find all folders with total size <= 100 000
PART_ONE: int = sum((size for size in folder_hierarchy.values() if size <= 100000))

print(f'Part One: {PART_ONE}.')

############
# Part Two #
############
'''
    Find the smallest directory that,
    if deleted, would free up enough space (total must be >= 30 000 000 free space) on the filesystem to run the update.
    What is the total size of that directory?
    (total diskspace is 70 000 000)
'''

additional_space_needed: int = (30000000 - (70000000 - folder_hierarchy['']))
smallest_folder_we_can_delete = float('inf')

for path, size in folder_hierarchy.items():
    if size >= additional_space_needed:
        smallest_folder_we_can_delete = min(size, smallest_folder_we_can_delete)

print(f'Part Two: {smallest_folder_we_can_delete}')