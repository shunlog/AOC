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

def move_head(p, d):
    if d == 'R':
        p[0] += 1
    elif d == 'L':
        p[0] -= 1
    elif d == 'U':
        p[1] -= 1
    elif d == 'D':
        p[1] += 1
    return p

def sign(n):
    return 1 if n >= 0 else -1

def far(a, b):
    return abs(a[0]-b[0]) > 1 or abs(a[1]-b[1]) > 1

def follow(b, a):
    if far(a, b):
        if abs(a[0] - b[0]) > 0:
            b[0] += 1 * sign(a[0] - b[0])
        if abs(a[1] - b[1]) > 0:
            b[1] += 1 * sign(a[1] - b[1])
    return b

def p2(inp):
    inp = inp.splitlines()
    pk = [[0, 0] for i in range(10)]
    v = dict()
    v[tuple(pk[-1])] = True

    for l in inp:
        d, s = l.split()
        for i in range(int(s)):
            pk[0] = move_head(pk[0], d)
            for n in range(1, 10):
                pk[n] = follow(pk[n], pk[n-1])
            v[tuple(pk[-1])] = True
    return len(v.keys())

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
