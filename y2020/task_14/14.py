import re

from Helpers.helpers import read_newest

# import os
# os.chdir('y2020/task_14')


class Bitmask:
    def __init__(self):
        self.memory = {}
        self.mask = 'X'*36

    def _write(self, value: int, memory_idx: int):
        self.memory[memory_idx] = self._apply_mask(value)

    def _change_mask(self, new_mask: str):
        self.mask = new_mask

    def _apply_mask(self, value: int):
        value_str = '{0:0>36b}'.format(value)
        after_mask = ''.join([v if m=='X' else m
                              for v, m
                              in zip(value_str, self.mask)])
        return int(after_mask, 2)

    def parse_command(self, com: str):
        if com[:4] == 'mask':
            self._change_mask(com[7:])
        elif com[:3] == 'mem':
            mem_pos = int(re.findall("(?<=\[)[0-9]*?(?=\])", com)[0])
            mem_val = int(re.findall("[0-9]*$", com)[0])
            self._write(mem_val, mem_pos)

    def sum_memory(self):
        return sum(self.memory.values())


class Bitmask2(Bitmask):
    def _write(self, value: int, memory_idx: int):
        memory_idxs = self._apply_mask(memory_idx)
        for idx in memory_idxs:
            self.memory[idx] = value

    def _apply_mask(self, value: int):
        value_str = '{0:0>36b}'.format(value)
        after_mask = ''.join(['X' if m == 'X' else
                              '1' if m == '1'
                              else v
                              for v, m
                              in zip(value_str, self.mask)])
        return [int(x, 2) for x in self._float_solver(after_mask)]

    def _float_solver(self, masks):
        if isinstance(masks, str):
            masks = [masks]
        solutions = []
        for mask in masks:
            try:
                firstX = mask.index('X')
            except ValueError:
                firstX = None
            if firstX is None:
                solutions.append(mask)
            else:
                solutions.append(mask[:firstX] + '1' + mask[(firstX+1):])
                solutions.append(mask[:firstX] + '0' + mask[(firstX+1):])
        if len(masks) != len(solutions):
            solutions = self._float_solver(solutions)
        return solutions


if __name__ == '__main__':
    data = read_newest()
    bm = Bitmask()
    for dat in data:
        bm.parse_command(dat)
    print(bm.sum_memory())

    bm2 = Bitmask2()
    for dat in data:
        bm2.parse_command(dat)
    print(bm2.sum_memory())
