import os
import sys
sys.path.append(os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode_2021'))
from utils.read_aoc_input_file import read_aoc_input_file

import numpy as np


print('Solving AoC 2021 day 1')
input = read_aoc_input_file(puzzle_day=1, return_as_string=False)

for i, window_size in enumerate([1, 3]):
    part_answer = np.sum(np.diff(np.convolve(input, np.ones(window_size, dtype=int), 'valid')) > 0)
    print(f'Part {i+1}: {part_answer}')
