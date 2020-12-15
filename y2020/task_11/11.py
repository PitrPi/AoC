from typing import List, Iterable, Optional

from Helpers.helpers import read_newest
import os

os.getcwd()
# os.chdir("y2020/task_11")


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


if __name__ == '__main__':
    data = read_newest()
    # Part 1
    cnw1 = Conway(data)
    cnw2 = Conway(data)
    cnw2.step()
    while cnw1.board != cnw2.board:
        cnw1.step()
        cnw2.step()
    print(cnw2.counter())

    # Part 2
    cnw1 = Conway(data, dead_thrs=5)
    cnw2 = Conway(data, dead_thrs=5)
    cnw2.step(long_view=True)
    while cnw1.board != cnw2.board:
        cnw1.step(long_view=True)
        cnw2.step(long_view=True)
    print(cnw2.counter())
