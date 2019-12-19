from Helpers.helpers import read_newest

def safe_add(dic, key, val=1):
    dic[key] = dic.get(key, 0) + val
    return dic


def manhatann(val):
    return sum([abs(x) for x in val])


data = read_newest()
# data = ['R8,U5,L5,D3','U7,R6,D4,L4']
# data = ['R75,D30,R83,U83,L12,D49,R71,U7,L72','U62,R66,U55,R34,D71,R55,D58,R83']
# data = ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51','U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']
data = [x.split(',') for x in data]
matrix_dict = {}
matrix_len = {}
for dat in data:
    current_x = 0
    current_y = 0
    this_wire = set()
    cntr = 0
    for instruction in dat:
        if instruction[0] == 'R':
            for i in range(int(instruction[1:])):
                current_x += 1
                cntr += 1
                if (current_x, current_y) not in this_wire:
                    matrix_dict = safe_add(matrix_dict, (current_x, current_y))
                    matrix_len = safe_add(matrix_len, (current_x, current_y), cntr)
                this_wire.add((current_x, current_y))
        elif instruction[0] == 'L':
            for i in range(int(instruction[1:])):
                current_x -= 1
                cntr += 1
                if (current_x, current_y) not in this_wire:
                    matrix_dict = safe_add(matrix_dict, (current_x, current_y))
                    matrix_len = safe_add(matrix_len, (current_x, current_y), cntr)
                this_wire.add((current_x, current_y))
        elif instruction[0] == 'D':
            for i in range(int(instruction[1:])):
                current_y -= 1
                cntr += 1
                if (current_x, current_y) not in this_wire:
                    matrix_dict = safe_add(matrix_dict, (current_x, current_y))
                    matrix_len = safe_add(matrix_len, (current_x, current_y), cntr)
                this_wire.add((current_x, current_y))
        elif instruction[0] == 'U':
            for i in range(int(instruction[1:])):
                current_y += 1
                cntr += 1
                if (current_x, current_y) not in this_wire:
                    matrix_dict = safe_add(matrix_dict, (current_x, current_y))
                    matrix_len = safe_add(matrix_len, (current_x, current_y), cntr)
                this_wire.add((current_x, current_y))
        else:
            raise ValueError('Invalid instruction')

possible_dist = []
possible_len = []
for key, value in matrix_dict.items():
    if value > 1:
        possible_dist.append(manhatann(key))
        possible_len.append(matrix_len[key])

print(min(possible_dist))
print(min(possible_len))
