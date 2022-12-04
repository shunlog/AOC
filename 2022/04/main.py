#!/bin/env python3
from icecream import ic

def contains(r1, r2):
    return r1[0] >= r2[0] and r1[1] <= r2[1]

def p1(inp):
    inp = [[list(map(int, r.split('-'))) for r in pair.split(',')] for pair in inp.splitlines()]
    contain = lambda p: contains(p[0], p[1]) or contains(p[1], p[0])
    return sum(map(contain, inp))

def overlap(r1, r2):
    return not (r1[1] < r2[0] or r1[0] > r2[1])

def p2(inp):
    inp = [[list(map(int, r.split('-'))) for r in pair.split(',')] for pair in inp.splitlines()]
    return sum(map(lambda p: int(overlap(*p)), inp))

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
