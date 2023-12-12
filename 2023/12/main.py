#!/bin/env python3
from icecream import ic
from functools import cache

@cache
def possib(s, nums):
    ic(s, nums)

    if (sum(nums) > len(s)):
        return 0
    if len(nums) == 0 and not any(ch == '#' for ch in s):
        return 1
    elif len(nums) == 0:
        return 0
    elif len(s) == 0:
        return 0

    N = nums[0]

    if s[0] == '.':
        return possib(s[1:], nums)

    if s[0] == '#': # we gotta place N #'s
        possible = (len(s) >= N and all(ch in ('#', '?') for ch in s[:N])) \
            and ((len(s) == N) \
                 or (len(s) > N and s[N] in ('.', '?')))
        if not possible:
            return 0
        else:
            return possib(s[N+1:], nums[1:])

    # 1. Skip
    p1 = possib(s[1:], nums)

    # 2. Place
    # check if can place
    can_place = len(s) >= N \
        and all(ch in ('?', '#') for ch in s[:N]) \
        and ((len(s) == N) or (s[N] in ('?', '.')))
    if can_place:
        p2 = possib(s[N+1:], nums[1:])
    else:
        p2 = 0

    # ic(s, nums, p1, p2, p1+p2)
    return p1 + p2

def solve(inp, part2=False):
    sm = 0
    for i, l in enumerate(inp.splitlines()):
        ic(i)
        s, nl = l.split()
        nums = [int(n) for n in nl.split(',')]

        if part2:
            s += "?"
            s = s*5
            s = s[:-1]
            nums = nums*5

        sm += possib(s, tuple(nums))
    return sm

    # s = (("???.#??#.???" + '?') * 5)[:-1]
    # nums = (1,1,2,1) * 5
    # possib(s, nums)
    return 0


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
