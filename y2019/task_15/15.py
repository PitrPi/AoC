from copy import deepcopy

from Helpers.helpers import read_newest_int_list
from Helpers.intcode3 import parse_op3
from random import randint
data = read_newest_int_list()

data_dict = dict(enumerate(data))
halt = False
idx = 0
base = 0
x = 0
y = 0
map_draw = {(0, 0): '.'}
move_coms = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
path = [0]
output = None
while output != 2:
    iterate = True
    inpt = randint(1, 4)
    # while map_draw.get((x, y), 0) == '.':
    x, y = x+move_coms[inpt][0], y+move_coms[inpt][1]
    path.append(inpt)
    while iterate:
        data_dict, idx, iterate, _, _, output, halt, base = \
            parse_op3(data_dict, idx, iterate, inpt, None, None, base)
    if output == 0:
        map_draw[(x, y)] = '#'
        x, y = x - move_coms[inpt][0], y - move_coms[inpt][1]
        path.pop()
    elif output == 1:
        map_draw[(x, y)] = '.'
        if path[-2] + inpt == 3 or path[-2] + inpt == 7:
            path.pop()
            path.pop()
    elif output == 2:
        map_draw[(x, y)] = 'O'
print(len(path)-1)
import pandas as pd
map_pandas = pd.DataFrame(index=range(-30, 30), columns=range(-30,30))
for k, v in map_draw.items():
    map_pandas.at[k] = v

# Part 2
print("Part 2")
counter = 0
while '.' in map_draw.values():
    counter += 1
    map_draw_copy = deepcopy(map_draw)
    for k, v in map_draw.items():
        if v == 'O':
            if map_draw.get((k[0]-1, k[1]), 0) == ".":
                map_draw_copy[(k[0]-1, k[1])] = "O"
            if map_draw.get((k[0]+1, k[1]), 0) == ".":
                map_draw_copy[(k[0]+1, k[1])] = "O"
            if map_draw.get((k[0], k[1]-1), 0) == ".":
                map_draw_copy[(k[0], k[1]-1)] = "O"
            if map_draw.get((k[0], k[1]+1), 0) == ".":
                map_draw_copy[(k[0], k[1]+1)] = "O"
    map_draw = map_draw_copy

print(counter)
pass