from Helpers.helpers import read_newest
# import os
# os.chdir('y2020/task_19')
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

    def check_rule(self, msg, rule_num, idx=0):
        rules = self.rules[rule_num]
        for rules_variant in rules:
            check_string = ''
            for rule in rules_variant:
                if rule.isnumeric():
                    check_rule(rule)
                else:
                    check_string += rule

if __name__ == '__main__':

    data = read_newest()

    def check_rule(msg, rule):
