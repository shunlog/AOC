#!/bin/env python3
from icecream import ic

# -1 if l1 < l2
# 0 if l1 = l2
# 1 if l1 > l2
# 3379 too low

def cmp_ints(i1, i2):
    if i1 < i2:
        return -1
    elif i1 == i2:
        return 0
    else:
        return 1

def cmp_lists(l1, l2):
    for e1, e2 in zip(l1, l2):
        r = cmp_expr(e1, e2)
        if r != 0:
            return r
    return cmp_ints(len(l1), len(l2))

def cmp_expr(e1, e2):
    if type(e1) == type(e2) == list:
        return cmp_lists(e1, e2)
    elif type(e1) == type(e2) == int:
        return cmp_ints(e1, e2)
    else:
        return cmp_lists([e1] if type(e1) == int else e1,
                         [e2] if type(e2) == int else e2)

def p1(inp):
    pairs = []
    for p in inp.split('\n\n'):
        pairs.append([eval(l) for l in p.splitlines()])
    s = 0
    for i, p in enumerate(pairs):
        ic(p[0], p[1])
        c = cmp_expr(p[0], p[1])
        if c == -1:
            s += i+1
    return s

def p2(inp):
    ic(inp.splitlines())
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
