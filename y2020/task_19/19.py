import re

from Helpers.helpers import read_newest
# import os
# os.chdir('y2020/task_19')


def check_msg(msg, regex):
    if re.match('^'+regex+'$', msg):
        return True
    else:
        return False


class Ruler:
    def __init__(self, data):
        self.rules, self.messages = self.parse_data(data)
        pass

    @staticmethod
    def parse_data(data):
        final_rules = {}
        final_msgs = []
        rules = True
        for dat in data:
            if dat == '':
                rules = False
                continue
            if rules:
                k, v = "", [[]]
                counter = 0
                for itm in dat.split(' '):
                    if itm[-1] == ":":
                        k = itm[:-1]
                    elif itm == '|':
                        counter += 1
                        v.append([])
                    else:
                        v[counter].append(itm)
                final_rules[k] = v
            else:
                final_msgs.append(dat)
        return final_rules, final_msgs

    def rule_to_regex(self, rule_num):
        rules = self.rules[rule_num]
        check_strings = []
        for rules_variant in rules:
            check_string = ''
            for rule in rules_variant:
                if rule.isnumeric():
                    check_string += '('+self.rule_to_regex(rule)+')'
                else:
                    check_string += rule[1]  # char is quoted
            check_strings.append(check_string)
        final_regex = '|'.join(check_strings)
        return final_regex

    def check_msgs(self, regex, count=True):
        cr = re.compile('^'+regex+'$')
        correct = []
        for msg in self.messages:
            if cr.match(msg):
                correct.append(True)
            else:
                correct.append(False)
        if count:
            return sum(correct)
        else:
            return correct


def use_data(idx=None):
    if idx is None or idx == 1:
        data = read_newest()
    elif idx == 2:
        data = '''0: 4 1 5
        1: 2 3 | 3 2
        2: 4 4 | 5 5
        3: 4 5 | 5 4
        4: "a"
        5: "b"

        ababbb
        bababa
        abbbab
        aaabbb
        aaaabbb'''.split('\n')
    elif idx == 3:
        data = '''42: 9 14 | 10 1
        9: 14 27 | 1 26
        10: 23 14 | 28 1
        1: "a"
        11: 42 31
        5: 1 14 | 15 1
        19: 14 1 | 14 14
        12: 24 14 | 19 1
        16: 15 1 | 14 14
        31: 14 17 | 1 13
        6: 14 14 | 1 14
        2: 1 24 | 14 4
        0: 8 11
        13: 14 3 | 1 12
        15: 1 | 14
        17: 14 2 | 1 7
        23: 25 1 | 22 14
        28: 16 1
        4: 1 1
        20: 14 14 | 1 15
        3: 5 14 | 16 1
        27: 1 6 | 14 18
        14: "b"
        21: 14 1 | 1 14
        25: 1 1 | 1 14
        22: 14 14
        8: 42
        26: 14 22 | 1 20
        18: 15 15
        7: 14 5 | 1 21
        24: 14 1

        abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
        bbabbbbaabaabba
        babbbbaabbbbbabbbbbbaabaaabaaa
        aaabbbbbbaaaabaababaabababbabaaabbababababaaa
        bbbbbbbaaaabbbbaaabbabaaa
        bbbababbbbaaaaaaaabbababaaababaabab
        ababaaaaaabaaab
        ababaaaaabbbaba
        baabbaaaabbaaaababbaababb
        abbbbabbbbaaaababbbbbbaaaababb
        aaaaabbaabaaaaababaa
        aaaabbaaaabbaaa
        aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
        babaaabbbaaabaababbaabababaaab
        aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'''.split('\n')
        d
    return data


if __name__ == '__main__':
    data = use_data()
    r = Ruler(data)
    regex = (r.rule_to_regex('0'))
    # Part 1
    print(r.check_msgs(regex))

    # Part 2 - new rules are used only in rule 0
    regex42 = r.rule_to_regex('42')
    regex31 = r.rule_to_regex('31')
    regex8 = r.rule_to_regex('8')
    part2 = []
    for i in range(1, 11):  # iterate over reasonable number of repetitions
        part2.append(r.check_msgs('(' + regex8 + ')+(' + regex42 + '){' + str(i) + '}(' + regex31 + '){' + str(i) + '}', count=False))
    part2_final = []
    for arr in zip(*part2):
        part2_final.append(any(arr))
    print(sum(part2_final))
