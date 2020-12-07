import os

from Helpers.helpers import read_newest

os.chdir("y2020/task_05")
data = read_newest()


def calculate_row(ticket: str):
    row = ticket[:-3]
    row = row.replace("F", "0")
    row = row.replace("B", "1")
    return int(row, 2)

def calculate_col(ticket: str):
    row = ticket[-3:]
    row = row.replace("L", "0")
    row = row.replace("R", "1")
    return int(row, 2)


def calculate_id(ticket):
    return 8*calculate_row(ticket) + calculate_col(ticket)

# Part 1
max_id = 0
for ticket in data:
    id = calculate_id(ticket)
    max_id = max(max_id, id)

print(max_id)

# Part 2
ids = []
for ticket in data:
    id = calculate_id(ticket)
    ids.append(id)

ids.sort()
for idx, id in enumerate(ids[1:]):
    if id - ids[idx] > 1:
        print(id-1)
