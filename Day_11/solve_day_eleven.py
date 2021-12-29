import os
import sys
sys.path.append(os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode_2021'))
from utils.read_aoc_input_file import read_aoc_input_file

from itertools import product
import numpy as np


print('Solving AoC 2021 day 11')
input = read_aoc_input_file(puzzle_day=11, return_as_string=False, test_input=False)

energy_levels = np.array([[int(v) for v in str(line)] for line in input])

flash_count = 0
num_steps = 0

while True:
    energy_levels += 1
    already_flashed = np.zeros(energy_levels.shape)

    next_to_flash = [[row, col] for [row, col] in product(range(0, energy_levels.shape[0]), range(0, energy_levels.shape[1])) if energy_levels[row][col] > 9]

    while next_to_flash:
        next_round = []
        for next_flash in next_to_flash:
            r, c = next_flash
            if already_flashed[r][c]:
                continue

            for i in range(-1, 2):
                for j in range(-1, 2):
                    row = r + i
                    col = c + j
                    if row == r and col == c:
                        energy_levels[row][col] = 0
                    elif row < 0 or row > 9 or col < 0 or col > 9:
                        continue
                    elif already_flashed[row][col] == 1:
                        continue
                    else:
                        energy_levels[row][col] += 1
                        if energy_levels[row][col] > 9 and already_flashed[row][col] == 0:
                            next_round.append([row, col])

            already_flashed[r][c] = 1
            flash_count += 1

        next_to_flash = next_round

    num_steps += 1
    if num_steps == 100:
        print(f'Part 1: {flash_count}')
    elif num_steps > 10000:
        print('More than 10000 steps')
        break

    if np.sum(energy_levels) == 0:
        print(f'Part 2: {num_steps}')
        break

print('Done')
