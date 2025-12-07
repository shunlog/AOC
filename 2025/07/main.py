#!/usr/bin/env python3
import sys
from icecream import ic
import functools
ic.disable()


def solve1(m):
    splitters = set()

    @functools.lru_cache
    def beam_splits(row, col):
        if row >= len(m):
            return 0
        if m[row][col] == '^':
            splitters.add((row, col))
            return 1 + beam_splits(row, col-1) + beam_splits(row, col+1)
        else:
            return beam_splits(row+1, col)
    beam_splits(0, m[0].index('S'))
    return len(splitters)


def solve2(m):

    @functools.lru_cache
    def beams_count(row, col):
        if row >= len(m):
            return 1
        if m[row][col] == '^':
            return beams_count(row, col-1) + beams_count(row, col+1)
        else:
            return beams_count(row+1, col)
    return beams_count(0, m[0].index('S'))


def solve(inp, part2=False):
    m = inp.strip().split()
    if part2:
        return solve2(m)
    return solve1(m)


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
