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

def transpose(l):
    return list(zip(*l))

def most_common(l):
    return int(sum(l) >= len(l)/2)

def least_common(l):
    return int(not most_common(l))

def p2(inp):
    inp = [[int(i) for i in l] for l in inp.splitlines()]
    ogr = inp.copy()
    csr = inp.copy()
    for i in range(len(ogr[0])):
        mc = most_common(transpose(ogr)[i])
        ogr = list(filter(lambda l: l[i] == mc, ogr))
        if len(ogr) == 1:
            break
    for i in range(len(csr[0])):
        lc = least_common(transpose(csr)[i])
        csr = list(filter(lambda l: l[i] == lc, csr))
        if len(csr) == 1:
            break
    to_int = lambda l: int(''.join(map(str,l)), 2)
    return to_int(ogr[0]) * to_int(csr[0])

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
