#!/bin/env python3
from icecream import ic
from itertools import *
from more_itertools import *
from collections import *

def p1(inp):
    MAX = 100000
    inp = inp.splitlines()
    dirs = []
    size = defaultdict(int)
    for l in inp:
        t = l.split()
        if t[0] == '$':
           if t[1] == 'cd':
               if t[2] == '..':
                   dirs.pop()
               else:
                   dirs.append("/".join(dirs)+t[2])
        elif t[0] == 'dir':
           pass
        else:
           s = int(t[0])
           assert(len(dirs) > 0)
           for d in dirs:
               size[d] += s
    ic(size)

    return sum([s for d,s in size.items() if s <= MAX])

def p2(inp):
    TOTAL= 70000000
    NEED = 30000000

    inp = inp.splitlines()
    dirs = []
    size = defaultdict(int)
    for l in inp:
        t = l.split()
        if t[0] == '$':
           if t[1] == 'cd':
               if t[2] == '..':
                   dirs.pop()
               else:
                   dirs.append("/".join(dirs)+t[2])
        elif t[0] == 'dir':
           pass
        else:
           s = int(t[0])
           assert(len(dirs) > 0)
           for d in dirs:
               size[d] += s
    USED = size['/']
    ic(USED)
    UNUSED = TOTAL - USED
    DEL = NEED - UNUSED

    return min(filter(lambda s: s >= DEL, size.values()))

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
