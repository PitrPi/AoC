import math
from typing import List

from Helpers.helpers import read_newest

# import os
# os.chdir('y2020/task_20')

DIRECTIONS = ["top", "right", "bottom", "left"]
DIRECTIONS_O = ["bottom", "left", "top", "right"]
IDX_O = [[-1, 0], [0, 1], [1, 0], [0, -1]]
DIRS = zip(DIRECTIONS, DIRECTIONS_O, IDX_O)
MONSTER = [[0, 18], [1, 18], [1, 19],  # Head
           [1, 0], [2, 1], [2, 4], [1, 5],
           [1, 6], [2, 7], [2, 10], [1, 11],
           [1, 12], [2, 13], [2, 16], [1, 17]]


class Tile:
    def __init__(self, tile_idx, tile_data: List[str]):
        self.idx = tile_idx
        self.tile = tile_data
        self.rotation = 0
        self.flip = 0

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
        self.flip += 1
        self.flip %= 2

    def apply_rotation(self):
        self.tile = ["".join(x[::-1]) for x in zip(*self.tile)]
        self.rotation += 1
        self.rotation %= 4

    def print(self):
        print("+"+"-"*(len(self.tile))+"+")
        for row in self.tile:
            print('|'+row+'|')
        print("+"+"-"*(len(self.tile))+"+")


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
    def __init__(self, tiles, tile_zero):
        self.final_board = []
        self.tiles = tiles
        self.tile_zero = tile_zero
        self.dim = int(math.sqrt(len(tiles)))
        self.target_array = [[tile_zero] * self.dim for _ in range(self.dim)]
        self.used_idx = []
        self.solved = False
        self.x = 0
        self.y = 0

    def check_valid(self, tile_idx: int):
        tile = self.tiles[tile_idx]
        if self.x > 0:
            if tile.read_edge("left") != self.target_array[self.x-1][self.y].read_edge("right"):
                return False
        if self.y > 0:
            if tile.read_edge("top") != self.target_array[self.x][self.y-1].read_edge("bottom"):
                return False
        self.used_idx.append(tile.idx)
        self.target_array[self.x][self.y] = tile
        self.increase_counter()
        return True

    def increase_counter(self):
        self.x += 1
        if self.x >= self.dim:
            self.x = 0
            self.y += 1
        if self.y >= self.dim:
            self.solved = True

    def decrease_counter(self):
        deleted_idx = self.used_idx.pop()
        self.target_array[self.x][self.y] = self.tile_zero
        self.x -= 1
        if self.x < 0:
            self.x = self.dim-1
            self.y -= 1
        if self.y < 0:
            raise IndexError
        return deleted_idx

    def remove_tile(self):
        self.decrease_counter()

    def yield_tiles(self):
        for idx in self.tiles.keys():
            if idx in self.used_idx:
                continue
            for _ in range(2):
                for _ in range(4):
                    yield idx
                    self.tiles[idx].apply_rotation()
                self.tiles[idx].apply_flip()

    def solve(self):
        if not self.solved:
            for tile_idx in self.yield_tiles():
                matching = self.check_valid(tile_idx)
                if matching:
                    # self.print_board()
                    self.solve()
                    if self.solved:
                        return None
            if self.solved:
                return None
            else:
                self.decrease_counter()

    def print_board(self):
        for tiles in self.target_array:
            for line_idx, _ in enumerate(tiles[0].tile):
                print("|".join([t.tile[line_idx][1:-1] for t in tiles]))
            print("-"*(len(self.target_array[0][0].tile)*3-1))
        print("-"*(len(self.target_array[0][0].tile)*3-1))

    def create_board_for_monsters(self):
        # Transpose
        transposed_array = list(map(list, zip(*self.target_array)))
        for tiles in transposed_array:
            for line_idx, _ in enumerate(tiles[0].tile):
                if line_idx == 0:
                    continue
                else:
                    self.final_board.append("".join([t.tile[line_idx][1:-1] for t in tiles]))
            self.final_board.pop()


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


def find_monsters(tile: Tile):
    monster_count = 0
    for line_idx in range(0, len(tile.tile)-2):
        for row_idx in range(0, len(tile.tile)-19):
            if is_monster(tile, line_idx, row_idx):
                monster_count += 1
    return monster_count


def is_monster(tile, line_idx, row_idx):
    for coords in MONSTER:
        if tile.tile[coords[0]+line_idx][coords[1]+row_idx] != "#":
            return False
    return True


if __name__ == '__main__':
    data = use_data(1)
    parsed_data = parse_data(data)
    tiles = {}
    for idx, tile in parsed_data.items():
        tiles[idx] = Tile(idx, tile)
    tile_zero = Tile(0, ["X"*len(tile)]*len(tile))
    board = Board(tiles, tile_zero)
    board.solve()
    board.print_board()
    print(board.target_array[0][0].idx
          * board.target_array[-1][0].idx
          * board.target_array[0][-1].idx
          * board.target_array[-1][-1].idx)
    board.create_board_for_monsters()
    final_board = Tile(0, board.final_board)
    final_board.print()
    monster_counts = []
    for _ in range(2):
        for _ in range(4):
            mc = find_monsters(final_board)
            monster_counts.append(mc)
            final_board.apply_rotation()
        final_board.apply_flip()
    print(2020-(max(monster_counts)*len(MONSTER)))


    fb = """.#.#..#.##...#.##..#####
    ###....#.#....#..#......
    ##.##.###.#.#..######...
    ###.#####...#.#####.#..#
    ##.#....#.##.####...#.##
    ...########.#....#####.#
    ....#..#...##..#.#.###..
    .####...#..#.....#......
    #..#.##..#..###.#.##....
    #.####..#.####.#.#.###..
    ###.#.#...#.######.#..##
    #.####....##..########.#
    ##..##.#...#...#.#.#.#..
    ...#..#..#.#.##..###.###
    .#.#....#.##.#...###.##.
    ###.#...#..#.##.######..
    .#.#.###.##.##.#..#.##..
    .####.###.#...###.#..#.#
    ..#.#..#..#.#.#.####.###
    #..####...#.#.#.###.###.
    #####..#####...###....##
    #.##..#..#...#..####...#
    .#.###..##..##..####.##.
    ...###...##...#...#..###""".split("\n")