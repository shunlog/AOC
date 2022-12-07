#!/bin/env python3
from icecream import ic
from itertools import *
from more_itertools import *
from collections import *

def get_sizes(inp):
    inp = inp.splitlines()
    sizes = defaultdict(int)
    dirs = ['/']
    for l in inp[1:]:
        t = l.split()
        if ['$', 'cd'] == t[:2] and t[2] == '..':
           dirs.pop()
        elif ['$', 'cd'] == t[:2] and t[2] != '..':
           dirs.append(dirs[-1]+t[2]+"/")
        elif '$' != t[0] and t[0] != 'dir':
           s = int(t[0])
           for d in dirs:
               sizes[d] += s
    return sizes

def p1(inp):
    MAX = 100000
    return sum([s for d,s in get_sizes(inp).items() if s <= MAX])

def p2(inp):
    TOTAL= 70000000
    NEED = 30000000
    sizes = get_sizes(inp)
    USED = sizes['/']
    UNUSED = TOTAL - USED
    DEL = NEED - UNUSED
    return min(filter(lambda s: s >= DEL, sizes.values()))

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
