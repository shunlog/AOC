#!/usr/bin/env python3
import sys
from icecream import ic

ic.disable()


def max_jolt_n(line: str, n: int) -> str:
    '''Picks n digits from the line, keeping order,
    such that they form the largest possible number
    E.g. max_jolt_n("3132111", 3) == "332"
    '''
    assert n <= len(line)
    
    def iter(start, end, remaining) -> str:
        if remaining == 0:
            return ""
        maxn = max(*line[start:end])
        idx = line.index(maxn, start, end)
        return maxn + iter(idx+1, end+1, remaining-1)
        
    return iter(0, len(line) - n + 1, n)


def test_max_jolt_n():
    ic.enable()
    assert max_jolt_n("3", 1) == "3"
    assert max_jolt_n("123", 1) == "3"
    assert max_jolt_n("23", 2) == "23"
    assert max_jolt_n("3132111", 3) == "332"
    assert max_jolt_n("987654321111111", 12) == "987654321111"
    assert max_jolt_n("811111111111119", 12) == "811111111119"
    assert max_jolt_n("234234234234278", 12) == "434234234278"
    assert max_jolt_n("818181911112111", 12) == "888911112111"

    
def solve(inp, part2=False):
    length = 12 if part2 else 2
    return sum(int(max_jolt_n(l, length)) for l in inp.split())


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
