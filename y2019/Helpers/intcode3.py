
def mode(base, mod, ele, data):
    if mod == '0':
        return data.get(ele, 0)
    elif mod == '1':
        return ele
    elif mod == '2':
        return data.get(base+ele, 0)
    else:
        raise ValueError("Wrong mode")


def op01(a, b, c, data, idx):
    data[c] = a+b
    return data, idx+4


def op02(a, b, c, data, idx):
    data[c] = a*b
    return data, idx+4


def op03(a, data, idx, inpt=None, phase=None):
    iterate = True
    if phase is not None:
        data[a] = phase
        phase = None
    elif phase is None and inpt is not None:
        data[a] = inpt
        inpt = None
    else:
        data[a] = int(input("Insert input:"))
    return data, idx+2, inpt, phase


def op04(a, data, idx):
    # print("Output:", a)
    return data, idx+2, a, False  # Stop iteration for now


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


def op09(a, idx, base):
    base += a
    return base, idx+2


def parse_op3(data, idx, iterate, inpt=None, phase=None, output=None, base=0):
    opcode = str(data.get(idx, 0)).zfill(5)
    halt = False
    if opcode[3:] == '01':
        param1 = mode(base, opcode[2], data.get(idx + 1, 0), data)
        param2 = mode(base, opcode[1], data.get(idx + 2, 0), data)
        param3 = data.get(idx + 3, 0) + base*(opcode[0] == '2')
        data, idx = op01(param1, param2, param3, data, idx)
    elif opcode[3:] == '02':
        param1 = mode(base, opcode[2], data.get(idx + 1, 0), data)
        param2 = mode(base, opcode[1], data.get(idx + 2, 0), data)
        param3 = data.get(idx + 3, 0) + base*(opcode[0] == '2')
        data, idx = op02(param1, param2, param3, data, idx)
    elif opcode[3:] == '03':
        param1 = data.get(idx + 1, 0) + base*(opcode[2] == '2')
        data, idx, inpt, phase = op03(param1, data, idx, inpt, phase)
    elif opcode[3:] == '04':
        param1 = mode(base, opcode[2], data.get(idx + 1, 0), data)
        data, idx, output, iterate = op04(param1, data, idx)
    elif opcode[3:] == '05':
        param1 = mode(base, opcode[2], data.get(idx + 1, 0), data)
        param2 = mode(base, opcode[1], data.get(idx + 2, 0), data)
        data, idx = op05(param1, param2, data, idx)
    elif opcode[3:] == '06':
        param1 = mode(base, opcode[2], data.get(idx + 1, 0), data)
        param2 = mode(base, opcode[1], data.get(idx + 2, 0), data)
        data, idx = op06(param1, param2, data, idx)
    elif opcode[3:] == '07':
        param1 = mode(base, opcode[2], data.get(idx + 1, 0), data)
        param2 = mode(base, opcode[1], data.get(idx + 2, 0), data)
        param3 = data.get(idx + 3, 0) + base*(opcode[0] == '2')
        data, idx = op07(param1, param2, param3, data, idx)
    elif opcode[3:] == '08':
        param1 = mode(base, opcode[2], data.get(idx + 1, 0), data)
        param2 = mode(base, opcode[1], data.get(idx + 2, 0), data)
        param3 = data.get(idx + 3, 0) + base*(opcode[0] == '2')
        data, idx = op08(param1, param2, param3, data, idx)
    elif opcode[3:] == '09':
        param1 = mode(base, opcode[2], data.get(idx + 1, 0), data)
        base, idx = op09(param1, idx, base)
    elif opcode[3:] == '99':
        halt = True
        iterate = False
    else:
        raise ValueError('Incorect instruction')
    return data, idx, iterate, inpt, phase, output, halt, base
