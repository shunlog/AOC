#!/bin/env python3
from icecream import ic
from itertools import *
from more_itertools import *
from collections import *

def p1(inp):
    MAX = 100000
    inp = inp.splitlines()
    dirs = []
    lvl = 0
    size = defaultdict(int)
    for l in inp:
        plvl = lvl

        t = l.split()
        if t[0] == '$':
           if t[1] == 'cd':
               if t[2] == '..':
                   lvl -= 1
               else:
                   dirs.append(t[2])
                   lvl += 1
        elif t[0] == 'dir':
           pass
        else:
           s = int(t[0])
           for d in dirs:
               size[d] += s

        if lvl < plvl:
            dirs.pop()

    return sum([s for d,s in size.items() if s < MAX])

def p2(inp):
    MAX = 100000
    inp = inp.splitlines()
    dirs = []
    lvl = 0
    size = defaultdict(int)
    for l in inp:
        plvl = lvl

        t = l.split()
        if t[0] == '$':
           if t[1] == 'cd':
               if t[2] == '..':
                   lvl -= 1
               else:
                   dirs.append(t[2])
                   lvl += 1
        elif t[0] == 'dir':
           pass
        else:
           s = int(t[0])
           for d in dirs:
               size[d] += s

        if lvl < plvl:
            dirs.pop()

    return sum([s for d,s in size.items() if s < MAX])

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
