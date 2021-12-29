import os
import sys
sys.path.append(os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode_2021'))
from utils.read_aoc_input_file import read_aoc_input_file

from collections import deque
import numpy as np


print('Solving AoC 2021 day 10')
input = read_aoc_input_file(puzzle_day=10, return_as_string=True)

start_chars = ['(', '[', '{', '<']
end_char_map = {')': '(', ']': '[', '}': '{', '>': '<'}
start_char_map = {v: k for k, v in end_char_map.items()}
syntax_error_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

syntax_error_chars = []
corrupted_lines = []

for idx, line in enumerate(input):
    stack = deque()
    for char in line:
        if char in start_chars:
            stack.append(char)
        else:
            previous_char = stack.pop()

            if previous_char != end_char_map.get(char):
                syntax_error_chars.append(char)
                corrupted_lines.append(idx)
                break

print(f'Part 1: {sum([syntax_error_scores.get(e) for e in syntax_error_chars])}')

incomplete_lines = [line for idx, line in enumerate(input) if idx not in corrupted_lines]
completion_scores = {')': 1, ']': 2, '}': 3, '>': 4}
scores = []

for idx, line in enumerate(incomplete_lines):
    line_score = 0
    stack = deque()
    for char in line:
        if char in start_chars:
            stack.append(char)
        else:
            previous_char = stack.pop()

    end_sequence = []
    while stack:
        next_char = stack.pop()
        end_sequence.append(start_char_map.get(next_char))

    for char in end_sequence:
        line_score = 5*line_score + completion_scores.get(char)
    scores.append(line_score)

print(f'Part 2: {int(np.median(scores))}')

print('Done')
