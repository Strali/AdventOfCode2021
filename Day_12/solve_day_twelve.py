import os
import sys
sys.path.append(os.path.join('C:/', 'Users', 'andre', 'Documents', 'AdventOfCode_2021'))
from utils.read_aoc_input_file import read_aoc_input_file

from collections import defaultdict, deque


def DFS_one_visit(graph, start_node='start', end_node='end'):

    node_stack = deque([(start_node, {start_node})])  # (current_node, visited_nodes)
    path_count = 0

    while node_stack:
        current_node, visited_nodes = node_stack.pop()

        if current_node == end_node:
            path_count += 1
            continue

        for vertex in graph.get(current_node):
            if vertex in visited_nodes and vertex.islower():
                continue
            else:
                node_stack.append((vertex, visited_nodes | {vertex}))

    return path_count


def DFS_single_revisit(graph, start_node='start', end_node='end'):

    node_stack = deque([(start_node, {start_node}, False)])  # (current_node, visited_nodes, revisit)
    path_count = 0

    while node_stack:
        current_node, visited_nodes, already_revisited = node_stack.pop()

        if current_node == end_node:
            path_count += 1
            continue

        for vertex in graph.get(current_node):
            if vertex not in visited_nodes or vertex.isupper():
                node_stack.append((vertex, visited_nodes | {vertex}, already_revisited))
                continue
            elif already_revisited or vertex == 'start':
                continue
            else:
                node_stack.append((vertex, visited_nodes | {vertex}, True))

    return path_count


print('Solving AoC 2021 day 12')
input = read_aoc_input_file(puzzle_day=12, return_as_string=True,
                            test_input=False)

cave_graph = defaultdict(list)
for edge in input:
    start_node, end_node = edge.split('-')
    cave_graph[start_node].append(end_node)
    cave_graph[end_node].append(start_node)

print(f'Part 1: {DFS_one_visit(cave_graph)}')
print(f'Part 2: {DFS_single_revisit(cave_graph)}')
