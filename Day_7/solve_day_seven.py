import os
import sys
sys.path.append(os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode_2021'))
from utils.read_aoc_input_file import read_aoc_input_file

import numpy as np


print('Solving AoC 2021 day 7')
input = read_aoc_input_file(puzzle_day=7, return_as_string=False)

for part in [1, 2]:
    min_fuel = 10e12
    min_pos = -1

    for pos in range(0, np.max(input)):
        if part == 1:
            fuel_consumption = np.sum([np.abs(v-pos) for v in input])
        else:
            fuel_consumption = np.sum([np.abs(v-pos)*(np.abs(v-pos)+1)/2 for v in input])

        if fuel_consumption < min_fuel:
            min_fuel = fuel_consumption
            min_pos = pos

    print(f'Part {part}: {int(min_fuel)} (at {min_pos})')

print('Done')
