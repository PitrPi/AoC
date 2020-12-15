import os
from time import sleep
from conway import Conway
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        inpt = 'input.txt'
    else:
        inpt = sys.argv[1]
    with open(inpt) as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    cnw = Conway(data)
    while True:
        cnw.print()
        cnw.step()
        sleep(0.2)
        os.system('cls')
