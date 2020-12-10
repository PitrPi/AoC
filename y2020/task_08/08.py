from Helpers.bootcode import Bootcode
from Helpers.helpers import read_newest
from copy import deepcopy
# import os

# os.chdir("y2020/task_08")
if __name__ == '__main__':
    data = read_newest()
    instructions = [d.split(" ") for d in data]
    # Part 1
    bc = Bootcode(instructions)
    bc.execute_instructions()
    print(bc.status)
    print(bc.accumulator)

    # Part 2 - brute force, change every possible jmp <-> nop
    for idx, instruction in enumerate(instructions):
        if instruction[0] == 'jmp':
            instructions_changed = deepcopy(instructions)
            instructions_changed[idx][0] = 'nop'
            bc = Bootcode(instructions_changed)
            bc.execute_instructions()
            if bc.status == "Out of instructions":
                print(bc.status)
                print(idx)
                print(bc.accumulator)
                break
        elif instruction[0] == 'nop':
            instructions_changed = deepcopy(instructions)
            instructions_changed[idx][0] = 'jmp'
            bc = Bootcode(instructions_changed)
            bc.execute_instructions()
            if bc.status == "Out of instructions":
                print(bc.status)
                print(idx)
                print(bc.accumulator)
                break

