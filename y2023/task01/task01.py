import re

with open('y2023/task01/input.txt') as f:
    data = f.readlines()
data = [x.strip() for x in data]

print(sum([
    int(re.search('[0-9]', x).group() + re.search('[0-9]', x[::-1]).group()) for x in data
]))


def str_replace(inp):
    start = 0
    start_idx = 999
    end = 0
    end_idx = -1
    map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for i, o in map.items():
        challenger = inp.find(i)
        if challenger >= 0 and challenger < start_idx:
            start = o
            start_idx = challenger
        challenger = inp.find(o)
        if challenger >= 0 and challenger < start_idx:
            start = o
            start_idx = challenger
        challenger = inp.rfind(i)
        if challenger >= 0 and challenger > end_idx:
            end = o
            end_idx = challenger
        challenger = inp.rfind(o)
        if challenger >= 0 and challenger > end_idx:
            end = o
            end_idx = challenger

    return int(start + end)

for d in data:
    print(str_replace(d), d)
print(sum([str_replace(x) for x in data]))
tests = [
    'two1nine',
    'eightwothree4',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'xxoneightonexx',
    '12abc31'
]
for test in tests:
    print(str_replace(test))
