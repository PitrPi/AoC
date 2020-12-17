from time import time

if __name__ == '__main__':
    data = [int(x) for x in '18,11,9,0,5,1'.split(',')]
    start_len = len(data)
    for _ in range(start_len, 2020):
        if data[-1] in data[:-1]:
            last_idx = data[-2::-1].index(data[-1])  # I hate slicing while reversing xD
            data.append(last_idx+1)
        else:
            data.append(0)
    print(data[-1])

    # Part 2
    """ Same approach won't work,
     it is exponentially expensive to look for numbers in list
     We need structure that forgets and have better look-up.
     So we use dict with numbers as keys and last indexes as values
    """
    data_solved = data[:]
    data = [int(x) for x in '18,11,9,0,5,1'.split(',')]
    data_dict = {v: k for k, v in enumerate(data[:-1])}
    value_to_solve = data[-1]
    start_len = len(data)-1
    prev_time = time()
    for idx in range(start_len, 30000000-1):
        if idx % 100000 == 0:
            print(idx)
            print(time()-prev_time)
            prev_time = time()
        if value_to_solve not in data_dict.keys():
            data_dict[value_to_solve] = idx
            value_to_solve = 0
        else:
            diff = idx - data_dict[value_to_solve]
            data_dict[value_to_solve] = idx
            value_to_solve = diff
        # if data[-1] in data[:-1]:
        #     last_idx = data[-2::-1].index(data[-1])  # I hate slicing while reversing xD
        #     data.append(last_idx+1)
        # else:
        #     data.append(0)
    print(value_to_solve)

