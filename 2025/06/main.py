#!/usr/bin/env python3
import sys
from icecream import ic
import math
import more_itertools

ic.disable()


def solve1(inp):
    lines = inp.strip().split('\n')
    * rows, opl = lines
    ops = opl.split()
    rownums = ((int(n) for n in r.split()) for r in rows)
    cols = list(zip(*rownums))

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
    lines = inp[:-1].split('\n')
    # transpose into list of column strings
    # e.g. ["1  +", "24  ", "356 "]
    cols = (''.join(col) for col in zip(*lines))
    # each group of columns is separated by empty column
    groups = list(more_itertools.split_at(
        cols, lambda x: x == ' '*len(lines)))

    def compute_group(g):
        # the operator is the last char in the first line
        op = g[0][-1]
        nums = (int(s[:-1]) for s in g)
        return sum(nums) if op == '+' else math.prod(nums)

    return sum(compute_group(g) for g in groups)


def solve(inp, part2=False):
    if part2:
        return solve2(inp)
    return solve1(inp)


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
