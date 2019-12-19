import math
from copy import copy
from Helpers.helpers import read_newest
import re
data = read_newest("14")


def parse_to_dict(data):
    out = {}
    for dat in data:
        inputs = re.findall(r'.*(?==>)', dat)[0]
        outputs = re.findall(r'(?<=>).*', dat)[0]
        inputs_names = re.findall('[A-Z]+', inputs)
        inputs_amts = re.findall('\d+', inputs)
        outputs_names = re.findall('[A-Z]+', outputs)[0]
        outputs_amts = re.findall('\d+', outputs)[0]
        out[outputs_names] = {'amt': int(outputs_amts), 'inputs': dict(zip(inputs_names, inputs_amts))}
    return out


def i_need_multiple(what, num, have, data_dict):
    needs = data_dict[what]['inputs']
    carry_on = True
    for need_name, need_amt in needs.items():
        if need_name != 'ORE':
            have, carry_on = i_need_multiple(need_name, math.ceil((int(need_amt)-have.get(need_name, 0))*num/data_dict[what]['amt']), have, data_dict)
        if not carry_on:
            break
    if carry_on:
        have[what] = have.get(what, 0) + math.ceil(num/data_dict[what]['amt'])*data_dict[what]['amt']
        for need_name, need_amt in needs.items():
            have[need_name] -= int(need_amt)*math.ceil(num/data_dict[what]['amt'])*data_dict[what]['amt']
            if have[need_name] < 0:
                if need_name == 'ORE':
                    return have, False
                have, carry_on = i_need_multiple(need_name, -have[need_name], have, data_dict)
                if not carry_on:
                    break
    return have, carry_on


def i_need(what, have, data_dict):
    needs = data_dict[what]['inputs']
    carry_on = True
    for need_name, need_amt in needs.items():
        while have.get(need_name, 0) < int(need_amt):
            if need_name == 'ORE':
                return have, False
            have, carry_on = i_need(need_name, have, data_dict)
            if not carry_on:
                break
    if carry_on:
        have[what] = have.get(what, 0) + data_dict[what]['amt']
        for need_name, need_amt in needs.items():
            have[need_name] -= int(need_amt)
            while have[need_name] < 0:
                if need_name == 'ORE':
                    return have, False
                have, carry_on = i_need(need_name, have, data_dict)
                if not carry_on:
                    break
    return have, carry_on

data_dict = parse_to_dict(data)
have = {'ORE': 1250000}
have, _ = i_need('FUEL', have, data_dict)

print(1250000 - have['ORE'])

# Part 2
have = {k: v*1000000000000/1250000 for k, v in have.items()}
carry_on = True
# have, _ = i_need_multiple('FUEL', math.floor(1000000000000/1046184), have, data_dict)
while carry_on:
    have, carry_on = i_need('FUEL', have, data_dict)
    # print(have)

print(have['FUEL'])

# seen = {}
# no_dups = True
# while no_dups and carry_on:
#     have, carry_on = i_need('FUEL', have, data_dict)
#     print(have)
#     have_copy = copy(have)
#     ore_amt = have_copy.pop('ORE')
#     fuel_amt = have_copy.pop('FUEL')
#     if have_copy in seen.values():
#         no_dups = False
#     seen[ore_amt] = have_copy
# pass

