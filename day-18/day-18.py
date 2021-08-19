with open('input', 'r') as f:
	contents = f.readlines()
	data = [ln.strip() for ln in contents]

trap_tiles = {(0, X) for X in range(len(data[0])) if data[0][X] == '^'}

def new_row_traps(tile_row: int, trap_tiles=trap_tiles) -> set:
	# Returns a set of traps present for a new row
	new_trap_row = set()
	for pos in range(0, len(data[0])):
		tiles_to_check = [pos-1, pos, pos+1]
		traps_present  = [] 
		for prev_tile in tiles_to_check:
			if (tile_row-1, prev_tile) in trap_tiles:
				traps_present.append(True)
			else:
				traps_present.append(False)
		LEFT, CENTER, RIGHT = traps_present
		if (LEFT and CENTER and not RIGHT) or (not LEFT and CENTER and RIGHT) or (LEFT and not CENTER and not RIGHT) or (not LEFT and not CENTER and RIGHT):
			new_trap_row.add((tile_row, pos))
	return new_trap_row

PART_ONE_ROWS = 40
PART_TWO_ROWS = 400000

for tile_row in range(1, PART_TWO_ROWS):
	if tile_row == PART_ONE_ROWS:
		print(f'Total Safe Tiles: {PART_ONE_ROWS*100-len(trap_tiles)} (Part One)')
	trap_tiles.update(new_row_traps(tile_row))

print(f'Total Safe Tiles: {PART_TWO_ROWS*100-len(trap_tiles)} (Part Two)')