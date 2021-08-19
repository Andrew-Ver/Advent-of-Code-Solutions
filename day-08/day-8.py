import re

with open('input', 'r') as f:
	contents = f.readlines()
	data = [ln.strip() for ln in contents]

WIDTH = 50; HEIGHT = 6

def part_one(instructions = data) -> int:
	pixels_on = set()

	for ins in instructions:
		A, B = list(map(int, re.findall(r'\d+', ins)))
		if ins.startswith('rect'):
			pixels = {(y,x) for x in range(A) for y in range(B)}
			pixels_on.update(pixels)

		elif ins.startswith('rotate row'):
			pix_row = [px for px in pixels_on if px[0] == A]
			new_pixels = set()
			for px in pix_row:
				Y, X = px
				new_pixels.add((Y, ((X+B)%WIDTH)))
			pixels_on.difference_update(pix_row)
			pixels_on.update(new_pixels)
			
		elif ins.startswith('rotate column'):	
			pix_col = [px for px in pixels_on if px[1] == A]
			new_pixels = set()
			for px in pix_col:
				Y, X = px
				new_pixels.add((((Y+B)%HEIGHT), X))
			pixels_on.difference_update(pix_col)
			pixels_on.update(new_pixels)
	#Part Two (EOARGPHYAO for my puzzle input)
	for Y in range(HEIGHT):
		row = []
		for X in range(WIDTH):
			if (Y, X) in pixels_on:
				row.append('#')
			else:
				row.append('.')
			row.append(' ')
		print(''.join(row))

	return len(pixels_on), 

print(f'Part One pixels on: {part_one()}')

