from Helpers.helpers import read_newest_int_list

data = read_newest_int_list()
data[1] = 12
data[2] = 2
idx = 0
current_value = data[idx]
while current_value != 99:
    if current_value == 1:
        data[data[idx+3]] = data[data[idx+1]]+data[data[idx+2]]
    elif current_value == 2:
        data[data[idx+3]] = data[data[idx+1]]*data[data[idx+2]]
    else:
        raise ValueError('Invalid value')
    idx += 4
    current_value = data[idx]
print('Part1')
print(data[0])
print('Part2')

data = read_newest_int_list()
for i in range(99):
    for j in range(99):
        try:
            data = read_newest_int_list()
            data[1] = i
            data[2] = j
            idx = 0
            current_value = data[idx]
            while current_value != 99:
                if current_value == 1:
                    data[data[idx+3]] = data[data[idx+1]]+data[data[idx+2]]
                elif current_value == 2:
                    data[data[idx+3]] = data[data[idx+1]]*data[data[idx+2]]
                else:
                    raise ValueError('Invalid operation')
                idx += 4
                current_value = data[idx]
            if data[0] == 19690720:
                print(data[1]*100+data[2])
            else:
                raise ValueError('Invalid end value')
        except ValueError:
            pass
