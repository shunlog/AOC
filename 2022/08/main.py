#!/bin/env python3
from icecream import ic

def transpose(l):
    return list(map(list,zip(*l)))

def p1(inp):
    hm = [[int(n) for n in l] for l in inp.splitlines()]
    W = len(hm[0])
    H = len(hm)
    ic(hm)
    v = [[False] * W for i in range(H)]

    for y in range(H):
        maxh = -1
        for i,h in enumerate(hm[y]):
            if h > maxh:
                maxh = h
                v[y][i] = True

    for y in range(H):
        maxh = -1
        for i,h in zip(range(W-1,0-1,-1),hm[y][::-1]):
            if h > maxh:
                maxh = h
                v[y][i] = True

    hm = transpose(hm)
    v = transpose(v)

    for y in range(H):
        maxh = -1
        for i,h in enumerate(hm[y]):
            if h > maxh:
                maxh = h
                v[y][i] = True

    for y in range(H):
        maxh = -1
        for i,h in zip(range(W-1,0-1,-1),hm[y][::-1]):
            if h > maxh:
                maxh = h
                v[y][i] = True

    hm = transpose(hm)
    v = transpose(v)

    ic(v)
    vc = 0
    for i in v:
        for j in i:
            vc += int(j)

    return vc

def swallow(l, n):
    for i,v in enumerate(l):
        if n <= v:
            return [n]+l[i:]
    return [n]


def it(r1, r2, hm, v):
    for y in r1:
        vh = []
        for x in r2:
            h = hm[y][x]
            vh2 = []
            for i in vh:
                if i >= h:
                    vh2.append(i)
                    break
                vh2.append(i)
            v[y][x].append(len(vh2))
            vh = [h] + vh

from functools import reduce
import operator

def p2(inp):
    hm = [[int(n) for n in l] for l in inp.splitlines()]
    W = len(hm[0])
    H = len(hm)
    ic(hm)
    # each square is the array of # of trees seen in each dir
    v = [[[] for j in range(W)] for i in range(H)]

    it(range(H), range(W), hm, v)
    it(range(H), range(W-1,0-1,-1), hm, v)

    hm = transpose(hm)
    v = transpose(v)

    it(range(H), range(W), hm, v)
    it(range(H), range(W-1,0-1,-1), hm, v)

    hm = transpose(hm)
    v = transpose(v)

    ic(v)
    p = [[reduce(operator.mul, vt, 1) for vt in l] for l in v]
    ic(p)
    maxv = max([max(l) for l in p])
    return maxv

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
