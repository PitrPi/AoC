import math
from typing import List

from Helpers.helpers import read_newest

# import os
# os.chdir('y2020/task_20')

DIRECTIONS = ["top", "right", "bottom", "left"]
DIRECTIONS_O = ["bottom", "left", "top", "right"]
IDX_O = [[-1, 0], [0, 1], [1, 0], [0, -1]]
DIRS = zip(DIRECTIONS, DIRECTIONS_O, IDX_O)


class Tile:
    def __init__(self, tile_idx, tile_data: List[str]):
        self.idx = tile_idx
        self.tile = tile_data
        # self.rotation = 0

    def read_edge(self, location="top"):
        if location == "top":
            return self.tile[0]
        elif location == "bottom":
            return self.tile[-1]
        elif location == "left":
            return "".join([x[0] for x in self.tile])
        elif location == "right":
            return "".join([x[-1] for x in self.tile])

    def apply_transposition(self):
        # rotate not transpose!
        self.tile = ["".join(x) for x in zip(*self.tile)]

    def apply_flip(self):
        self.tile = [x[::-1] for x in self.tile]

    def apply_rotation(self):
        self.tile = ["".join(x[::-1]) for x in zip(*self.tile)]

    def print(self):
        print("-"*(len(self.tile)+2))
        for row in self.tile:
            print('|'+row+'|')
        print("-"*(len(self.tile)+2))


def parse_data(data):
    final = {}
    current_idx = 0
    for dat in data:
        if dat[:4] == "Tile":
            current_idx = int(dat[5:-1])
            final[current_idx] = []
        elif dat == '':
            continue
        else:
            final[current_idx].append(dat)
    return final


class Board:
    def __init__(self, tiles):
        self.tiles = tiles
        self.dim = int(math.sqrt(len(tiles)))
        self.target_array = [[0] * self.dim for _ in range(self.dim)]
        self.used_idx = []
        self.solved = False

    def yield_tiles(self, row, col):
        for idx in self.tiles.keys():
            if idx in self.used_idx:
                continue
            for _ in range(2):
                for _ in range(4):
                    self.target_array[row][col] = idx
                    if self.check_valid():
                        self.used_idx.append(idx)
                        yield idx
                    else:
                        self.target_array[row][col] = 0
                    self.tiles[idx].apply_rotation()
                self.tiles[idx].apply_flip()
        return None

    def solve(self, row, col):
        for _ in self.yield_tiles(row, col):
            ncol = col + 1
            nrow = row
            if ncol >= self.dim:
                ncol = 0
                nrow += 1
                if nrow >= self.dim:
                    self.solved = True
                    return None
            if self.solved:
                return None
            self.solve(nrow, ncol)
            self.used_idx.pop()
            self.target_array[row][col] = 0

    def solve_part1(self):
        self.solve(0, 0)

    def check_valid(self):
        dirs = zip(DIRECTIONS, DIRECTIONS_O, IDX_O)
        for row_idx, row in enumerate(self.target_array):
            for col_idx, col in enumerate(row):
                if col == 0:
                    continue
                for direction, odirection, oidx in dirs:
                    orow_idx = row_idx + oidx[0]
                    ocol_idx = col_idx + oidx[1]
                    otile_idx = self.target_array[orow_idx][ocol_idx]
                    if otile_idx == 0:
                        continue
                    otile = self.tiles[otile_idx]
                    if (0 <= orow_idx <= self.dim
                            and 0 <= ocol_idx <= self.dim):
                        if (self.tiles[col].read_edge(direction)
                                != otile.read_edge(odirection)):
                            return False
        return True


def use_data(idx=None):
    if idx is None or idx == 1:
        data = read_newest()
    elif idx == 2:
        data = '''Tile 2311:
XX##X#XX#X
##XX#XXXXX
#XXX##XX#X
####X#XXX#
##X##X###X
##XXX#X###
X#X#X#XX##
XX#XXXX#XX
###XXX#X#X
XX###XX###

Tile 1951:
#X##XXX##X
#X####XXX#
XXXXX#XX##
#XXX######
X##X#XXXX#
X###X#####
###X##X##X
X###XXXX#X
XX#X#XX#X#
#XXX##X#XX

Tile 1171:
####XXX##X
#XX##X#XX#
##X#XX#X#X
X###X####X
XX###X####
X##XXXX##X
X#XXX####X
#X##X####X
####XX#XXX
XXXXX##XXX

Tile 1427:
###X##X#XX
X#XX#X##XX
X#X##X#XX#
#X#X#X##X#
XXXX#XXX##
XXX##XX##X
XXX#X#####
X#X####X#X
XX#XX###X#
XX##X#XX#X

Tile 1489:
##X#X#XXXX
XX##XXX#XX
X##XX##XXX
XX#XXX#XXX
#####XXX#X
#XX#X#X#X#
XXX#X#X#XX
##X#XXX##X
XX##X##X##
###X##X#XX

Tile 2473:
#XXXX####X
#XX#X##XXX
#X##XX#XXX
######X#X#
X#XXX#X#X#
X#########
X###X#XX#X
########X#
##XXX##X#X
XX###X#X#X

Tile 2971:
XX#X#XXXX#
#XXX###XXX
#X#X###XXX
##X##XX#XX
X#####XX##
X#XX####X#
#XX#X#XX#X
XX####X###
XX#X#X###X
XXX#X#X#X#

Tile 2729:
XXX#X#X#X#
####X#XXXX
XX#X#XXXXX
XXXX#XX#X#
X##XX##X#X
X#X####XXX
####X#X#XX
##X####XXX
##XX#X##XX
#X##XXX##X

Tile 3079:
#X#X#####X
X#XX######
XX#XXXXXXX
######XXXX
####X#XX#X
X#XXX#X##X
#X#####X##
XX#X###XXX
XX#XXXXXXX
XX#X###XXX'''.split('\n')
    return data


if __name__ == '__main__':
    data = use_data(2)
    parsed_data = parse_data(data)
    tiles = {}
    for idx, tile in parsed_data.items():
        tiles[idx] = Tile(idx, tile)
    board = Board(tiles)
    board.check_valid()
    board.solve_part1()
    board.check_valid()
    print(board.target_array[0][0]
          * board.target_array[-1][0]
          * board.target_array[0][-1]
          * board.target_array[-1][-1])
    tiles[board.target_array[1][0]].print()