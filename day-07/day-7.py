import re
from collections import defaultdict

with open('input', 'r') as f:
	PUZZLE_INPUT = [ln.strip() for ln in f.readlines()]

def solution(initial_signals: dict = {}) -> dict[int]:
    wire_signals = defaultdict(lambda: None, initial_signals)
    completed = set() #Skip iterating over lines that were already completed
    iterations = 0
    while wire_signals['a'] == None:
        for ln in range(len(PUZZLE_INPUT)):
            if ln not in completed:
                command = re.search(r'(AND|LSHIFT|NOT|OR|RSHIFT)', PUZZLE_INPUT[ln])
                only_numeric_signal = re.search(r'^\d+', PUZZLE_INPUT[ln])
                ONE_AND_wire = re.search(r'^1\sAND\s[a-z]+', PUZZLE_INPUT[ln])
                sending_wires = re.findall(r'[a-z]{1,2}', ''.join(PUZZLE_INPUT[ln].split('->')[0]))
                receiving_wire = re.search(r'[a-z]{1,2}', ''.join(PUZZLE_INPUT[ln].split('->')[1])).group()

                if ONE_AND_wire:
                    if wire_signals[sending_wires[0]] != None:
                        wire_signals[receiving_wire] = (1 & wire_signals[sending_wires[0]])
                        completed.add(ln)
                
                elif not command and len(sending_wires) == 1 and wire_signals[sending_wires[0]] != None:
                    wire_signals[receiving_wire] = wire_signals[sending_wires[0]]
                    completed.add(ln)

                elif only_numeric_signal:
                    if receiving_wire not in initial_signals.keys():
                        wire_signals[receiving_wire] = int(only_numeric_signal.group())
                    completed.add(ln)

                elif command and all([True if (wire_signals[w] != None) else False for w in sending_wires ]):
                    command = command.group()
                    sending_wire_signals = [int(wire_signals[w]) for w in sending_wires]
                    if len(sending_wire_signals) == 2:
                        if command == 'AND':
                            wire_signals[receiving_wire] = sending_wire_signals[0] & sending_wire_signals[1]
                        elif command == 'OR':
                            wire_signals[receiving_wire] = sending_wire_signals[0] | sending_wire_signals[1]
                    if len(sending_wire_signals) == 1:
                        if command == 'NOT':
                            wire_signals[receiving_wire] =  ~sending_wire_signals[0] % 65536
                        elif command == 'LSHIFT':
                            n = int(re.search(r'\d+', PUZZLE_INPUT[ln]).group())
                            wire_signals[receiving_wire] = sending_wire_signals[0] << n
                        elif command == 'RSHIFT':
                            n = int(re.search(r'\d+', PUZZLE_INPUT[ln]).group())
                            wire_signals[receiving_wire] = sending_wire_signals[0] >> n
                    completed.add(ln)
                else:
                    for sw in sending_wires:
                        wire_signals[sw]
    return wire_signals

part_one_answer = solution()
print(f'Part One "a" wire: {part_one_answer["a"]}')

'''
Part Two:
Now, take the signal you got on wire a, override wire b to that signal, 
and reset the other wires (including wire a). 
What new signal is ultimately provided to wire a?
'''
print(f'Part Two "a" wire: {solution({"b": part_one_answer["a"]})["a"]}')
