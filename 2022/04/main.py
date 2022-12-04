#!/bin/env python3
from icecream import ic

def contains(r1, r2):
    return r1[0] >= r2[0] and r1[1] <= r2[1]

def p1(inp):
    inp = [[list(map(int, r.split('-'))) for r in pair.split(',')] for pair in inp.splitlines()]
    ic(inp)
    n = 0
    for p in inp:
        ic(p)
        n += ic(int(contains(p[0], p[1]) or contains(p[1], p[0])))
    return n

def overlap(r1, r2):
    return r1[0] <= r2[0] <= r1[1] or r1[0] <= r2[1] <= r1[1] or contains(r1, r2) or contains (r2, r1)

def p2(inp):
    inp = [[list(map(int, r.split('-'))) for r in pair.split(',')] for pair in inp.splitlines()]
    ic(inp)
    n = 0
    for p in inp:
        ic(p)
        n += ic(int(overlap(p[0], p[1])))
    return n

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not 'test' in sys.argv:
        ic.disable()
        pass
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
