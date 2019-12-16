from Helpers.intcode3 import parse_op3
from Helpers.helpers import read_newest_int_list

data = read_newest_int_list()
data_dict = dict(enumerate(data))
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
direction = 0

halt = False
idx = 0
x = 0
y = 0
output_final = {}  # Part 1
output_final = {(0, 0): 1}  # Part 2
spray = True
sprayed = set()
base = 0
while not halt:
    iterate = True
    while iterate:
        inpt = output_final.get((x, y), 0)
        data_dict, idx, iterate, inpt, _, output, halt, base = \
            parse_op3(data_dict, idx, iterate, inpt, None, None, base)
        if halt:
            break
    if spray and not halt:
        output_final[(x, y)] = output
        sprayed.add((x, y))
        spray = False
    elif not spray and not halt:  # Move
        spray = True
        if output == 0:
            direction = (direction-1) % 4
        else:
            direction = (direction+1) % 4
        x += directions[direction][0]
        y += directions[direction][1]
print(len(sprayed))  # Part 1

import pandas as pd
import numpy as np
x_min = min([x[0] for x in output_final.keys()])
y_min = min([x[1] for x in output_final.keys()])
x_max = max([x[0] for x in output_final.keys()])
y_max = max([x[1] for x in output_final.keys()])
output_graphics = pd.DataFrame(np.zeros((x_max-x_min, y_max-y_min)))
for location, color in output_final.items():
    output_graphics.at[location] = color

pass  # Read it from debugger :P
