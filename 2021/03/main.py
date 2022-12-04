#!/bin/env python3
from icecream import ic

def p1(inp):
    inp = inp.splitlines()
    trans = list(zip(*inp))
    mc = ['1' if n >= len(inp)//2 else '0' for n in [sum(map(int,l)) for l in trans]]
    gamma_bs = ic(''.join(mc))
    gamma = int(gamma_bs, 2)
    eps = 2**len(trans) - gamma - 1
    return gamma * eps

def p2(inp):
    inp = inp.splitlines()
    trans = list(zip(*inp))
    ic(trans)
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
