import os
import re

from Helpers.helpers import read_newest

data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".split('\n')


# Parse strings
def parse_rules(data):
    parsed = {}
    for dat in data:
        findings = re.findall("(\w*? \w*?) bag", dat)
        parsed[findings[0]] = findings[1:]
    return parsed


def parse_rules_with_count(data):
    parsed = {}
    for dat in data:
        findings = re.findall("([0-9]*)? ?(\w*? \w*?) bag", dat)
        if findings[1][1] != 'no other':
            parsed[findings[0][1]] = {f[1]: int(f[0]) for f in findings[1:]}
        else:
            parsed[findings[0][1]] = {}
    return parsed


def find_wrappers(parsed_data: dict, what):
    found = []
    for out, inn in parsed_data.items():
        if what in inn:
            found.append(out)
    return found


def iterative_find(parsed_data: dict, what):
    found = []
    wrappers = find_wrappers(parsed_data, what)
    found.extend(wrappers)
    # print(what + ": [" + ", ".join(wrappers) + "]")
    for wrapper in wrappers:
        found.extend(iterative_find(parsed_data, wrapper))
    return set(found)


def count_bags(parsed_data: dict, what):
    final_count = 0
    for bag, count in parsed_data[what].items():
        final_count += count
        final_count += count*count_bags(parsed_data, bag)
    return final_count


# os.chdir("y2020/task_07")

if __name__ == '__main__':
    data = read_newest()
    # Part 1
    parsed = parse_rules(data)
    wrappers = iterative_find(parsed, "shiny gold")
    print(len(wrappers))
    # Part 2
    parsed_with_count = parse_rules_with_count(data)
    counts = count_bags(parsed_with_count, "shiny gold")
    print(counts)