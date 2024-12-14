#!/bin/env python3
import sys
from icecream import ic

import re
from math import prod


def solve1(ls):
    t = 100

    # For examples:
    # w = 11
    # h = 7
    w = 101
    h = 103

    halfw = w // 2
    halfh = h // 2

    # key is composed of two booleans:
    # 1. whether the x is on the left of the halfway intersection
    # 2. whether the y is on the left of the halfway intersection
    quadr_cnt = {(True, True): 0,
                 (True, False): 0,
                 (False, True): 0,
                 (False, False): 0}

    for l in ls:
        x, y, vx, vy = l
        xf = (x + (vx * t)) % w
        yf = (y + (vy * t)) % h

        # skip values falling on the half-way intersections
        if xf == halfw or yf == halfh:
            continue
        quadr_cnt[(xf < halfw, yf < halfh)] += 1

    return prod(quadr_cnt.values())


def solve2(m):
    return


def solve(inp, part2=False, debug=False):
    if not debug:
        ic.disable()

    # pre-process for both parts
    inp = inp.strip()
    ls = []
    for l in inp.splitlines():
        nums = re.findall(r'-?\d+', l)
        assert len(nums) == 4
        nums_int = [int(n) for n in nums]
        ls.append(nums_int)

    if part2:
        return solve2(ls)

    return solve1(ls)


if __name__ == "__main__":
    # read the file from stdin and pass to solve()
    debug = '-d' in sys.argv
    inp = sys.stdin.read()
    if '2' not in sys.argv:
        print(solve(inp, False, debug))
    if '1' not in sys.argv:
        print(solve(inp, True, debug))
