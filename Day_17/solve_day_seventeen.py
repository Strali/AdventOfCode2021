import os
import sys

from numpy.core.fromnumeric import size
sys.path.append(os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode_2021'))
from utils.read_aoc_input_file import read_aoc_input_file

import numpy as np


print('Solving AoC 2021 day 17')
input = read_aoc_input_file(puzzle_day=17, return_as_string=True, test_input=False)
min_x, max_x = [int(v) for v in input[0].split(', ')]
min_y, max_y = [int(v) for v in input[1].split(', ')]

max_y_vel_to_hit = np.abs(min_y) - 1  # Since y-velocity is -vy_0 at y=0
print(f'Part 1: {int((max_y_vel_to_hit) * (max_y_vel_to_hit + 1)/2)}')

target_hits = 0
for vx_0 in range(1, max_x+1):
    for vy_0 in range(min_y, np.abs(min_y)):
        x, y = 0, 0
        vx = vx_0
        vy = vy_0

        while x <= max_x and y >= min_y:

            if x >= min_x and y <= max_y:
                target_hits += 1
                break

            x += vx
            y += vy

            if vx > 0:
                vx -= 1
            vy -= 1

print(f'Part 2: {target_hits}')
