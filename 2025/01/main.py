#!/usr/bin/env python3
import sys
from icecream import ic

ic.disable()

def solve1(inp):
    dial = 50
    res = 0
    for ins in inp.strip().split():
        dirn, cnt = ins[:1], int(ins[1:])
        if dirn == 'L':
            dial = (dial - cnt) % 100
        else:
            dial = (dial + cnt) % 100
        if dial == 0:
            res += 1
    return res


def solve2(inp):
    dial = 50
    res = 0
    for ins in inp.strip().split():
        dirn, cnt = ins[:1], int(ins[1:])
        if dirn == 'L':
            res += abs((dial - cnt) // 100)
            dial = (dial - cnt) % 100

        else:
            res += (dial + cnt) // 100
            dial = (dial + cnt) % 100

        ic(ins, dial, res)
    return res


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
