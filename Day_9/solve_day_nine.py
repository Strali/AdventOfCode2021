import os
import sys
sys.path.append(os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode_2021'))
from utils.read_aoc_input_file import read_aoc_input_file

import numpy as np
from skimage.measure import label, regionprops


def local_minima(array2d):
    return ((array2d < np.roll(array2d,  1, 0)) &
            (array2d < np.roll(array2d, -1, 0)) &
            (array2d < np.roll(array2d,  1, 1)) &
            (array2d < np.roll(array2d, -1, 1)))


print('Solving AoC 2021 day 9')
input = read_aoc_input_file(puzzle_day=9, return_as_string=True)
height_map = np.pad(np.array([[int(num) for num in row] for row in input]),
                    pad_width=1, mode='constant', constant_values=9)

hotspots = height_map[local_minima(height_map)]

print(f'Part 1: {sum(hotspots) + len(hotspots)}')

basin_map = height_map.copy()
basin_map[basin_map < 9] = 0

labels = label(basin_map, background=9, connectivity=1)
props = regionprops(labels)
basin_sizes = sorted([basin.area for basin in props])
largest_basins = basin_sizes[-3:]

print(f'Part 2: {np.prod(largest_basins)}')

print('Done')
