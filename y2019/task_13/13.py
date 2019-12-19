from Helpers.intcode3 import parse_op3
from Helpers.helpers import read_newest_int_list

data = read_newest_int_list()
data_dict = dict(enumerate(data))
# Part 2
data_dict[0] = 2
attention = False
print_output = False


halt = False
idx = 0
x = 0
y = 0
block_cnt = 0
output_cnt = 0
base = 0
inpt = None

while not halt:
    iterate = True
    while iterate:
        data_dict, idx, iterate, inpt, _, output, halt, base = \
            parse_op3(data_dict, idx, iterate, inpt, None, None, base)
        if halt:
            break
    if output_cnt == 2:
        if output == 2:
            block_cnt += 1
        output_cnt = 0
        attention = False
        print_output = False
    elif output_cnt == 0 and output == -1:
        attention = True
        output_cnt += 1
    elif output_cnt == 1 and output == 0 and attention is True:
        print_output = True
        output_cnt += 1
    elif print_output is True:
        print("Score is:", str(output))

# Part 1
print(block_cnt)
