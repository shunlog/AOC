#!/bin/env python3
from icecream import ic

# True if l1 < l2
# False otherwise

def cmp_lists(l1, l2):
    return True

def cmp_expr(e1, e2):
    if type(e1) == type(e2) == list:
        return cmp_lists(e1, e2)
    elif type(e1) == type(e2) == int:
        return e1 < e2
    else:
        if type(e1) == int:
            e1 = [e1]
        else:
            e2 = [e2]
        return cmp_lists(e1, e2)

def parse(inp):
    pairs = []
    for p in inp.split('\n\n'):
        pairs.append([eval(l) for l in p.splitlines()])
    return pairs

def p1(inp):
    inp = parse(inp)
    s = 0
    for i, p in enumerate(inp):
        ic(p[0], p[1])
        if cmp_expr(p[0], p[1]):
            s += i+1
    return s

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
