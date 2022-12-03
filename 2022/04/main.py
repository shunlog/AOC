#!/bin/env python3
from icecream import ic

def p1(inp):
    return 0

def p2(inp):
    return 0

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not 'test' in sys.argv:
        pass
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
