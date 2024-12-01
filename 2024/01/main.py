#!/bin/env python3
import sys
from collections import Counter
from icecream import ic


def solve1(l1, l2):
    ls1 = sorted(l1)
    ls2 = sorted(l2)
    return sum(abs(x - y) for x, y in zip(ls1, ls2))


def solve2(l1, l2):
    c = Counter(l2)
    return sum(x * c[x] for x in l1)


def solve(inp, part2=False, debug=False):
    if not debug:
        ic.disable()

    inp = inp.strip()
    m = [[int(i) for i in l.split()] for l in inp.splitlines()]
    l1, l2 = list(zip(*m))  # transpose

    if part2:
        return solve2(l1, l2)

    return solve1(l1, l2)


if __name__ == "__main__":
    debug = '-d' in sys.argv
    inp = sys.stdin.read()
    if '2' not in sys.argv:
        print(solve(inp, False, debug))
    if '1' not in sys.argv:
        print(solve(inp, True, debug))
