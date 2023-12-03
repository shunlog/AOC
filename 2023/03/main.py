#!/bin/env python3
from icecream import ic
import re
from collections import defaultdict
import math


def adjacent_to_symbol(x, y, m):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:  # the digit itself
                continue
            try: # check if out of bounds
                m[y+dy][x+dx]
            except:
                continue
            ch = m[y+dy][x+dx]
            if not ch.isnumeric() and ch != '.': # char is a symbol
                return True
    return False


def p2(inp):
    # 1. Go through each digit of each number, find all adj. gears to that number
    # 2. for each gear, add the number to the dict
    # 3. Go through each gear, check neighb.=2, add to sum
    m = inp.splitlines() # matrix
    gears = defaultdict(set)  # (x, y) --> set(numbers)

    def neighb_gears(x, y):
        # return set of neighb. gears
        g = set()
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue # the digit itself
                try:
                    m[y+dy][x+dx]
                except:
                    continue # out of bounds
                ch = m[y+dy][x+dx]
                if ch != '*':
                    continue # not a gear
                g.add((x+dx, y+dy))
        return g


    p = re.compile(r'\d+')
    s = 0
    for y, l in enumerate(m):
        for match in p.finditer(l): # check each number
            ng = set() # neighbor gears of number
            for x in range(*match.span()): # check each digit
                ng |= neighb_gears(x, y)  # find all neighb. gears
            for g in ng:
                gears[g].add(match[0])

    ic(gears)

    return sum(math.prod(int(n) for n in v) for v in gears.values() if len(v) == 2)


def solve(inp, part2=False):
    if part2:
        return p2(inp)
    m = inp.splitlines() # matrix
    p = re.compile(r'\d+')

    s = 0
    for y, l in enumerate(m):
        for match in p.finditer(l): # check each number
            ic(match)
            for x in range(*match.span()): # check each digit
                ic(m[y][x])
                if adjacent_to_symbol(x, y, m): # is engine part
                    s += int(match[0])
                    break

    return s


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
