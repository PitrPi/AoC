from Helpers.helpers import read_newest_int
import os

os.getcwd()
os.chdir("y2020/task_10")

data = read_newest_int()


data.append(0)
data.append(max(data)+3)
data.sort()

# Part 1
step1 = 0
step2 = 0
step3 = 0
for idx in range(1, len(data)):
    step = data[idx]-data[idx-1]
    if step == 1:
        step1 += 1
    elif step == 2:
        step2 += 1
    elif step == 3:
        step3 += 1
    else:
        print(step)
        break
print(step1*step3)

# Observe, that step2 == 2. Every Step3 is separation point.
# Count steps between step3
length_of_onesteps = []
single_len = 0
for idx in range(1, len(data)):
    step = data[idx]-data[idx-1]
    if step == 1:
        single_len += 1
    elif step == 3:
        length_of_onesteps.append(single_len)
        single_len = 0
    else:
        print(step)
        break

# lengths 1 gives no freedom
# lengths 2 gives freedom 1 (on/off) x2
# lengths 3 gives freedom 3 (00,01,10,11) x4
# lengths 4 gives freedom 6 (001, 010, 011, 100, 101, 110, 111) x7
# Note that 000 for len4 is not valid as it creates hole of 4
print(2**length_of_onesteps.count(2) * 4**length_of_onesteps.count(3) * 7**length_of_onesteps.count(4))