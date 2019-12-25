from Helpers.helpers import read_newest_int_list
from Helpers.intcode3 import parse_op3

data = read_newest_int_list()
data_dict = dict(enumerate(data))
out = {}
x = 0
y = 0
idx = 0
base = 0
halt = False

while not halt:
    iterate = True
    inpt = None
    output = None
    while iterate:
        data_dict, idx, iterate, _, _, output, halt, base = \
            parse_op3(data_dict, idx, iterate, inpt, None, None, base)
        if halt:
            break
    if output == 10:
        x = 0
        y += 1
    else:
        out[(x, y)] = output
        x += 1

res = 0
for k, v in out.items():
    if v != 46:
        if (out.get((k[0]+1, k[1]), 46) != 46 and
                out.get((k[0], k[1]+1), 46) != 46 and
                out.get((k[0]-1, k[1]), 46) != 46 and
                out.get((k[0], k[1]-1), 46) != 46):
            res += k[0]*k[1]
print(res)

pass



# move up
def move_u(path, robot_x, robot_y):
    moved = False
    while out.get((robot_x, robot_y + 1), 46) != 46:
        moved = True
        path.append('^')
        robot_y += 1
    return path, robot_x, robot_y, moved
# move right
def move_r(path, robot_x, robot_y):
    moved = False
    while out.get((robot_x + 1, robot_y), 46) != 46:
        moved = True
        path.append('>')
        robot_x += 1
    return path, robot_x, robot_y, moved
# move down
def move_d(path, robot_x, robot_y):
    moved = False
    while out.get((robot_x, robot_y - 1), 46) != 46:
        moved = True
        path.append('v')
        robot_y -= 1
    return path, robot_x, robot_y, moved
# move left
def move_l(path, robot_x, robot_y):
    moved = False
    while out.get((robot_x - 1, robot_y), 46) != 46:
        moved = True
        path.append('<')
        robot_x -= 1
    return path, robot_x, robot_y, moved


# Find path for Part 2
path = []
# Find cleaning robot
for k, v in out.items():
    if v != 46 and v != 35 and v is not None:  # it is not # or .
        robot_x, robot_y = k
        if v == 94:
            last_move = 'u'
end = False
# Main logic
while not end:
    if last_move == 'u' or last_move == 'd':
        path, robot_x, robot_y, moved = move_l(path, robot_x, robot_y)
        if moved is False:
            path, robot_x, robot_y, moved = move_r(path, robot_x, robot_y)
            if moved is False:
                print("Dead-end at", str(robot_x), str(robot_y))
                end = True
            else:
                last_move = 'r'
        else:
            last_move = 'l'
    else:
        path, robot_x, robot_y, moved = move_u(path, robot_x, robot_y)
        if moved is False:
            path, robot_x, robot_y, moved = move_d(path, robot_x, robot_y)
            if moved is False:
                print("Dead-end at", str(robot_x), str(robot_y))
                end = True
            else:
                last_move = 'd'
        else:
            last_move = 'u'
print(path)
nu = 1
for idx, mov in enumerate(path):
    if idx > 0:
        if path[idx] == path[idx-1]:
            nu += 1
        else:
            print(path[idx-1], nu)
            nu = 1

import pandas as pd
pd_out = pd.DataFrame(index=range(45), columns=range(45))
for k, v in out.items():
    if v is not None:
        pd_out.at[k] = chr(v)
pd_out.to_csv("vis.csv")
pass

