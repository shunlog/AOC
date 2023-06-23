#!/bin/env python3
from icecream import ic

def p1(inp):
    ls = [(s[0], int(s[1:])) for s in inp.split(', ')]
    ic(ls)

    # dir is in range 0..3:
    # 0 - north
    # 1 - east
    # 2 - south
    # 3 - west

    dir = 0
    pos = [0, 0]
    for rot, steps in ls:
        if rot == 'R':
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4

        if dir == 0:
            pos[1] += steps
        elif dir == 1:
            pos[0] += steps
        elif dir == 2:
            pos[1] -= steps
        elif dir == 3:
            pos[0] -= steps

    return abs(pos[0]) + abs(pos[1])


def p2(inp):
    return 0

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
