import os
import sys

from numpy.core.fromnumeric import size
sys.path.append(os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode_2021'))
from utils.read_aoc_input_file import read_aoc_input_file

from scipy.ndimage import convolve
import numpy as np


print('Solving AoC 2021 day 20')
input = read_aoc_input_file(puzzle_day=20, return_as_string=True, test_input=False)

enhancement_algorithm = input[0]
turn_on = np.array([i for i, v in enumerate(enhancement_algorithm) if v == '#'])
image = np.array([[int(v=='#') for v in line] for line in input[2:]])

total_iterations = 50  # For part 2 as well
image = np.pad(image, total_iterations)

weights = np.array([[1, 2, 4], [8, 16, 32], [64, 128, 256]])
# Determine how to handle the "infinite grid"
if enhancement_algorithm[0] == '.':
    cval = lambda x: (x+1) % 2
else:
    cval = lambda x: x % 2

for i in range(total_iterations):
    tmp_image = convolve(image, weights, mode='constant', cval=cval(i))
    image = np.isin(tmp_image, turn_on).astype(int)

    if i == 1:
        print(f'Part 1: {np.sum(image)}')

print(f'Part 2: {np.sum(image)}')
