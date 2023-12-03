#!/bin/env python3
from icecream import ic
import re
from collections import defaultdict
import math
from collections import namedtuple

def neighbors(m, x, y):
    # Input: matrix and a pair of coordinates
    # Output: list of all neighboring cells: Cell(val, x, y)
    Cell = namedtuple('Cell', ['val', 'x', 'y'])
    l = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue # same cell
            try:
                m[y+dy][x+dx]
            except:
                continue # out of bounds
            nx, ny = x+dx, y+dy
            v = m[ny][nx]
            l.append(Cell(v, nx, ny))
    return l



def p1(inp):
    # 1. Go through each digit of each number,
    # 2. Check all neighboring sympols
    # 3. If found, add number to sum
    def adjacent_to_symbol(x, y, m):
        for cell in neighbors(m, x, y):
            if not cell.val.isnumeric() and cell.val != '.': # char is a symbol
                return True
        return False

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


def p2(inp):
    # 1. Go through each digit of each number, find all adj. gears to that number
    # 2. for each gear, add the number to the dict
    # 3. Go through each gear, check neighb.=2, add to sum
    m = inp.splitlines() # matrix
    gears = defaultdict(set)  # (x, y) --> set(numbers)

    def neighb_gears(x, y):
        # return set of neighb. gears
        g = set()
        for cell in neighbors(m, x, y):
            if cell.val != '*':
                continue # not a gear
            g.add((cell.x, cell.y))
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

    return p1(inp)


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
