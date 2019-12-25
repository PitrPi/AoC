import pandas as pd
from Helpers.intcode3 import parse_op3
from Helpers.helpers import read_newest_int_list
data = read_newest_int_list()
data[0] = 2
data_dict = dict(enumerate(data))
# Starts with right  ^ --> >
# Aggregate path
# R4R10R10R8
# L12L10L4L4R10R10
# R6
# L12L10L4L4R10R10
# R8R8L10L4
# R8
# L12L10L4
# R8R8
# A:L10L4L4R10R10R8R8L10L4
A = 'R,4,L,10,L,10'
B = 'L,8,R,12,R,10,R,4'
C = 'L,8,L,8,R,10,R,4'
routine = 'A,B,A,B,A,C,B,C,A,C'
A_ascii = [ord(char) for char in A]
A_ascii.append(10)
B_ascii = [ord(char) for char in B]
B_ascii.append(10)
C_ascii = [ord(char) for char in C]
C_ascii.append(10)
R_ascii = [ord(char) for char in routine]
R_ascii.append(10)
pd_out = pd.DataFrame(index=range(45), columns=range(45))
x = 0
y = 0
idx = 0
base = 0
halt = False
inpt = [10, ord('n')]
inpt.extend(reversed(C_ascii))
inpt.extend(reversed(B_ascii))
inpt.extend(reversed(A_ascii))
inpt.extend(reversed(R_ascii))
while not halt:
    iterate = True
    output = None
    while iterate:
        data_dict, idx, iterate, _, _, output, halt, base = \
            parse_op3(data_dict, idx, iterate, inpt, None, None, base)
        if halt:
            break
        if output is not None and output < 256:
            if output == 10:
                x = 0
                y += 1
            else:
                pd_out.at[(x, y)] = output
                x += 1
        elif output is not None:
            print(output)
