import math
from Helpers.helpers import read_newest_int

data = read_newest_int()
print(sum([math.floor(dat/3)-2 for dat in data]))


def calc_fuel(inpt):
    return math.floor((inpt/3))-2


total_fuel = 0
for dat in data:
    while calc_fuel(dat) > 0:
        dat = calc_fuel(dat)
        total_fuel += dat
print(total_fuel)
