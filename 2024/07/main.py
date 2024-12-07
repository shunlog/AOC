#!/bin/env python3
import sys
from icecream import ic

from itertools import product


def solvable(result, nums):
    '''Given the list of nums, return True if it can be solved.'''
    ops_ls = list(product(*['+*'] * (len(nums)-1)))

    for ops in ops_ls:
        expr = []
        for num, op in zip(nums[1:], ops):
            expr.extend([op, num, ')'])
        s = '(' * (len(nums)-1) + nums[0] + ' '.join(expr)
        r = eval(s)
        if r == result:
            return True

    return False


def solve1(ls):
    return sum(l[0] for l in ls if solvable(l[0], l[1:]))


def solve2(ls):
    return


def solve(inp, part2=False, debug=False):
    if not debug:
        ic.disable()

    # pre-process for both parts
    inp = inp.strip()
    ls = []
    for l in inp.splitlines():
        nums = [n for n in l.replace(':', '').split()]
        ls.append(nums)

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
