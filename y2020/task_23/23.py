if __name__ == '__main__':

    l = [int(x) for x in "364297581"]
    # l = [int(x) for x in "389125467"]
    idx = 0
    target = l[0]-1
    MAX_L = max(l)
    ORIG_LEN = len(l)


    def get_target_index(l, target):
        while True:
            try:
                idx = l.index(target)
                return idx+1
            except ValueError:
                target -= 1
                if target <= 0:
                    target = MAX_L
    for _ in range(100):
        picked = l[1:4]
        l = l[:1] + l[4:]
        target_idx = get_target_index(l, target)
        l = l[0:target_idx] + picked + l[target_idx:]
        idx = ((l.index(target+1)+1)) % ORIG_LEN
        target = l[idx]-1
        l = l[idx:]+l[:idx]
    print(l[l.index(1):] + l[:l.index(1)])

    # Part 2 - crazy slow
    """
    import time
    start_time = time.time()
    l = [int(x) for x in "364297581"]
    l.extend(range(10, 1000001))
    idx = 0
    target = l[0]-1
    MAX_L = max(l)
    ORIG_LEN = len(l)
    for cycle in range(10000000):
        picked = l[1:4]
        l = l[:1] + l[4:]
        target_idx = get_target_index(l, target)
        l = l[0:target_idx] + picked + l[target_idx:]
        idx = ((l.index(target+1)+1)) % ORIG_LEN
        target = l[idx]-1
        l = l[idx:]+l[:idx]
        print(l)
        if cycle % 100 == 0:
            print(time.time()-start_time)
            start_time = time.time()

    # print(l[l.index(1):] + l[:l.index(1)])
    l = l[l.index(1):] + l[:l.index(1)]
    print(l[1]*l[2])
    """
    # Part 2 - pointer approach
    class Cup:
        def __init__(self, this, prev=None, next=None):
            self.this = this
            if prev is None:
                self.prev = this - 1
            else:
                self.prev = prev
            if next is None:
                self.next = this + 1
            else:
                self.next = next

    cups = {i: Cup(i) for i in range(1, 1000001)}
    start = l
    for i, c in enumerate(start):
        if i == 0:
            cups[c].prev = 1000000
        else:
            cups[c].prev = start[i-1]
        if i+1 == len(l):
            cups[c].next = len(l)+1
        else:
            cups[c].next = start[i+1]
    cups[1000000].next = start[0]

    current_cup = l[0]
    for cycle in range(9999999):
        picked_cups = [cups[current_cup].next]
        for _ in range(2):
            picked_cups.append(cups[picked_cups[-1]].next)
        target_cup = current_cup-1
        while target_cup in picked_cups:
            target_cup -= 1
        if target_cup == 0:
            target_cup = len(cups)
        while target_cup in picked_cups:
            target_cup -= 1
        # Insert
        cups[current_cup].next = cups[picked_cups[-1]].next
        cups[cups[current_cup].next].prev = current_cup

        cups[picked_cups[-1]].next = cups[target_cup].next
        cups[cups[target_cup].next].prev = cups[picked_cups[-1]]
        cups[target_cup].next = picked_cups[0]
        cups[picked_cups[0]].prev = target_cup
        current_cup = cups[current_cup].next
    printable = [1]
    for _ in range(8):
        printable.append(cups[printable[-1]].next)
    print(printable)
    print(printable[1]*printable[2])


