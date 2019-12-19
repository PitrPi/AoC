from Helpers.intcode3 import parse_op3
from Helpers.helpers import read_newest_int_list

data = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
data = [1102,34915192,34915192,7,4,7,99,0]
data = read_newest_int_list('09')
data_dict = dict(enumerate(data))
halt = False
iterate = True
idx=0
inpt=2
base=0
while not halt:
    iterate = True
    while iterate:
        data_dict, idx, iterate, inpt, _, _, halt, base = \
            parse_op3(data_dict, idx, iterate, inpt, None, None, base)
    if halt:
        break
