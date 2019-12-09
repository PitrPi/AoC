from Helpers.intcode import parse_op
from Helpers.intcode2 import parse_op2
from Helpers.helpers import read_newest_int_list
from itertools import permutations
from copy import deepcopy

# Part 1
data = read_newest_int_list()
# data = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
inpts = []
for phases in permutations(range(5), 5):
    inpt = 0
    output = None
    for phase in phases:
        idx = 0
        iterate = True
        datarun = deepcopy(data)
        while iterate:
            datarun, idx, iterate, inpt, phase, output = parse_op(datarun, idx, iterate, inpt, phase, output)
        inpt = output
    inpts.append(inpt)
print(max(inpts))

# Part2
data = read_newest_int_list()
# data = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26, 27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
inpts = []
for phases in permutations(range(5,10), 5):
    database = [deepcopy(data), deepcopy(data), deepcopy(data), deepcopy(data), deepcopy(data), ]
    idxs = [0, 0, 0, 0, 0]
    inpt = 0
    output = None
    halt = False
    phases_data = list(phases)
    while not halt:
        for amp, phase in enumerate(phases):
            print("AMP:", amp, " Phase:", phase, " Inpt:", inpt, " Phases_data:", phases_data[amp])
            idx = idxs[amp]
            iterate = True
            datarun = database[amp]
            while iterate:
                datarun, idx, iterate, inpt, phases_data[amp], output, halt = \
                    parse_op2(datarun, idx, iterate, inpt, phases_data[amp], output)
            inpt = output
            database[amp] = datarun
            idxs[amp] = idx
            if halt:
                break
    inpts.append(inpt)
print(max(inpts))
