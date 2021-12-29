import os
import sys
sys.path.append(os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode_2021'))
from utils.read_aoc_input_file import read_aoc_input_file

import numpy as np

print('Solving AoC 2021 day 4')
input = read_aoc_input_file(puzzle_day=4, return_as_string=False)
boards_raw = read_aoc_input_file(puzzle_day=4, return_as_string=True, alternative_file_name='boards')

clean_boards = []
current_board = []
for line in boards_raw:
    if line == '':
        clean_boards.append(current_board)
        current_board = []
    else:
        current_board.append([int(v.strip()) for v in line.split(' ') if v.strip()])

boards = np.array(clean_boards)
winning_board_idx = -1

for num in input:
    boards[boards==num] = -1

    for idx, board in enumerate(boards):
        if any(np.sum(board, axis=0) == -5) or any(np.sum(board, axis=1) == -5):
            winning_board_idx = idx
            break
    if winning_board_idx >= 0:
        break

winning_board = boards[winning_board_idx]
print(f'Part 1: {np.sum(winning_board[np.where(winning_board >= 0)])*num}')

boards = np.array(clean_boards)
for num in input:
    boards[boards==num] = -1

    idx_to_delete = []
    for idx, board in enumerate(boards):

        if any(np.sum(board, axis=0) == -5) or any(np.sum(board, axis=1) == -5):
            winning_board_idx = idx

            last_winning_board_state = board
            idx_to_delete.append(idx)
    if idx_to_delete:
        boards = np.delete(boards, idx_to_delete, axis=0)
    if len(boards) == 0:
        break

print(f'Part 2: {np.sum(last_winning_board_state[np.where(last_winning_board_state >= 0)])*num}')

print('Done')
