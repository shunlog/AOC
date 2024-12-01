#!/bin/env python3
from icecream import ic
from collections import Counter


def solve1(l1, l2):
    ls1 = sorted(l1)
    ls2 = sorted(l2)

    return sum(abs(x - y) for x, y in zip(ls1, ls2))


def solve2(l1, l2):
    c = Counter(l2)
    return sum(x * c[x] for x in l1)


def solve(inp, part2=False):
    inp = inp.strip()

    l1 = []
    l2 = []
    for l in inp.split('\n'):
        a, b = [int(i) for i in l.split()]
        l1.append(a)
        l2.append(b)

    if part2:
        return solve2(l1, l2)

    return solve1(l1, l2)


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
