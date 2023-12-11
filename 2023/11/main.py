#!/bin/env python3
from icecream import ic
from itertools import combinations
from functools import cache

@cache
def compute_actual_dist(m, expansion):
    '''For any x and y on which there is a galaxy,
    actual_x[x] = actual x after expansion
    actual_y[y] = actual y after expansion
    '''
    w, h = len(m[0]), len(m)
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

    return actual_x, actual_y


def manhattan_dist(m, expansion, g1, g2):
    actual_x, actual_y = compute_actual_dist(m, expansion)
    dx = abs(actual_x[g1[0]] - actual_x[g2[0]])
    dy = abs(actual_y[g1[1]] - actual_y[g2[1]])
    return dx + dy


def solve(inp, part2=False):
    expansion = 1000000-1 if part2 else 1
    m = tuple(inp.splitlines())  # needs to be hashable
    galaxies = {(x, y) for y, r in enumerate(m) for x, ch in enumerate(r) if ch == '#'}
    return sum(manhattan_dist(m, expansion, g1, g2) for g1, g2 in combinations(galaxies, 2))


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
