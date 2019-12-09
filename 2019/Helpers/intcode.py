
def mode(mod, ele, data):
    if mod == '0':
        return data[ele]
    elif mod == '1':
        return ele
    else:
        raise ValueError("Wrong mode")


def op01(a, b, c, data, idx):
    data[c] = a+b
    return data, idx+4


def op02(a, b, c, data, idx):
    data[c] = a*b
    return data, idx+4


def op03(a, data, idx, inpt=None, phase=None):
    if phase is not None:
        data[a] = phase
        phase = None
    elif phase is None and inpt is not None:
        data[a] = inpt
        inpt = None
    else:
        data[a] = int(input("Input needed: "))
    return data, idx+2, inpt, phase


def op04(a, data, idx):
    # print(a)
    return data, idx+2, a


def op05(a, b, data, idx):
    if a != 0:
        return data, b
    return data, idx + 3


def op06(a, b, data, idx):
    if a == 0:
        return data, b
    return data, idx + 3


def op07(a, b, c, data, idx):
    if a < b:
        data[c] = 1
    else:
        data[c] = 0
    return data, idx+4


def op08(a, b, c, data, idx):
    if a == b:
        data[c] = 1
    else:
        data[c] = 0
    return data, idx+4


def parse_op(data, idx, iterate, inpt=None, phase=None, output=None):
    opcode = str(data[idx]).zfill(5)
    if opcode[3:] == '01':
        param1 = mode(opcode[2], data[idx + 1], data)
        param2 = mode(opcode[1], data[idx + 2], data)
        param3 = data[idx + 3]
        data, idx = op01(param1, param2, param3, data, idx)
    elif opcode[3:] == '02':
        param1 = mode(opcode[2], data[idx + 1], data)
        param2 = mode(opcode[1], data[idx + 2], data)
        param3 = data[idx + 3]
        data, idx = op02(param1, param2, param3, data, idx)
    elif opcode[3:] == '03':
        param1 = data[idx + 1]
        data, idx, inpt, phase = op03(param1, data, idx, inpt, phase)
    elif opcode[3:] == '04':
        param1 = mode(opcode[2], data[idx + 1], data)
        data, idx, output = op04(param1, data, idx)
    elif opcode[3:] == '05':
        param1 = mode(opcode[2], data[idx + 1], data)
        param2 = mode(opcode[1], data[idx + 2], data)
        data, idx = op05(param1, param2, data, idx)
    elif opcode[3:] == '06':
        param1 = mode(opcode[2], data[idx + 1], data)
        param2 = mode(opcode[1], data[idx + 2], data)
        data, idx = op06(param1, param2, data, idx)
    elif opcode[3:] == '07':
        param1 = mode(opcode[2], data[idx + 1], data)
        param2 = mode(opcode[1], data[idx + 2], data)
        param3 = data[idx + 3]
        data, idx = op07(param1, param2, param3, data, idx)
    elif opcode[3:] == '08':
        param1 = mode(opcode[2], data[idx + 1], data)
        param2 = mode(opcode[1], data[idx + 2], data)
        param3 = data[idx + 3]
        data, idx = op08(param1, param2, param3, data, idx)
    elif opcode[3:] == '99':
        iterate = False
    else:
        raise ValueError('Incorect instruction')
    return data, idx, iterate, inpt, phase, output
