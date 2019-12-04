def incrs(num):
    sort = sorted([char for char in str(num)])
    return int(''.join(sort)) == num


def double(num):
    lst = [char for char in str(num)]
    return any([lst[i] == lst[i+1] for i in range(len(lst)-1)])


def double_not_triple(num):
    lst = ["a"]
    lst.extend([char for char in str(num)])
    lst.append("a")
    return any([lst[i] == lst[i+1]
                and lst[i-1] != lst[i]
                and lst[i+1] != lst[i+2]
                for i in range(1, len(lst)-2)])


possible_a = 0
possible_b = 0
for num in range(165432, 707912):
    if incrs(num) and double(num):
        possible_a += 1
        if double_not_triple(num):
            possible_b += 1

print("Part 1: ", possible_a)
print("Part 2: ", possible_b)
