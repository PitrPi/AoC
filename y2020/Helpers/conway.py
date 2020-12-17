from copy import deepcopy
from itertools import product
from typing import Optional, List, Iterable


class Conway:
    def __init__(self, data: Optional[List[Iterable]], rows=None, cols=None, alive='#', dead="L", static=".", live_thrs=0, dead_thrs=4):
        self.DEAD = dead
        self.ALIVE = alive
        self.STATIC = static
        self.LIFE_THRS = live_thrs
        self.DEAD_THRS = dead_thrs
        if data is None:
            if rows is None or cols is None:
                raise ValueError("Data or rows and cols have to be specified")
            else:
                self.board = [[self.DEAD for _ in range(cols)] for _ in range(rows)]
        else:
            self.board = data
        self.COLS = len(self.board[0])
        self.ROWS = len(self.board)

    def _calculate_state(self, row, col, long_view):
        if self.board[row][col] == self.STATIC:
            return self.STATIC
        alive = self._calculate_neighbors(row, col, long_view)
        if self.board[row][col] == self.ALIVE and alive >= self.DEAD_THRS:
            return self.DEAD
        elif self.board[row][col] == self.DEAD and alive <= self.LIFE_THRS:
            return self.ALIVE
        else:
            return self.board[row][col]

    def _calculate_neighbors(self, row, col, long_view):
        alive = 0
        neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        for rw, cl in neighbors:
            if not long_view:
                if row+rw < 0 or col+cl < 0 or row+rw >= self.ROWS or col+cl >= self.COLS:
                    continue
                elif self.board[row+rw][col+cl] == self.ALIVE:
                    alive += 1
            else:
                multiplier = 1
                while multiplier > 0:
                    if (row+(rw*multiplier) < 0
                            or col+(cl*multiplier) < 0
                            or row+(rw*multiplier) >= self.ROWS
                            or col+(cl*multiplier) >= self.COLS):
                        multiplier = 0
                    elif self.board[row+(rw*multiplier)][col+(cl*multiplier)] == self.ALIVE:
                        alive += 1
                        multiplier = 0
                    elif self.board[row + (rw*multiplier)][col + (cl*multiplier)] == self.DEAD:
                        multiplier = 0
                    elif self.board[row+(rw*multiplier)][col+(cl*multiplier)] == self.STATIC:
                        multiplier += 1

        return alive

    def step(self, long_view=False):
        new_board = [["" for _ in range(self.COLS)] for _ in range(self.ROWS)]
        for row in range(self.ROWS):
            for col in range(self.COLS):
                new_board[row][col] = self._calculate_state(row, col, long_view)
        self.board = new_board

    def print(self):
        for row in self.board:
            print("".join(row))

    def counter(self, what=None):
        if what is None:
            what = self.ALIVE
        count = 0
        for row in self.board:
            for col in row:
                if col == what:
                    count += 1
        return count


class Conway3D(Conway):
    def __init__(self, *args, **kwargs):
        if kwargs.get('data') is None \
                and kwargs.get('rows') is None\
                and kwargs.get('cols') is None:
            data = [[]]
            self.infinite = True
            self.x_min = 0
            self.y_min = 0
            self.z_min = 0
            self.x_max = 0
            self.y_max = 0
            self.z_max = 0
        else:
            data = kwargs['data']
            self.infinite = False
        super(Conway3D, self).__init__(data=data, *args, **kwargs)

    def insert_initial_board(self, board):
        # Board will be dict Z, Y, X with idx as key
        self.board = {}
        # Start is onedimensional in z = 0
        z = 0
        self.board[z] = {}
        for y, row in enumerate(board):
            self.board[z][y] = {}
            for x, col in enumerate(row):
                self.board[z][y][x] = col
            self.x_max = x+1
        self.y_max = y+1
        self.z_max = z+1
        # All +1 ensure that we can iterate over range(self.x_min, self.x_max)

    def _calculate_neighbors(self, x, y, z):
        alive = 0
        neighbors = product([-1, 0, 1], repeat=3)
        for x_chg, y_chg, z_chg in neighbors:
            if x_chg == y_chg == z_chg == 0:
                continue
            if self._is_alive(x+x_chg, y+y_chg, z+z_chg):
                alive += 1
        return alive

    def _calculate_state(self, x, y, z):
        try:
            current_state = self.board[z][y][x]
        except KeyError:
            current_state = self.DEAD
        neighbors = self._calculate_neighbors(x, y, z)
        if current_state == self.ALIVE:
            if 2 <= neighbors <= 3:
                return self.ALIVE
            else:
                return self.DEAD
        elif current_state == self.DEAD:
            if neighbors == 3:
                return self.ALIVE
            else:
                return self.DEAD

    def step(self):
        new_board = deepcopy(self.board)
        for z in range(self.z_min-1, self.z_max+1):
            if z not in new_board.keys():
                new_board[z] = {}
            for y in range(self.y_min - 1, self.y_max + 1):
                if y not in new_board[z].keys():
                    new_board[z][y] = {}
                for x in range(self.x_min - 1, self.x_max + 1):
                    new_board[z][y][x] = self._calculate_state(x, y, z)
        self.board = new_board
        self.x_min -= 1
        self.y_min -= 1
        self.z_min -= 1
        self.x_max += 1
        self.y_max += 1
        self.z_max += 1

    def _is_alive(self, x, y, z):
        try:
            res = self.board[z][y][x]
            if res == self.ALIVE:
                return True
            else:
                return False
        except KeyError:
            return False

    def counter(self, what=None):
        if what is None:
            what = self.ALIVE
        count = 0
        for x in range(self.x_min, self.x_max):
            for y in range(self.y_min, self.y_max):
                for z in range(self.z_min, self.z_max):
                    if self._is_alive(x, y, z):
                        count += 1
        return count

    def print(self):
        for z in range(self.z_min, self.z_max):
            print("-"*(self.x_max-self.x_min))
            print("z=" + str(z))
            for y in range(self.y_min, self.y_max):
                out = ''
                for x in range(self.x_min, self.x_max):
                    out += self.board[z][y][x]
                print(out)

class Conway4D(Conway3D):
    def __init__(self, *args, **kwargs):
        super(Conway4D, self).__init__(*args, **kwargs)
        self.t_min = 0
        self.t_max = 0

    def insert_initial_board(self, board):
        # Board will be dict Z, Y, X with idx as key
        self.board = {}
        # Start is onedimensional in z = 0
        z = 0
        t = 0
        self.board[t] = {}
        self.board[t][z] = {}
        for y, row in enumerate(board):
            self.board[t][z][y] = {}
            for x, col in enumerate(row):
                self.board[t][z][y][x] = col
            self.x_max = x+1
        self.y_max = y+1
        self.z_max = z+1
        self.t_max = t+1
        # All +1 ensure that we can iterate over range(self.x_min, self.x_max)

    def _calculate_neighbors(self, x, y, z, t):
        alive = 0
        neighbors = product([-1, 0, 1], repeat=4)
        for x_chg, y_chg, z_chg, t_chg in neighbors:
            if x_chg == y_chg == z_chg == t_chg == 0:
                continue
            if self._is_alive(x+x_chg, y+y_chg, z+z_chg, t+t_chg):
                alive += 1
        return alive

    def _calculate_state(self, x, y, z, t):
        try:
            current_state = self.board[t][z][y][x]
        except KeyError:
            current_state = self.DEAD
        neighbors = self._calculate_neighbors(x, y, z, t)
        if current_state == self.ALIVE:
            if 2 <= neighbors <= 3:
                return self.ALIVE
            else:
                return self.DEAD
        elif current_state == self.DEAD:
            if neighbors == 3:
                return self.ALIVE
            else:
                return self.DEAD

    def step(self):
        new_board = deepcopy(self.board)
        for t in range(self.t_min-1, self.t_max+1):
            if t not in new_board.keys():
                new_board[t] = {}
            for z in range(self.z_min-1, self.z_max+1):
                if z not in new_board[t].keys():
                    new_board[t][z] = {}
                for y in range(self.y_min - 1, self.y_max + 1):
                    if y not in new_board[t][z].keys():
                        new_board[t][z][y] = {}
                    for x in range(self.x_min - 1, self.x_max + 1):
                        new_board[t][z][y][x] = self._calculate_state(x, y, z, t)
        self.board = new_board
        self.x_min -= 1
        self.y_min -= 1
        self.z_min -= 1
        self.t_min -= 1
        self.x_max += 1
        self.y_max += 1
        self.z_max += 1
        self.t_max += 1

    def _is_alive(self, x, y, z, t):
        try:
            res = self.board[t][z][y][x]
            if res == self.ALIVE:
                return True
            else:
                return False
        except KeyError:
            return False

    def counter(self, what=None):
        if what is None:
            what = self.ALIVE
        count = 0
        for t in range(self.t_min, self.t_max):
            for x in range(self.x_min, self.x_max):
                for y in range(self.y_min, self.y_max):
                    for z in range(self.z_min, self.z_max):
                        if self._is_alive(x, y, z, t):
                            count += 1
        return count


if __name__ == '__main__':
    c3d = Conway3D(dead='.', alive='#', static=' ')
    test_data = """.#.
..#
###""".split('\n')
    c3d.insert_initial_board(test_data)
    for _ in range(6):
        c3d.print()
        c3d.step()
    print(c3d.counter())