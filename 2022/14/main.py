#!/bin/env python3
from itertools import *
import re
from more_itertools import *
from icecream import ic

def ints(s):
    return [int(i) for i in re.findall(r'\d+', s)]

def segp(sg):
    '''
    Return list of points in a segment represented by two points
    '''
    xp = sg[0][0], sg[1][0]
    yp = sg[0][1], sg[1][1]
    ps = []
    for x in range(min(xp), max(xp)+1):
        for y in range(min(yp), max(yp)+1):
            ps.append((x, y))
    return ps

def fall(p, cave):
    '''
    Return the new coordinates of a sand particle at 'p',
    or None if it's already in place
    '''
    nps = [(p[0], p[1] + 1),
           (p[0] - 1, p[1] + 1),
           (p[0] + 1, p[1] + 1)]
    for np in nps:
        if not cave.get(np):
            return np
    return None

def parse(inp):
    cave = {}
    for l in inp.splitlines():
        cs = chunked(ints(l), 2)
        for sg in windowed(cs, 2):
            for p in segp(sg):
                cave[p] = '#'
    return cave

def ppcave(cave):
    minx = min(list(zip(*cave.keys()))[0])
    miny = min(list(zip(*cave.keys()))[1])
    maxx = max(list(zip(*cave.keys()))[0])
    maxy = max(list(zip(*cave.keys()))[1])
    for y in range(miny, maxy):
        for x in range(minx, maxx):
            ch = cave.get((x, y))
            ch = ' ' if not ch else ch
            print(ch, end='')
        print()

def p1(inp):
    cave = parse(inp)
    maxy = max(list(zip(*cave.keys()))[1])

    p = (500, 0)
    while True:
        np = fall(p, cave)
        if not np:
            cave[p] = 'o'
            p = (500, 0)
            continue
        if np[1] > maxy:
            break
        p = fall(p, cave)

    return list(cave.values()).count('o')

def p2(inp):
    cave = parse(inp)
    maxy = max(list(zip(*cave.keys()))[1])
    for x in range(0, 1000):
        cave[(x, maxy+2)] = '#'

    p = (500, 0)
    while True:
        np = fall(p, cave)
        if not np:
            cave[p] = 'o'
            if p == (500, 0):
                break
            p = (500, 0)
            continue
        p = fall(p, cave)

    return list(cave.values()).count('o')

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
