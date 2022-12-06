#!/bin/env python3
from icecream import ic
from collections import Counter

def solve(inp, n):
    c = Counter()
    for i, ch in enumerate(inp):
        c[ch] += 1
        if i < n:
            continue
        c[inp[i-n]] -= 1
        if c[inp[i-n]] == 0:
            del c[inp[i-n]]
        if len(c.keys()) == n:
            return i + 1
    return -1

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp, 4))
    if '1' not in sys.argv:
        print(solve(inp, 14))
