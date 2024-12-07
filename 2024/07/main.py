#!/bin/env python3
import sys
from icecream import ic

from itertools import product


def solvable(expected: str, nums: str, part2=False):
    '''Given the list of nums and the expected result,
    return True if it can be solved with any combination of operators.'''

    def try_ops(ops):
        res = nums[0]
        for num, op in zip(nums[1:], ops):
            if op == '*':
                res = str(int(res) * int(num))
            elif op == '|':
                res += num
            else:
                res = str(int(res) + int(num))
            if int(res) > int(expected):
                return False

        if res == expected:
            return True

    operations = '+*' if not part2 else '+*|'
    ops_ls = list(product(*[operations] * (len(nums)-1)))
    for ops in ops_ls:
        if try_ops(ops):
            return True

    return False


def solve1(ls):
    return sum(int(l[0]) for l in ls if solvable(l[0], l[1:]))


def solve2(ls):
    return sum(int(ic(l[0])) for l in ls if solvable(l[0], l[1:], True))


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
