#!/bin/env python3
from icecream import ic
import regex as re

def num(s):
    '''Return the number: first dig + last dig'''
    nums = list(filter(lambda ch: ch.isnumeric(), s))
    return int(nums[0] + nums[-1])


def num2(s):
    '''Return the number: first dig + last dig'''
    def tonum(s):
        if s.isnumeric():
            return s
        return str({'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}[s])

    p = re.compile(r'\d|one|two|three|four|five|six|seven|eight|nine')
    nums = p.findall(s, overlapped=True)
    ic(nums)
    num1 = tonum(nums[0])
    num2 = tonum(nums[-1])
    return int(num1 + num2)


def solve(inp, part2=False):
    num_fun = num if not part2 else num2
    return sum(num_fun(l) for l in inp.splitlines())


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().rstrip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
