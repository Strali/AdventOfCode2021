import os
import sys
sys.path.append(os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode_2021'))
from utils.read_aoc_input_file import read_aoc_input_file

import numpy as np


def get_rating_value(arr, mode='oxygen', idx=0):
    if len(arr) == 1:
        return arr
    else:
        unique, counts = np.unique(arr.T[idx], return_counts=True)
        if len(counts) == 1:
            keep_flag = unique[0]
        elif counts[0] == counts[1]:
            if mode == 'oxygen':
                keep_flag = 1
            else:
                keep_flag = 0
        else:
            if mode == 'oxygen':
                keep_flag = unique[np.argmax(counts)]
            else:
                keep_flag = unique[np.argmin(counts)]

        return get_rating_value(arr[arr[:, idx] == keep_flag], mode, idx+1)


print('Solving AoC 2021 day 3')
input = read_aoc_input_file(puzzle_day=3, return_as_string=True)

binary_array = np.array([[int(i) for i in binary_num] for binary_num in input])

gamma_value = []
epsilon_value = []
for column in binary_array.T:
    unique, counts = np.unique(column, return_counts=True)

    gamma_value.append(unique[np.argmax(counts)])
    epsilon_value.append(unique[np.argmin(counts)])

gamma_value = ''.join([str(v) for v in gamma_value])
epsilon_value = ''.join([str(v) for v in epsilon_value])

print(f'Part 1: {int(gamma_value, 2)*int(epsilon_value, 2)}')

oxygen_rating = get_rating_value(binary_array.copy(), 'oxygen', 0)
co_2_rating = get_rating_value(binary_array.copy(), 'co2', 0)

oxygen_rating = ''.join([str(v) for v in oxygen_rating[0]])
co_2_rating = ''.join([str(v) for v in co_2_rating[0]])

print(f'Part 2: {int(oxygen_rating, 2)*int(co_2_rating, 2)}')

print('Done')
