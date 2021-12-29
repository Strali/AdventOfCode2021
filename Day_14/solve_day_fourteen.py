import os
import sys
sys.path.append(os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode_2021'))
from utils.read_aoc_input_file import read_aoc_input_file

from collections import Counter, defaultdict


print('Solving AoC 2021 day 14')
input = read_aoc_input_file(puzzle_day=14, return_as_string=True, test_input=False)

sequence = [c for c in input[0]]
rules = {k: v for k, v in [v.split(' -> ') for v in input[2:]]}

part_to_iteration_mapping = {1: 10, 2: 40}

for part, num_iterations in part_to_iteration_mapping.items():
    segment_count = Counter([''.join(sequence[i:i+2]) for i in range(len(sequence)-1)])
    element_count = Counter(sequence)

    for iter in range(num_iterations):
        tmp_segment_count = defaultdict(int)

        for seg, count in segment_count.items():
            element_to_add = rules.get(seg)
            if element_to_add:
                tmp_segment_count[seg[0]+element_to_add] += count
                tmp_segment_count[element_to_add+seg[1]] += count
                element_count[element_to_add] += count

        segment_count = tmp_segment_count

    print(f'Part {part}: {max(element_count.values())-min(element_count.values())}')

print('Done')
