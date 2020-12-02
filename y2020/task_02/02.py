from Helpers.helpers import read_newest
import os
os.chdir("y2020/task_02")
data = read_newest()
parsed = []
for line in data:
    rng, ch, pwd = line.split(" ")
    mn, mx = rng.split("-")
    ch = ch[:-1]
    parsed.append({"mn": int(mn), "mx": int(mx), "wht": ch, "pwd": pwd})

# Part 1
counter = 0
for line in parsed:
    if line["mx"] >= line["pwd"].count(line["wht"]) >= line["mn"]:
        counter += 1
print(counter)

# Part 2
counter = 0
for line in parsed:
    if (line["pwd"][line["mn"]-1]==line["wht"]) != (line["pwd"][line["mx"]-1]==line["wht"]):
        counter += 1
print(counter)