#!/bin/env python3
from icecream import ic

def p1(inp):
    from collections import Counter
    c = Counter()

    for i, ch in enumerate(inp):
        c[ch] += 1
        if i > 3:
            c[inp[i-4]] -= 1
            if c[inp[i-4]] == 0:
                del c[inp[i-4]]
        ic(c)
        if len(c.keys()) == 4:
            return i + 1

    return -1

def p2(inp):
    from collections import Counter
    c = Counter()

    for i, ch in enumerate(inp):
        c[ch] += 1
        if i > 13:
            c[inp[i-14]] -= 1
            if c[inp[i-14]] == 0:
                del c[inp[i-14]]
        ic(c)
        if len(c.keys()) == 14:
            return i + 1

    return -1

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
