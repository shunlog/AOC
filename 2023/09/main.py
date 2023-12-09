#!/bin/env python3
from icecream import ic


def extrapolate(a, backwards=False):
    if all(i == 0 for i in a):
        return 0

    subl = [n2 - n1 for n2, n1 in zip(a[1:], a[:-1])]

    if backwards:
        return a[0] - extrapolate(subl, backwards)
    else:
        return a[-1] + extrapolate(subl, backwards)


def solve(inp, part2=False):
    lists_gen = ([int(n) for n in l.split()] for l in inp.splitlines())
    return sum(extrapolate(l, part2) for l in lists_gen)


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
