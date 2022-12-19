#!/bin/env python3
import re
from icecream import ic
import math

def ints(s):
    return [int(i) for i in re.findall(r'-?\d+', s)]

from collections import defaultdict
mem = None

def bfs(bp, ores, bots, t):
    '''Return the maximum number of geodes produced from current time till end'''
    if t > 24:
        return ores
    return ores


def p1(inp):
    bpl = []
    for l in inp.splitlines():
        il = ints(l)
        assert(len(il) == 7)
        o1, c1, ob1, ob2, g1, g3 = il[1:]
        bpl.append(((o1, 0, 0, 0), (c1, 0, 0, 0),
                    (ob1, ob2, 0, 0), (g1, 0, g3, 0)))

    for bp in bpl:
        global mem
        mem = defaultdict(lambda: tuple([-1, -1, -1, -1]))
        v = bfs(bp, (0, 0, 0, 0), (1, 0, 0, 0), 1)
        ic(bp, v)

    return 0

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
