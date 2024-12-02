#!/bin/env python3
import sys
from icecream import ic


def solve1(m):
    return


def solve2(m):
    return


def solve(inp, part2=False, debug=False):
    if not debug:
        ic.disable()

    # pre-process for both parts
    inp = inp.strip()

    if part2:
        return solve2(inp)

    return solve1(inp)


if __name__ == "__main__":
    # read the file from stdin and pass to solve()
    debug = '-d' in sys.argv
    inp = sys.stdin.read()
    if '2' not in sys.argv:
        print(solve(inp, False, debug))
    if '1' not in sys.argv:
        print(solve(inp, True, debug))
