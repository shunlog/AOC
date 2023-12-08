#!/bin/env python3
from icecream import ic
from collections import Counter
from itertools import chain


def hand_type(h, part2=False):
    '''There are 7 types of hands:
    0. Five of a kind
    1. Four of a kind
    2. Full house
    3. Three of a kind
    4. Two pair
    5. One pair
    6. High card
    '''
    c = Counter(h)
    if part2 and c['J']: # convert all J's to the most common card
        mc = c.most_common(2)
        if len(mc) < 2: # there's only jokers
            return 0
        else:
            # pick the most-common non-J card
            mc_card = mc[0][0] if mc[0][0] != 'J' else mc[1][0]
            c.update({mc_card: c['J']})
            del c['J']

    if len(c) == 1:
        return 0
    if sorted(c.values()) == [1, 4]:
        return 1
    if sorted(c.values()) == [2, 3]:
        return 2
    if sorted(c.values()) == [1, 1, 3]:
        return 3
    if sorted(c.values()) == [1, 2, 2]:
        return 4
    if len(c) == 4:
        return 5
    if len(c) == 5:
        return 6
    assert False


def test_hand_type():
    assert hand_type('AAAAA') == 0
    assert hand_type('AA2AA') == 1
    assert hand_type('23332') == 2
    assert hand_type('TTT98') == 3
    assert hand_type('23432') == 4
    assert hand_type('A23A4') == 5
    assert hand_type('23456') == 6

    assert hand_type('AAAAA', True) == 0
    assert hand_type('T55J5', True) == 1
    assert hand_type('KTJJT', True) == 1
    assert hand_type('QQQJA', True) == 1


def key_func(h, part2=False):
    '''Transform a hand into a string,
    such that you could use it to sort hands
    Numbers are already fine, so we just need to replace these with characters:
    A, K, Q, J, T ->
    E, D, C, B, A
    '''
    J_subst = 'B' if not part2 else '1' # in part2, Jokers are rated the lowest
    return h.replace('A', 'E')\
        .replace('K', 'D')\
        .replace('Q', 'C')\
        .replace('J', J_subst)\
        .replace('T', 'A')

def solve(inp, part2=False):
    test_hand_type()

    d = {hand: int(bid) for hand, bid in (l.split() for l in inp.splitlines())}
    groups = [[] for _ in range(7)]

    # sort the hands by type
    for hand in d.keys():
        t = hand_type(hand, part2)
        groups[6-t].append(hand) # store them in reverse order

    # sort the hands in each group
    for l in groups:
        l.sort(key=lambda h: key_func(h, part2))

    s = 0
    for rank, hand in enumerate(chain(*groups), start=1):
        s += d[hand] * rank

    return s


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
