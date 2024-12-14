#!/bin/env python3
import sys
from icecream import ic

import re


def solve_system(a, b, c, d, e, f) -> tuple[int, int]:
    rem = (c * e - b * f) % (a * e - b * d)
    if rem != 0:
        return None
    x = (c * e - b * f) // (a * e - b * d)

    rem2 = (f - d * x) % e
    if rem2 != 0:
        return None
    y = (f - d * x) // e

    return x, y


def solve1(ls, part2):
    # ax+by=c
    # dx+ey=f
    # x, y - number of presses on A and B respectively
    # Button A: X+a, Y+d
    # Button B: X+b, Y+e
    # Prize: X=c, Y=f

    tok = 0

    for l in ls:
        a, d, b, e, c, f = l

        if part2:
            c += 10000000000000
            f += 10000000000000

        s = solve_system(a, b, c, d, e, f)
        ic(s)
        if not s:
            continue

        x, y = s
        assert x > 0 and y > 0
        if not part2 and (x > 100 or y > 100):
            continue
        tok += 3 * x + y

    return tok


def solve(inp, part2=False, debug=False):
    if not debug:
        ic.disable()

    # pre-process for both parts
    inp = inp.strip()

    ls = []
    for par in inp.split('\n\n'):
        nums = re.findall(r'\d+', par)
        assert len(nums) == 6
        nums_int = [int(n) for n in nums]
        ls.append(nums_int)

    return solve1(ls, part2)


if __name__ == "__main__":
    # read the file from stdin and pass to solve()
    debug = '-d' in sys.argv
    inp = sys.stdin.read()
    if '2' not in sys.argv:
        print(solve(inp, False, debug))
    if '1' not in sys.argv:
        print(solve(inp, True, debug))
