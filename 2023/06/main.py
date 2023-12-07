#!/bin/env python3
from icecream import ic
from math import sqrt, ceil, floor


def solve(inp, part2=False):
    # dist(x) = (t - x) * x
    # dist(x) = record to find x1 and x2
    # rec = (t - x) * x
    # x**2 - t*x + rec = 0

    tl, recl = ([int(n) for n in l.split()[1:]] for l in inp.splitlines())

    prod = 1
    for t, rec in zip(tl, recl):
        delta = t**2 - 4*rec
        x1 = -(t - sqrt(delta)) / 2
        x1 = ceil(x1)
        x2 = -(t + sqrt(delta)) / 2
        x2 = floor(x2)
        n = abs(x2 - x1 + 1)

        ic(n)
        prod *= n

    return prod


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
