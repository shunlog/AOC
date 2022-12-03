#!/bin/env python3
from itertools import zip_longest
from icecream import ic

def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks.

    >>> grouper('ABCDEFG', 3, 'x')
    ['ABC', 'DEF', 'Gxx']
    """
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def pr(i):
    if ord('a') <= ord(i) <= ord('z'):
        return ord(i) - ord('a') + 1
    elif ord('A') <= ord(i) <= ord('Z'):
        return ord(i) - ord('A') + 27
    raise

def halve(l):
    return l[:len(l)//2], l[len(l)//2:]

def p1(inp):
    inp = inp.splitlines()
    repeated = [set.intersection(*map(set, halve(l))) for l in inp]
    s = sum((sum((pr(i) for i in l)) for l in repeated))
    return s

def p2(inp):
    inp = inp.splitlines()
    sets = [map(set, l) for l in grouper(inp, 3)]
    b = [list(set.intersection(*s))[0] for s in sets]
    return sum(map(pr, b))

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not 'test' in sys.argv:
        pass
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
