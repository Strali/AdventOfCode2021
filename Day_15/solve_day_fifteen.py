import os
import sys

from numpy.core.fromnumeric import size
sys.path.append(os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode_2021'))
from utils.read_aoc_input_file import read_aoc_input_file

from heapq import heappop, heappush
import numpy as np


class GridUtils():
    def __init__(self, grid, size_factor):
        self.height = grid.shape[0]
        self.width = grid.shape[1]
        self.size_factor = size_factor

    def _test_within_bounds(self, location):
        y, x = location
        return 0 <= x < self.width*self.size_factor and 0 <= y < self.height*self.size_factor

    def get_valid_neighbours(self, location):
        y, x = location
        neighbour_locations = [(y, x+1), (y, x-1), (y-1, x), (y+1, x)]

        return  [v for v in neighbour_locations if self._test_within_bounds(v)]


print('Solving AoC 2021 day 15')
input = read_aoc_input_file(puzzle_day=15, return_as_string=True, test_input=False)
grid = np.array([[int(c) for c in row] for row in input])

part_to_size_mapping = {1: 1, 2: 5}

start_node = (0, 0)

for part, cave_size in part_to_size_mapping.items():

    grid_utils = GridUtils(grid, cave_size)
    end_node = (grid.shape[0]*cave_size-1, grid.shape[1]*cave_size-1)

    visited = {start_node}
    risk_to_loc = {start_node: 0}
    path_heap = [(0, start_node)]

    while path_heap:
        risk, location = heappop(path_heap)

        if location == end_node:
            break

        neighbours = grid_utils.get_valid_neighbours(location)
        for loc in neighbours:
            sup_row, sub_row = divmod(loc[0], grid_utils.height)
            sup_col, sub_col = divmod(loc[1], grid_utils.width)

            current_risk = risk + (grid[(sub_row, sub_col)] + sup_row + sup_col - 1) % 9 + 1
            if current_risk < risk_to_loc.get(loc, np.inf):
                risk_to_loc[loc] = current_risk

            if loc not in visited:
                heappush(path_heap, (current_risk, loc))
                visited.add(loc)


    print(f'Part {part}: {risk_to_loc.get(end_node)}')
