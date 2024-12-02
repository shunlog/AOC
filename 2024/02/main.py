#!/bin/env python3
import sys
from icecream import ic

from itertools import pairwise


def safe(rep):
    l = list(pairwise(rep))
    diff = [b-a for (a, b) in l]
    if not (all(n < 0 for n in diff)
            or all(n > 0 for n in diff)):
        return False
    if any(abs(n) > 3 for n in diff):
        return False
    return True


def solve1(m):
    return sum(int(safe(r)) for r in m)


def safe_dampened(r):
    if safe(r):
        return True

    miss = [r[:i] + r[i+1:] for i in range(len(r))]
    ic(miss)
    for l in miss:
        if safe(l):
            return True

    return False


def solve2(m):
    return sum(int(safe_dampened(r)) for r in m)


def solve(inp, part2=False, debug=False):
    if not debug:
        ic.disable()

    # pre-process for both parts
    inp = inp.strip()
    m = [[int(n) for n in l.split()] for l in inp.splitlines()]

    ic(m)

    if part2:
        return solve2(m)

    return solve1(m)


if __name__ == "__main__":
    # read the file from stdin and pass to solve()
    debug = '-d' in sys.argv
    inp = sys.stdin.read()
    if '2' not in sys.argv:
        print(solve(inp, False, debug))
    if '1' not in sys.argv:
        print(solve(inp, True, debug))
