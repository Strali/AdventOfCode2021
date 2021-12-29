import os
import sys
sys.path.append(os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode_2021'))
from utils.read_aoc_input_file import read_aoc_input_file

from itertools import compress
import numpy as np


print('Solving AoC 2021 day 5')
input = read_aoc_input_file(puzzle_day=5, return_as_string=True)

input_split = [v.split(' -> ') for v in input]
start_points = [[int(p) for p in v[0].split(',')] for v in input_split]
end_points = [[int(p) for p in v[1].split(',')] for v in input_split]
line_points = [z for z in zip(start_points, end_points)]

is_hv = [a[0][0] == a[1][0] or a[0][1] == a[1][1] for a in line_points]

hv_lines = list(compress(line_points, is_hv))
diagonal_lines = list(compress(line_points, [not v for v in is_hv]))

hotspots = np.zeros((np.max(np.asarray(hv_lines)), np.max(np.asarray(hv_lines))))

for line in hv_lines:
    if line[0][0] == line[1][0]:
        start_point = np.min([line[0][1], line[1][1]])
        end_point = np.max([line[0][1], line[1][1]]) + 1
        hotspots[line[0][0], start_point:end_point] += 1
    else:
        start_point = np.min([line[0][0], line[1][0]])
        end_point = np.max([line[0][0], line[1][0]]) + 1
        hotspots[start_point:end_point, line[0][1]] += 1

print(f'Part 1: {np.sum(hotspots > 1)}')

for line in diagonal_lines:
    if line[0][0] < line[1][0]:
        if line[0][1] < line[1][1]:
            intermediate_points = [[x, y] for x, y in zip(range(line[0][0],line[1][0]+1), range(line[0][1],line[1][1]+1))]
        else:
            intermediate_points = [[x, y] for x, y in zip(range(line[0][0],line[1][0]+1), range(line[0][1],line[1][1]-1, -1))]
    else:
        if line[0][1] < line[1][1]:
            intermediate_points = [[x, y] for x, y in zip(range(line[0][0],line[1][0]-1, -1), range(line[0][1],line[1][1]+1))]
        else:
            intermediate_points = [[x, y] for x, y in zip(range(line[1][0],line[0][0]+1), range(line[1][1],line[0][1]+1))]

    for point in intermediate_points:
        hotspots[point[0], point[1]] += 1

print(f'Part 2: {np.sum(hotspots > 1)}')

print('Done')
