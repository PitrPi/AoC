from Helpers.helpers import read_newest
import math

data = read_newest()
number = int(data[0])
data_bu = data[1]
# Part 1
divisors = [int(x) for x in data[1].split(',') if x != 'x']
departures = [math.ceil(number/divisor)*divisor
              for divisor in divisors]
differences = [departure - number for departure in departures]
min_diff = min(differences)
print(min_diff*divisors[differences.index(min_diff)])

# Part 2
# data[1] = "7,13,x,x,59,x,31,19"
# data[1] = "17,x,13,19"
# data[1] = "67,7,59,61"
divisors = [int(x) for x in data[1].split(',') if x != 'x']
divisors_all = [x for x in data[1].split(',')]
offsets = [divisors_all.index(str(divisor))
           for divisor in divisors]

# Bruteforce
def check_timestamp(timestamp):
    for divisor, offset in zip(divisors, offsets):
        if (timestamp+offset) % divisor != 0:
            return False
    return True

max_divisor = max(divisors)
timestamp = 0 - offsets[divisors.index(max_divisor)]

while not check_timestamp(timestamp):
    timestamp += max_divisor
print(timestamp)

# Mathematics
"""
Looking for t in N s.t.:
t = x1 * d1 - o1
t = x2 * d2 - o2
t = x3 * d3 - o3
t = x4 * d4 - o4
t = x5 * d5 - o5
t = x6 * d6 - o6
t = x7 * d7 - o7
t = x8 * d8 - o8
t = x9 * d9 - o9
x123456789 in N
d123456789 in divisors
o123456789 in offsets
t = x1 * 23 
t = x2 * 41 - 13
t = x3 * 733 - 23
t = x4 * 13 - 36
t = x5 * 17 - 37
t = x6 * 19 - 42
t = x7 * 29 - 52
t = x8 * 449 - 54
t = x9 * 37 - 91
This can be solved using chinese remainder theorem,
but wolfram alpha is just much more faster
https://www.wolframalpha.com/input/?i=t+%3D+x1+*+23%3B++t+%3D+x2+*+41+-+13%3B+t+%3D+x3+*+733+-+23%3B+t+%3D+x4+*+13+-+36%3B+t+%3D+x5+*+17+-+37%3B+t+%3D+x6+*+19+-+42%3B+t+%3D+x7+*+29+-+52%3B+t+%3D+x8+*+449+-+54%3B+t+%3D+x9+*+37+-+91
Looking for integer solution where n=0 for t


"""