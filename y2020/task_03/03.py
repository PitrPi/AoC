from Helpers.helpers import read_newest
import os
os.chdir("y2020/task_03")

test_input = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
test_input = test_input.split('\n')
data = read_newest()
data = test_input
width = len(data[0])

all_tree_counter = 1
slope = [1, 3]
tree_counter = 0
for line_idx, line in enumerate(data):
    if line[line_idx*slope[1] % width] == "#":
        tree_counter += 1
print(tree_counter)
all_tree_counter *= tree_counter

slope = [1, 1]
tree_counter = 0
for line_idx, line in enumerate(data):
    if line[line_idx*slope[1] % width] == "#":
        tree_counter += 1
print(tree_counter)
all_tree_counter *= tree_counter

slope = [1, 5]
tree_counter = 0
for line_idx, line in enumerate(data):
    # print(line_idx*slope[1] % width)
    if line[line_idx*slope[1] % width] == "#":
        tree_counter += 1
print(tree_counter)
all_tree_counter *= tree_counter

slope = [1, 7]
tree_counter = 0
for line_idx, line in enumerate(data):
    if line[line_idx*slope[1] % width] == "#":
        tree_counter += 1
print(tree_counter)
all_tree_counter *= tree_counter

slope = [2, 1]
tree_counter = 0
for line_idx, line in enumerate(data):
    if (line_idx % 2) == 1:
        continue
    if line[line_idx*slope[1]//2 % width] == "#":
        tree_counter += 1
print(tree_counter)
all_tree_counter *= tree_counter

print(all_tree_counter)
