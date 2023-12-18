#!/bin/env python3
from icecream import ic
from copy import deepcopy


RIGHT = (1, 0)
LEFT = (-1, 0)
UP = (0, -1)
DOWN = (0, 1)


def roll(m, dirn):
    w, h = len(m[0]), len(m)

    def roll_rock(x, y):
        nx, ny = x + dirn[0], y + dirn[1]
        if nx not in range(w) or ny not in range(h):
            return
        if m[ny][nx] != '.':
            return

        m[y][x] = '.'
        m[ny][nx] = 'O'
        roll_rock(nx, ny)

        return

    # have to roll each rock in the appropriate order
    if dirn == UP:
            coords = ((x, y) for y in range(h) for x in range(w))
    elif dirn == DOWN:
            coords = ((x, y) for x in range(w) for y in range(h-1, -1, -1))
    elif dirn == LEFT:
            coords = ((x, y) for y in range(h) for x in range(w))
    elif dirn == RIGHT:
            coords = ((x, y) for y in range(h) for x in range(w-1, -1, -1))

    for (x, y) in coords:
            if m[y][x] != 'O':
                continue
            roll_rock(x, y)


def load(m):
    s = 0
    h = len(m)
    for row, l in enumerate(m):
        for ch in l:
            if ch == 'O':
                s += (h - row)
    return s


def roll_cycle(m):
    roll(m, UP)
    roll(m, LEFT)
    roll(m, DOWN)
    roll(m, RIGHT)


def solve(inp, part2=False):
    m = [list(l) for l in inp.splitlines()]

    if not part2:
        roll(m, UP)
        return load(m)

    mincycle = 101  # guessed 100, but lower didn't work
    cycles = 1000000000

    # do some iterations until it starts cycling
    for i in range(mincycle):
        roll_cycle(m)

    # find the length of a cycle
    oldm = deepcopy(m)
    for i in range(mincycle+1, cycles):
        roll_cycle(m)
        if oldm == m:
            lencycle = i - mincycle
            break

    # do the last few iterations
    left = (cycles - mincycle) % lencycle
    for i in range(left):
        roll_cycle(m)

    return load(m)



if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
