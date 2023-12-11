#!/bin/env python3
from icecream import ic
from itertools import combinations


def solve(inp, part2=False):
    expansion = 1000000-1 if part2 else 1

    m = [list(row) for row in inp.splitlines()]
    w, h = len(m[0]), len(m)

    rows_empty = set(y for y, r in enumerate(m) if all(ch == '.' for ch in r))
    cols_empty = set(x for x in range(w) if all(m[y][x] == '.' for y in range(h)))

    galaxies = {(x, y) for y, r in enumerate(m) for x, ch in enumerate(r) if ch == '#'}
    ic(galaxies)
    ic(len(list(combinations(galaxies, 2))))

    # for any x on which there is a galaxy,
    # actual_x[x] = actual distance from 0
    actual_y = {}
    offset = 0
    for y, row in enumerate(m):
        if all(ch == '.' for ch in row):
            offset += expansion
        else:
            actual_y[y] = y + offset

    actual_x = {}
    offset = 0
    for x in range(w):
        if all (m[y][x] == '.' for y in range(h)):
            offset += expansion
        else:
            actual_x[x] = x + offset


    s = 0
    for g1, g2 in combinations(galaxies, 2):
        dx = abs(actual_x[g1[0]] - actual_x[g2[0]])
        dy = abs(actual_y[g1[1]] - actual_y[g2[1]])
        dist = dx + dy
        s += dist

    # for each pair of galaxies: 96141
    # * for each pair of rows + columns:  combi(140, 2) = 9730 * 2 = 18k

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
