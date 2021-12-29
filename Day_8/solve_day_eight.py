import os
import sys
sys.path.append(os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode_2021'))
from utils.read_aoc_input_file import read_aoc_input_file


def overlap(d1, d2):
    return len(set(d1) & set(d2))


def get_initial_digit_mapping(digits):
    segment_to_digit_map = dict()
    for digit_segment in digits:
        if len(digit_segment) == 2:
            segment_to_digit_map[1] = ''.join(sorted(digit_segment))
        elif len(digit_segment) == 3:
            segment_to_digit_map[7] = ''.join(sorted(digit_segment))
        elif len(digit_segment) == 4:
            segment_to_digit_map[4] = ''.join(sorted(digit_segment))
        elif len(digit_segment) ==7:
            segment_to_digit_map[8] = ''.join(sorted(digit_segment))

    return segment_to_digit_map


def map_segments_to_digits(digits):

    segment_to_digit_map = get_initial_digit_mapping(digits)

    for digit_segment in digits:
        if digit_segment in segment_to_digit_map.values():
            continue

        if len(digit_segment) == 6:
            if overlap(digit_segment, segment_to_digit_map.get(7)) == 3 and \
                overlap(digit_segment, segment_to_digit_map.get(4)) == 4:
                segment_to_digit_map[9] = ''.join(sorted(digit_segment))
            elif overlap(digit_segment, segment_to_digit_map.get(8)) == 6 and \
                overlap(digit_segment, segment_to_digit_map.get(4)) == 3 and \
                overlap(digit_segment, segment_to_digit_map.get(1)) == 2:
                segment_to_digit_map[0] = ''.join(sorted(digit_segment))
            else:
                segment_to_digit_map[6] = ''.join(sorted(digit_segment))

        elif len(digit_segment) == 5:
            if overlap(digit_segment, segment_to_digit_map.get(7)) == 3:
                segment_to_digit_map[3] = ''.join(sorted(digit_segment))
            elif overlap(digit_segment, segment_to_digit_map.get(4)) == 3:
                 segment_to_digit_map[5] = ''.join(sorted(digit_segment))
            else:
                segment_to_digit_map[2] = ''.join(sorted(digit_segment))

    return segment_to_digit_map


def map_sequence_to_number(segment_sequence, segment_to_digit_map):
    numbers_as_str = [str(segment_to_digit_map.get(''.join(sorted(k)))) for k in segment_sequence]
    return int(''.join(numbers_as_str))

print('Solving AoC 2021 day 8')
input = read_aoc_input_file(puzzle_day=8, return_as_string=True)

input_values = [i.split(' | ')[0] for i in input]
output_values = [i.split(' | ')[1] for i in input]
input_digits = [v.split(' ') for v in input_values]
output_digits = [v.split(' ') for v in output_values]

unique_segment_counts = [2, 3, 4, 7]  # 1, 7, 4, 8
segments_per_digit = [[int(len(d) in unique_segment_counts) for d in seg] for seg in output_digits]
unique_segment_number_digits = sum([sum(d) for d in segments_per_digit])

print(f'Part 1: {unique_segment_number_digits}')

output_values = []
for idx, input_segments in enumerate(input_digits):
    digit_to_segment_map = map_segments_to_digits(input_segments)
    segment_to_digit_map = {v: k for k, v in digit_to_segment_map.items()}

    output_values.append(map_sequence_to_number(output_digits[idx], segment_to_digit_map))

print(f'Part 2: {sum(output_values)}')

print('Done')
