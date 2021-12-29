import os
import sys
sys.path.append(os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode_2021'))
from utils.read_aoc_input_file import read_aoc_input_file


print('Solving AoC 2021 day 2')
input = read_aoc_input_file(puzzle_day=2, return_as_string=True)

for part in [1, 2]:
    state = [0,0,0]  # Horizontal, depth, aim

    for instruction in input:
        direction, value = instruction.split(' ')

        if direction == 'forward':
            state[0] += int(value)
            if part == 2:
                state[1] += int(value)*state[2]

        elif direction == 'down':
            state[part] += int(value)

        elif direction == 'up':
            state[part] -= int(value)

    print(f'Part {part}: {state[0]*state[1]}')
