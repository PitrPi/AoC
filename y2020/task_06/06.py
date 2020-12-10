import os

from Helpers.helpers import read_newest

# os.chdir("y2020/task_06")
data = read_newest()
data_stream = " ".join(data)
data_split = data_stream.split("  ")
data_sets = [set(x.replace(" ", "")) for x in data_split]
# Part 1
print(sum([len(x) for x in data_sets]))

# Part 2
data_lens = []
counter = 0
for dat in data:
    if dat == '':
        data_lens.append(counter)
        counter = 0
    else:
        counter += 1
data_lens.append(counter)

part2_counter = 0
for idx, data_set in enumerate(data_sets):
    answer_counter = 0
    for answer in data_set:
        if data_split[idx].count(answer) != data_lens[idx]:
            data_set_ok = False
        else:
            answer_counter += 1
    part2_counter += answer_counter
print(part2_counter)
