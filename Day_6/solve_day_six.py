import os
import sys
sys.path.append(os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode_2021'))
from utils.read_aoc_input_file import read_aoc_input_file

from collections import Counter, defaultdict

print('Solving AoC 2021 day 6')
input = read_aoc_input_file(puzzle_day=6, return_as_string=False)

n_iterations = [80, 256]

for part, iters in enumerate(n_iterations):
    fish_state = dict(Counter(input))

    for iter in range(0, iters):
        new_state = defaultdict(int)
        for k, v in fish_state.items():
            if k == 0:
                new_state[8] = v
                new_state[6] += v
            else:
                new_state[k-1] += v

        fish_state = new_state

    print(f'Part {part+1}: {sum([v for v in fish_state.values()])}')

print('Done')
