door = 1717001
key = 523731
snum = 7
key_num = 1
for i in range(10000000):
    key_num *= snum
    key_num %= 20201227
    if key_num == key:
        break

key_num = 1
snum = 1717001
for j in range(i+1):
    key_num *= snum
    key_num %= 20201227
