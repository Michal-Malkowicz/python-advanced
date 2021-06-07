import itertools


def read_input(fileanme) -> list:
    with open(fileanme, 'r') as read_file:
        cube = [[element for element in line.strip()] for line in read_file.readlines()]
    return cube


def create_empty_cube(x_size: int, y_size: int, z_size: int) -> list:
    # kreator putego obiektu
    return [[['.' for _ in range(xy_size)] for _ in range(xy_size)] for _ in range(z_size)]


def inject_initial_layer(initial_layer, cube):
    for y in range(len(initial_layer[0])):
        for x in range(len(initial_layer[0][0])):
            cube[cycles][cycles + y][cycles + x] = initial_layer[0][y][x]


# przygotowanie zmiennych setup:
cycles = 6
initial_layer = read_input('input.txt')
xy_size = cycles*2 + len(initial_layer)
z_size = cycles*2 + 1

unit_vector = [-1, 0, 1]

# tworzymy dwa razy obiekt bo kopiowanie zmeinnych przekazuje referencje i edycja edytuje oryginal
new_cube = create_empty_cube(xy_size, xy_size, z_size)
copy_cube = create_empty_cube(xy_size, xy_size, z_size)

inject_initial_layer(initial_layer, new_cube)
inject_initial_layer(initial_layer, copy_cube)

#for x, y, z in itertools.product(x):



print(new_cube)


