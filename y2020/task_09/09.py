from Helpers.helpers import read_newest_int
import os

os.getcwd()
os.chdir("y2020/task_09")


def check_sum(data, idx):
    # Check values
    for idx_start in range(idx-25, idx):
        for idx_current in range(idx_start+1, idx):
            print(str(idx_start) + ":" + str(idx_current))
            if ((data[idx_current] != data[idx_start]) and
                ((data[idx_start] + data[idx_current]) == data[idx])):
                return True
    return False


def find_set(data, target):
    min_length = 2
    for idx in range(len(data)):
        current_length = min_length
        while sum(data[idx:(idx+current_length)]) < target:
            current_length += 1
        if sum(data[idx:(idx+current_length)]) == target:
            return min(data[idx:(idx+current_length)]) + max(data[idx:(idx+current_length)])
    return None


data = read_newest_int()

# Part 1
for idx in range(25, len(data)):
    if check_sum(data, idx):
        continue
    else:
        print(data[idx])
        break

# Part 2
find_set(data, data[idx])
