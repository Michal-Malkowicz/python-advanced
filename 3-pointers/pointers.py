
#def read_data(filename: str) -> list:
#    file = open(filename, 'r').read()
#    return file.split()
#
#
#lines = read_data('input.txt')
#
#pointer, trees = 0, 0
#for line in lines:
#    if (pointer + 3) >= len(line):
#        pointer = pointer % len(line)
#    if line[pointer] == '#':
#        trees += 1
#    pointer += 3
#
#print(trees)

import os
import logging


def read_data(filename: str) -> list:
    # skleja input z wywolywanym plikiem
    input_path = os.path.abspath(os.path.join(os.path.dirname(__file__), filename))
    file = open(input_path, 'r').read()
    return file.split()


def count_trees(tree_map, step_x, step_y):
    x_len, y_len = len(tree_map[0]), len(tree_map)
    pointer_x, pointer_y = 0, 0

    num_of_trees = 0

    for pointer_y in range(0, y_len, step_y):
        if tree_map[pointer_y][pointer_x % x_len] == '#':
            num_of_trees += 1
        pointer_x += step_x
    return num_of_trees





tree_map = read_data('input.txt')
step_x, step_y = 3, 1
print(count_trees(tree_map, step_x, step_y))

move_schema = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

result = 1
for step in move_schema:
    result *= count_trees(tree_map, *step)
print(result)

message_format = '%(asctime)s: %(message)s'
logging.basicConfig(format=message_format, level=logging.DEBUG, datefmt='%H:%M:%S')

logging.info(f'Total number of trees {result}')
logging.debug(f'Total number of trees {result}')
logging.warning(f'Total number of trees {result}')
