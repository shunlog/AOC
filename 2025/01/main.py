#!/usr/bin/env python3
import sys
from icecream import ic
from math import floor

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


def shift_left(dial: int, shift: int) -> tuple[int, int]:
    '''Returns count of 0's ticked, and resulting dial
    e.g. shift_left(1, 2) -> (1, 99)
    '''
    dial2 = (dial - shift) % 100
    zeros = abs(floor((dial - shift) / 100))
    if dial2 == 0:
        zeros += 1
    if dial == 0:
        zeros -= 1
    return zeros, dial2


def test_shift_left():
    ic.enable()
    assert shift_left(50, 1) == (0, 49)
    assert shift_left(1, 1) == (1, 0)
    assert shift_left(0, 1) == (0, 99)
    assert shift_left(50, 100) == (1, 50)
    assert shift_left(50, 200) == (2, 50)
    assert shift_left(50, 50) == (1, 0)
    assert shift_left(0, 200) == (2, 0)

    
def solve2(inp):
    dial = 50
    res = 0
    for ins in inp.strip().split():
        dirn, cnt = ins[:1], int(ins[1:])
        if dirn == 'L':
            zeros, dial = shift_left(dial, cnt)
            res += zeros
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
