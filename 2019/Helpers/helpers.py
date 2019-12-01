import os
import glob


def read_newest():
    latest = max(glob.glob('../Data/*'), key=os.path.getctime)
    with open(latest) as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    return data


def read_newest_int():
    return [int(x) for x in read_newest()]
