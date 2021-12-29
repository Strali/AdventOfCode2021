import os
import sys
sys.path.append(os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode_2021'))
from utils.read_aoc_input_file import read_aoc_input_file

import numpy as np


print('Solving AoC 2021 day 13')
input = read_aoc_input_file(puzzle_day=13, return_as_string=True, test_input=False)
input = [[int(v) for v in row.split(',')] for row in input]

instructions = read_aoc_input_file(puzzle_day=13, return_as_string=True, alternative_file_name='instructions')
instructions = [v.split(' ')[-1].split('=') for v in instructions]

max_x = max([v[0] for v in input])
max_y = max([v[1] for v in input])
paper = np.zeros((max_y+1, max_x+1))

for dot in input:
    x, y = dot
    paper[y][x] = 1

for i, instruction in enumerate(instructions):
    axis = instruction[0]
    location = int(instruction[1])
    if axis == 'y':
        top_half = paper[0:location, :]
        bottom_half = paper[location+1:, :]
        bottom_half = np.flipud(bottom_half)

        top_half[(top_half.shape[0]-bottom_half.shape[0]):, :] += bottom_half

        paper = np.clip(top_half, 0, 1)
    else:
        left_half = paper[:, 0:location]
        right_half = paper[:, location+1:]
        right_half = np.fliplr(right_half)

        left_half[:, (left_half.shape[1]-right_half.shape[1]):] += right_half
        paper = np.clip(left_half, 0, 1)

    if i == 0:
        print(f'Part 1: {int(np.sum(paper))}')

print(f'Part 2: {paper}')
print('Done')
