#!/bin/env python3
from icecream import ic
import math

def count_colors(s):
    # "3 blue, 4 red" --> (4, 0, 3)
    d = {'red': 0, 'green': 0, 'blue': 0}
    for p in s.split(','):
        n, col = p.split()
        d[col] = int(n)
    return (d['red'], d['green'], d['blue'])


def p1(l):
    def impossible(t):
        # (20, 0, 0) --> True
        if t[0] > 12 or t[1] > 13 or t[2] > 14:
            return True
        return False

    left, right = l.split(":")
    gid = int(left.split()[-1]) # game id
    trips = [count_colors(s) for s in right.split(";")] # list of triples (r, g, b)
    for trip in trips:
        if impossible(trip):
            return 0
    return gid


def p2(l):
    left, right = l.split(":")
    trips = [count_colors(s) for s in right.split(";")] # list of triples (r, g, b)
    minset = [0, 0, 0]
    for trip in trips:
        for i in range(3):
            minset[i] = max(minset[i], trip[i])
    return math.prod(minset)


def solve(inp, part2=False):
    foo = p2 if part2 else p1
    return sum(foo(l) for l in inp.splitlines())


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
