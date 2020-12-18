from Helpers.helpers import read_newest
import re
# import os
# os.chdir("y2020/task_18")

if __name__ == '__main__':
    data = read_newest()
    # Part 1 - linear evaluation
    data = [re.sub("\(", "( ", x) for x in data]
    data = [re.sub("\)", " )", x) for x in data]
    data = [x.split(' ') for x in data]

    def operate(num, res, ope):
        if ope == '+':
            return res+num
        elif ope == '*':
            return res*num

    def evaluate(equation):
        operation = '+'
        result = 0
        in_parenthesis = 0
        for idx, ch in enumerate(equation):
            if in_parenthesis < 0:
                print(result)
                return result
            if in_parenthesis > 0:
                if ch == ')':
                    in_parenthesis -= 1
                elif ch == '(':
                    in_parenthesis += 1
                continue
            if ch == '*':
                operation = '*'
            elif ch == '+':
                operation = '+'
            elif ch == '(':
                in_parenthesis += 1
                result = operate(evaluate(equation[idx+1:]), result, operation)
            elif ch == ')':
                print(result)
                return result
            else:
                result = operate(int(ch), result, operation)
        return result

    # print(evaluate('( ( 2 + 4 * 9 ) * ( 6 + 9 * 8 + 6 ) + 6 ) + 2 + 4 * 2'.split(' ')))
    res = [evaluate(x) for x in data]
    print(sum(res))

    # Part 2
    def evaluate2(equation):
        inner_eq = []
        in_parenthesis = 0
        for idx, ch in enumerate(equation):
            if in_parenthesis < 0:
                print(inner_eq)
                return evaluate_no_par(inner_eq)
            if in_parenthesis > 0:
                if ch == ')':
                    in_parenthesis -= 1
                elif ch == '(':
                    in_parenthesis += 1
                continue
            if ch == '(':
                in_parenthesis += 1
                inner_eq.append(str(evaluate2(equation[idx + 1:])))
            elif ch == ')':
                print(inner_eq)
                return evaluate_no_par(inner_eq)
            else:
                inner_eq.append(ch)
        return evaluate_no_par(inner_eq)

    def evaluate_no_par(inner_eq):
        # Add ()
        eq = ''.join(inner_eq)
        return eval(re.sub(r"([0-9+]+)", r"(\1)", eq))

    # evaluate2("( ( 2 + 4 * 9 ) * ( 6 + 9 * 8 + 6 ) + 6 ) + 2 + 4 * 2".split(' '))
    res = [evaluate2(x) for x in data]
    print(sum(res))
