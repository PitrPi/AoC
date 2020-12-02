def read_newest(file=None):
    if file is None:
        latest = 'input.txt'
    else:
        latest = file + '.txt'
    with open(latest) as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    return data


def read_newest_int(file=None):
    return [int(x) for x in read_newest(file)]


def read_newest_int_list(file=None):
    data = read_newest(file)[0].split(',')
    return [int(x) for x in data]


def read_newest_list(file=None):
    data = read_newest(file)[0].split(',')
    return data


