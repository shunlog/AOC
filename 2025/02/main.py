#!/usr/bin/env python3
import sys
from icecream import ic
import itertools

ic.disable()

def is_invalid(s: str):
    if len(s) <= 1:
        return False
    if len(s) % 2 != 0:
        return False
    hl = len(s) // 2
    return s[:hl] == s[hl:]


def is_invalid2(s: str):
    if len(s) <= 1:
        return False
    def check_times(t: int):
        if len(s) % t != 0:
            return False
        batches = list(itertools.batched(s, len(s) // t))
        ic(batches)
        return all(b == batches[0] for b in batches[1:])
    return any(check_times(times) for times in range(2, len(s)+1))
        

def test_invalid2():
    ic.enable()
    assert is_invalid2('12341234')
    assert is_invalid2('123123123')
    assert is_invalid2('12121212')
    assert is_invalid2('11')
    assert not is_invalid2('121232')
        

def solve1(inp, is_invalid):
    res = 0
    for rang in inp.split(','):
        start, end = rang.split('-')
        for num in range(int(start), int(end)+1):
            if is_invalid(str(num)):
                ic(num)
                res += num
    return res



def solve(inp, part2=False, verbose=False):
    if part2:
        return solve1(inp, is_invalid2)
    return solve1(inp, is_invalid)


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
