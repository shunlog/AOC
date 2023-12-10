#!/bin/env python3
from icecream import ic


def find_S(m):
    for y, row in enumerate(m):
        for x, ch in enumerate(row):
            if ch == 'S':
                return (x, y)


def find_next_pipe(m, pos, prev=None):
    enters = { # the directions in which you can enter the pipe
        '-': ((1, 0), (-1, 0)),
        '|': ((0, 1), (0, -1)),
        'F': ((-1, 0), (0, -1)),
        'L': ((0, 1), (-1, 0)),
        'J': ((0, 1), (1, 0)),
        '7': ((0, -1), (1, 0)),
        'S': ((-1, 0), (1, 0), (0, -1), (0, 1))
    }
    exits = { # the directions in which you can exit the pipe
        '-': ((1, 0), (-1, 0)),
        '|': ((0, 1), (0, -1)),
        'F': ((1, 0), (0, 1)),
        'L': ((1, 0), (0, -1)),
        'J': ((0, -1), (-1, 0)),
        '7': ((0, 1), (-1, 0)),
        'S': ((-1, 0), (1, 0), (0, -1), (0, 1))
    }

    x, y = pos
    ch = m[y][x]
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = x + dx, y + dy
        if (nx, ny) == prev:
            continue
        try:
            nch = m[ny][nx]
        except:
            continue
        if (dx, dy) not in exits[ch]: # can't exit the pipe in that direction
            continue
        if nch != '.' and (dx, dy) in enters[nch]:
            return (nx, ny)


def solve(inp, part2=False):
    m = inp.splitlines()
    S = find_S(m)

    path = []
    pos = S
    prev = None
    ic(pos)
    while True:
        path.append(pos)
        prev, pos = pos, find_next_pipe(m, pos, prev)
        ch = m[pos[1]][pos[0]]
        prev_ch = m[prev[1]][prev[0]]
        # ic(prev_ch, ch)
        if ch == 'S':
            break

    ic(len(path))

    return len(path) // 2


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
