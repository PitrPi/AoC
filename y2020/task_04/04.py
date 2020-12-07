import os
import re

from Helpers.helpers import read_newest

os.chdir("y2020/task_04")
data = read_newest()
data.append('')

def evaluate(data):
    if all(dat == 1 for dat in data):
        return 1
    return 0

def validate_four_digits(s: str) -> bool:
    return validate_digits(s, 4)

def validate_digits(s: str, i: int) -> bool:
    if len(s) != i:
        return False
    try:
        int(s)
        return True
    except ValueError:
        return False

def evaluate_field(k, v):
    if k == 'byr':
        if validate_four_digits(v) and (1920 <= int(v) <= 2002):
            return 1
        else:
            return 0
    elif k == 'iyr':
        if validate_four_digits(v) and (2010 <= int(v) <= 2020):
            return 1
        else:
            return 0
    elif k == 'eyr':
        if validate_four_digits(v) and (2020 <= int(v) <= 2030):
            return 1
        else:
            return 0
    elif k == 'hgt':
        if v[-2:] == 'cm' and (150 <= int(v[:-2]) <= 193):
            return 1
        elif v[-2:] == 'in' and (59 <= int(v[:-2]) <= 76):
            return 1
        else:
            return 0
    elif k == 'hcl':
        if len(v) != 7:
            return 0
        if v[0] == '#':
            for c in v[1:]:
                if c not in 'abcdef0123456789':
                    return 0
        return 1
    elif k == 'ecl':
        if v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return 1
        else:
            return 0
    elif k == 'pid':
        if validate_digits(v, 9):
            return 1
        else:
            return 0


# Part 1
counter = 0
req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',]
req_fields_counter = [0]*len(req_fields)
for line in data:
    if line == '':
        counter += evaluate(req_fields_counter)
        req_fields_counter = [0]*len(req_fields)
    else:
        line += ' '
        found_fields = re.findall(".{3}(?=:)", line)
        for field in found_fields:
            if field == "cid":
                continue
            req_fields_counter[req_fields.index(field)] += 1
print(counter)


# Part 2

counter = 0
req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',]
req_fields_counter = [0]*len(req_fields)
for line in data:
    if line == '':
        counter += evaluate(req_fields_counter)
        req_fields_counter = [0]*len(req_fields)
    else:
        line += ' '
        found_fields = re.findall("(.{3})(:)(.*?)(?= )", line)
        for match in found_fields:
            if match[0] == "cid":
                continue
            req_fields_counter[req_fields.index(match[0])] += evaluate_field(match[0], match[2])

print(counter)

