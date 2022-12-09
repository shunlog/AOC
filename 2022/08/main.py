#!/bin/env python3
from icecream import ic

def visible_in_line(l):
    mx = -1
    v = []
    for h in l:
        v.append(True if h > mx else False)
        mx = max(h, mx)
    return v

def p1(inp):
    inp = [[int(n) for n in l] for l in inp.splitlines()]
    s = len(inp)
    v = [[False] * s for i in range(s)]
    for n in range(s):
        for i in range(s):
            v[n][i] |= visible_in_line((inp[n][i] for i in range(s)))[i]
            v[n][i] |= visible_in_line((inp[n][i] for i in range(s-1,-1,-1)))[s-i-1]
            v[i][n] |= visible_in_line((inp[i][n] for i in range(s)))[i]
            v[i][n] |= visible_in_line((inp[i][n] for i in range(s-1,-1,-1)))[s-i-1]

    return sum([sum(map(int, l)) for l in v])

def transpose(l):
    return list(map(list,zip(*l)))

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
