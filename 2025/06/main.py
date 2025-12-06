#!/usr/bin/env python3
import sys
from icecream import ic
import math

ic.disable()


def solve1(cols, ops):
    res = 0
    for col, op in zip(cols, ops):
        if op == '+':
            col_res = sum(col)
        elif op == '*':
            col_res = math.prod(col)
        res += col_res
    return res


def solve2(inp):
    # assuming \n at the end of file
    m = list(reversed(list(zip(*inp[:-1].split('\n')))))
    ic(m)

    res = 0
    nums = []
    for l in m:
        if l[-1] in ('+', '*'):
            nums.append(int(''.join(l[:-1])))
            ic(nums)
            res += sum(nums) if l[-1] == '+' else math.prod(nums)
            nums = []
        elif all(ch == ' ' for ch in l):
            continue
        else:
            nums.append(int(''.join(l)))

    return res


def solve(inp, part2=False):
    lines = inp.strip().split('\n')
    * rows, opl = lines
    ops = opl.split()
    rownums = ((int(n) for n in r.split()) for r in rows)
    cols = list(zip(*rownums))

    if part2:
        return solve2(inp)
    return solve1(cols, ops)


if __name__ == "__main__":
    '''
    $ ./main.py                    # reads input.txt
    $ ./main.py -v -1 example.txt   # turns on logging, run only part 1
    '''

    last_arg = sys.argv[-1]
    if '.txt' in last_arg:
        fn = last_arg
    else:
        fn = "input.txt"
    with open(fn) as f:
        inp = f.read()

    if '-v' in sys.argv:
        ic.enable()

    if '-2' not in sys.argv:
        print(solve(inp, False))
    if '-1' not in sys.argv:
        print(solve(inp, True))
