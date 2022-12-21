#!/bin/env python3
from icecream import ic

def p1(inp):
    d = {}

    for l in inp.splitlines():
        t = l.split()
        if len(t) == 2:
            e = f"{int(t[1])}"
            ic(e)
            d[t[0][:-1]] = lambda d, e=e: eval(e)
        else:
            e = f"d['{t[1]}'](d) " + t[2] + f" d['{t[3]}'](d)"
            ic(e)
            d[t[0][:-1]] = lambda d, e=e: eval(e)

    ic(d)

    return int(d['root'](d))

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
