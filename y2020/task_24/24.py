from Helpers.helpers import read_newest
from collections import Counter, Set

data = read_newest()
dat = data[0]
data_list = []
for dat in data:
    data_single = []
    buffer = ''
    for ch in dat:
        buffer += ch
        if ch in 'ew':
            data_single.append(buffer)
            buffer = ''
    data_list.append(data_single)


data_coords = []
for dat in data_list:
    data_coords.append((2*dat.count('e')-2*dat.count('w')+dat.count('ne')+dat.count('se')-dat.count('nw')-dat.count('sw'),
                        dat.count('se')+dat.count('sw')-dat.count('nw')-dat.count('ne')))

counter = Counter(data_coords)
# Part 1
[*counter.values()].count(1)

# Part 2


def update_list_of_blacks(black, flip):
    for fl in flip:
        if fl in black:
            black.remove(fl)
        else:
            black.add(fl)
    return black

def count_neighbors(black, coords):
    count = 0
    for direction in [(2, 0), (1, 1), (-1, 1), (-2, 0), (1, -1), (-1, -1)]:
        coords_check = (coords[0] + direction[0], coords[1] + direction[1])
        if coords_check in black:
            count += 1
    return count

def get_list_to_flip(black):
    flip_list = []
    min_x, max_x = min([b[0] for b in black]),  max([b[0] for b in black])
    min_y, max_y = min([b[1] for b in black]),  max([b[1] for b in black])
    for x in range(min_x-1, max_x+2):
        for y in range(min_y-1, max_y+2):
            neighbors = count_neighbors(black, (x, y))
            if (x, y) in black and (neighbors == 0 or neighbors > 2):
                flip_list.append((x, y))
            elif (x, y) not in black and neighbors == 2:
                flip_list.append((x, y))
    return flip_list


black = set()
black = update_list_of_blacks(black, data_coords)
len(black)

for _ in range(100):
    black = update_list_of_blacks(black, get_list_to_flip(black))
    print(len(black))
