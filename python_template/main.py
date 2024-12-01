#!/bin/env python3
from icecream import ic


def solve1(l):
    return


def solve2(l):
    return


def solve(inp, part2=False):
    # pre-process for both parts
    inp = inp.strip()

    if part2:
        return solve2(l1, l2)

    return solve1(l1, l2)


if __name__ == "__main__":
    # read the file from stdin and pass to solve()
    import sys
    inp = sys.stdin.read()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
