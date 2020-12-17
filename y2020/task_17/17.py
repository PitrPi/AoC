from Helpers.conway import Conway3D, Conway4D
from Helpers.helpers import read_newest

if __name__ == '__main__':
    data = read_newest()
    c3d = Conway3D(dead='.', alive='#', static=' ')
    c3d.insert_initial_board(data)
    print(c3d.counter())
    c3d.print()
    for _ in range(6):
        c3d.step()
        c3d.print()
        print(c3d.counter())

    c4d = Conway4D(dead='.', alive='#', static=' ')
    c4d.insert_initial_board(data)
    print(c4d.counter())
    for _ in range(6):
        c4d.step()
        print(c4d.counter())
