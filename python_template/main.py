#!/usr/bin/env python3
import sys
from icecream import ic


def solve1(inp):
    return 0


def solve2(inp):
    return 0


def solve(inp, part2=False, debug=False):
    if debug:
        ic.enable()
    else:
        ic.disable()

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
