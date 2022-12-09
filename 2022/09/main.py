#!/bin/env python3
from icecream import ic
from collections import defaultdict

move = {'U': [0, -1],
        'R': [1, 0],
        'D': [0, 1],
        'L': [-1, 0]}

def dist(a, b):
    return max(abs(a[0] - b[0]), abs(a[1]-b[1]))

def addd(a, b):
    return a[0]+b[0],a[1]+b[1]

def p1(inp):
    ins = [(l.split()[0],int(l.split()[1])) for l in inp.splitlines()]
    v = defaultdict(int)
    ph = (0, 0)
    pt = (0, 0)
    v[pt] += 1
    ic(ins)
    for d,s in ins:
        for i in range(s):
            pph = ph
            ph = addd(ph, move[d])
            if dist(ph, pt) > 1:
                pt = pph
                v[pt] += 1
    ic(v)
    return len(v.keys())

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
