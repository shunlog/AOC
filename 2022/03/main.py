#!/bin/env python3
from icecream import ic
from itertools import zip_longest

def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks.

    >>> grouper('ABCDEFG', 3, 'x')
    ['ABC', 'DEF', 'Gxx']
    """
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def format_input(inp):
    inp = inp.splitlines()
    ic(inp)
    return inp

def pr(i):
    if ord('a') <= ord(i) <= ord('z'):
        return ord(i) - ord('a') + 1
    elif ord('A') <= ord(i) <= ord('Z'):
        return ord(i) - ord('A') + 27
    raise

def p1(inp):
    inp = format_input(inp)
    inp = [(set(l[:len(l)//2]), set(l[len(l)//2:])) for l in inp]
    ic(inp)
    cmn = [p[0].intersection(p[1]) for p in inp]
    ic(cmn)
    v = [[pr(i) for i in s] for s in cmn]
    ic(v)
    unp = []
    for i in v:
        unp += i
    ic(unp)
    return sum(unp)

def p2(inp):
    inp = format_input(inp)
    g = list(grouper(inp, 3))
    ic(g)
    b = [list(set(gr[0]).intersection(set(gr[1]), set(gr[2])))[0] for gr in g]
    ic(b)
    return sum(map(pr, b))

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not 'test' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
