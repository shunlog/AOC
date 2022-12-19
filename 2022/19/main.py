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
    memores = mem[tuple([bots, t])]
    if all(memo >= o for memo, o in zip(memores, ores)):
        return memores

    oldores = ores
    ores = tuple(o+b for o,b in zip(ores, bots))

    maxores = ores
    bestbots = bots

    newores = bfs(bp, ores, bots, t+1)
    if maxores[-1] <= newores[-1]:
        maxores = newores
        bestbots = bots

    for bi,botbp in enumerate(bp):
        if not all(oldores[i] >= botbp[i] for i in range(4)):
            continue
        newores = tuple(ore - bpore for ore, bpore in zip(ores, botbp))
        newbots = tuple(bc + 1 if i == bi else bc for i,bc in enumerate(bots))
        newores = bfs(bp, newores, newbots, t+1)
        if maxores[-1] < newores[-1]:
            bestbots = newbots
            maxores = newores

    memores = mem[tuple([bestbots, t])]
    if all(memo < o for memo, o in zip(memores, maxores)):
        mem[tuple([bestbots, t])] = maxores
    return maxores


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
        for bt,o in mem.items():
            b, t = bt
            if t == 24 and b[0] == 1 and b[1] == 4:
                ic(b,t,o)
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
