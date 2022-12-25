#!/bin/env python3
import math
from icecream import ic

digits = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

sdigits = {value: key for key, value in digits.items()}

def tosnafu(n):
    digc = math.floor(math.log(n, 5)) + 1
    sn = ""
    pn = n
    for i in range(digc, -1, -1):
        rest = sum(2 * (5**j) for j in range(i-1, -1, -1))
        cur =  (n+rest) // (5**i)
        sn += sdigits[cur]
        n -= cur * (5**i)
    while sn[0] == '0':
        sn = sn[1:]
    assert todec(sn) == pn
    return sn

def todec(sn):
    return sum(5**i * digits[d] for i,d in enumerate(sn[::-1]))

def p1(inp):
    nl = []
    for sn in inp.splitlines():
        n = todec(sn)
        nl.append(n)

    # for i in range(1, 100):
    #     ic(i, tosnafu(i))

    return tosnafu(sum(nl))

def p2(inp):
    return 0

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
