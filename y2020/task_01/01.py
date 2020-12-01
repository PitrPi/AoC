with open("y2020/task_01/input.txt") as f:
    data = f.readlines()
data = [x.strip() for x in data]
data = [int(x) for x in data]


def solve(data):
    for prev_val in data:
        for val in data:
            if prev_val + val == 2020:
                return prev_val*val


def solve2(data):
    for prev_val in data:
        for val in data:
            for post_val in data:
                if post_val + prev_val + val == 2020:
                return prev_val*val*post_val

print(solve(data))
print(solve2(data))
