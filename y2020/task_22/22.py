from copy import copy
from typing import List

from Helpers.helpers import read_newest


class Deck:
    def __init__(self, cards: List[int]):
        self.deck = cards

    def draw(self):
        card = self.deck[0]
        self.deck = self.deck[1:]
        return card

    def add(self, cards: List[int]):
        for card in cards:
            self.deck.append(card)

    def is_not_empty(self):
        return bool(self.deck)


def compare(c1, c2):
    if c1 > c2:
        return [c1, c2], []
    elif c1 < c2:
        return [], [c2, c1]


def play_game(p1, p2, depth=0):
    # print("Entered play game")
    depth += 1
    counter = 0
    visited_states = set()
    while p1.is_not_empty() and p2.is_not_empty():
        counter += 1
        if depth == 1:
            print(counter)
        if (tuple(p1.deck), tuple(p2.deck)) in visited_states:
            p1.deck += p2.deck
            p2.deck = []
            print("depth {}, counter {}: loop".format(depth, counter))
            return p1, p2
        visited_states.add((tuple(p1.deck), tuple(p2.deck)))
        card1 = p1.draw()
        card2 = p2.draw()
        if len(p1.deck) >= card1 and len(p2.deck) >= card2:
            p1res, p2res = play_game(copy(p1), copy(p2), depth)
            if p1res.deck:
                # print("P1 wins")
                p1.add([card1, card2])
            else:
                # print("P2 wins")
                p2.add([card2, card1])
        else:
            res1, res2 = compare(card1, card2)
            p1.add(res1)
            p2.add(res2)
        # print(p1.deck)
        # print(p2.deck)
    print("depth {}, counter {}: loop".format(depth, counter))
    return p1, p2


if __name__ == '__main__':
    data = read_newest()
#     data = '''Player 1:
# 9
# 2
# 6
# 3
# 1
#
# Player 2:
# 5
# 8
# 4
# 7
# 10'''.split('\n')
    target = True
    deck1 = []
    deck2 = []
    for card in data[1:]:
        if card.isdigit():
            if target:
                deck1.append(int(card))
            else:
                deck2.append(int(card))
        else:
            target = False
    # Part 1
    me = Deck(deck1)
    crab = Deck(deck2)
    counter = 0
    while me.is_not_empty() and crab.is_not_empty():
        res1, res2 = compare(me.draw(), crab.draw())
        me.add(res1)
        crab.add(res2)
    print(sum([(x+1) * card for x, card in enumerate(me.deck[::-1])]))
    print(sum([(x+1) * card for x, card in enumerate(crab.deck[::-1])]))

    # Part 2
    me = Deck(deck1)
    crab = Deck(deck2)
    me, crab = play_game(me, crab)
    print(sum([(x+1) * card for x, card in enumerate(me.deck[::-1])]))
    print(sum([(x+1) * card for x, card in enumerate(crab.deck[::-1])]))
