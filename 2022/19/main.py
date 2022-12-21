#!/bin/env python3
import re
from icecream import ic
import math

def ints(s):
    return [int(i) for i in re.findall(r'-?\d+', s)]

cnt = 0

from collections import defaultdict
mem = None

def dfs(bpl, ores, bots, t):
    '''Return the maximum number of geodes produced from current time till end'''
    global cnt
    cnt += 1
    if t > 24:
        return ores

    # memoize
    for memores in mem[tuple([tuple(bots), t])]:
        if all(a >= b for a,b in zip(memores, ores)):
            return (-1, -1, -1, -1)
    else:
        mem[tuple([tuple(bots), t])].append(tuple(ores))

    bestores = ores
    buybotsl = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]
    for buybots in buybotsl:
        # check if robot is not required
        try:
            bi = buybots.index(1)
            notreq = False
            if all(bpl[bi][o] <= bots[o] for o in range(3)):
                ic(bots, bp, buybots)
                notreq = True
            if notreq:
                continue
        except:
            pass
        # buy bot
        cost = [0, 0, 0, 0]
        for bi,buybot in enumerate(buybots):
            if buybot == 0:
                continue
            cost = [a + b for a,b in zip(cost, [pr * buybot for pr in bpl[bi]])]
        if any(ores[i] < cost[i] for i in range(4)):
            continue
        # collect res
        newores = [a + b - c for a,b,c in zip(ores, bots, cost)]
        # get bot
        newbots = [a + b for a,b in zip(bots, buybots)]
        # dfs
        nextores = dfs(bpl, newores, newbots, t+1)
        if nextores[-1] > bestores[-1]:
            bestores = nextores

    return bestores


def p1(inp):
    bpl = []
    for l in inp.splitlines():
        il = ints(l)
        assert(len(il) == 7)
        o1, c1, ob1, ob2, g1, g3 = il[1:]
        bpl.append(((o1, 0, 0, 0), (c1, 0, 0, 0),
                    (ob1, ob2, 0, 0), (g1, 0, g3, 0)))

    q = 0
    for i, bp in enumerate(bpl):
        global mem, cnt
        mem = defaultdict(list)
        cnt = 0
        v = dfs(bp, (0, 0, 0, 0), (1, 0, 0, 0), 1)
        q += v[-1] * (i+1)
        # ic(mem)
        ic(bp, v)
        ic(cnt)

    return q

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
