with open('input', 'r') as f:
	puzzle_input = [line.strip() for line in f.readlines()]

#Part One 
gamma_rate = [[puzzle_input[r][i] for r in range(len(puzzle_input))] for i in range(len(puzzle_input[0]))]
epsilon_rate = [['1' if i == '0' else '0' for i in ln] for ln in gamma_rate]
gamma_rate = int(''.join([max(ln, key = lambda x: ln.count(x)) for ln in gamma_rate]), 2)
epsilon_rate = int(''.join([max(ln, key = lambda x: ln.count(x)) for ln in epsilon_rate]), 2)

print(f'Part One: {gamma_rate * epsilon_rate}')

#Part Two
def oxygen_genrator_rating(report: list[int]) -> tuple[int, int]:
    most_common_bits = []
    possible = report
    for c in range(len(report[0])):
        zeroes = 0
        ones = 0
        nums_with_ones_bit = []
        nums_with_zeroes_bit = []
        for r in range(len(possible)):
            if possible[r][c] == '0':
                zeroes += 1
                nums_with_zeroes_bit.append(possible[r])
            else:
                ones += 1
                nums_with_ones_bit.append(possible[r])
        if zeroes > ones:
            most_common_bits.append('0')
            possible = nums_with_zeroes_bit
        else:
            most_common_bits.append('1')
            possible = nums_with_ones_bit

        if len(possible) == 1:
            return int(''.join(possible[0]), 2)
    
def co2_scrubber_rating(report: list[int]) -> tuple[int, int]:
    least_common_bits = []
    possible = report
    for c in range(len(report[0])):
        zeroes = 0
        ones = 0
        nums_with_ones_bit = []
        nums_with_zeroes_bit = []
        for r in range(len(possible)):
            if possible[r][c] == '0':
                zeroes += 1
                nums_with_zeroes_bit.append(possible[r])
            else:
                ones += 1
                nums_with_ones_bit.append(possible[r])
        if zeroes <= ones:
            least_common_bits.append('0')
            possible = nums_with_zeroes_bit
        elif ones < zeroes:
            least_common_bits.append('1')
            possible = nums_with_ones_bit
        
        if len(possible) == 1:
            return int(''.join(possible[0]), 2)

print(f'Part Two: {oxygen_genrator_rating(puzzle_input) * co2_scrubber_rating(puzzle_input)}')
