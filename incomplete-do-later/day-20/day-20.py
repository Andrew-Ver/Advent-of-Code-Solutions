with open('input', 'r') as f:
    PUZZLE = [ln.strip() for ln in f.readlines() if ln]

enhancement_algorithm = PUZZLE[0]
input_image = [''.join(ln) for ln in PUZZLE[1:] if ln]
input_image = {(r, c) for r in range(len(input_image)) for c in range(len(input_image[0])) if input_image[r][c] == '#'}

def update_input_output_img(input_img: set[tuple[int, int]] = input_image, infinite_lights_on: bool = True) -> set[tuple[int, int]]:
    '''
        Go around the perimeter of the min/max rows and cols
    '''
    min_row, max_row = min(input_img, key=lambda x: x[0])[0], max(input_img, key=lambda x: x[0])[0]
    min_col, max_col = min(input_img, key=lambda x: x[1])[1], max(input_img, key=lambda x: x[1])[1]
    #print(f'Min row: {min_row} Max row: {max_row}\nMin col: {min_col} Max Col: {max_col}')
    def determine_output_pixel(r: int, c: int, input_img: set[int, int] = input_image) -> int:
        '''
            All pixels in the infinite grid surrounded by dots are "on" for the first iteration
            if the pixel (x, y) is outside of (min(rows)-1, max(rows)) it is assumed to be "on'
        '''
        rows = [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]
        binary = ''
        square_surrounded_by_nothing = all([(a, b) not in input_img for a, b in rows])
        #print(f'Square ({r})({c}) surrounded by nothing: {square_surrounded_by_nothing}')

        for x, y in rows:
            if square_surrounded_by_nothing:
                return -1
            elif (x, y) in input_img:
                binary += '1'
            elif not (min_row-1 < x < max_row+1) and not (min_col-1 < y < max_col+1):
                if infinite_lights_on:
                    binary += '1'
                else:
                    binary += '0'
            elif (x, y) not in input_img:
                binary += '0'

        return enhancement_algorithm[int(binary, 2)]

    new_img = set()
    for a in range(min_row-1, max_row+2):
        for b in range(min_col-1, max_col+2):
            if determine_output_pixel(a, b) == '#':
                new_img.add((a, b))
    return new_img

def print_grid(dot_coords = input_image) -> None:
    for r in range(-10, 15):
        print('\t\t\t',''.join(['#' if (r, c) in dot_coords else '.' for c in range(-10, 15)]))

print(f'Initial count: {len(input_image)}')

inf = True

for i in range(3):
    input_image = update_input_output_img(input_image, inf)
    if inf:
        inf = False
    elif not inf:
        inf = True
    print(i+1, len(input_image))
