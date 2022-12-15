#!/bin/env python3
from icecream import ic
import re

# 1. check all the sensors whose scanning area intersects the line
# 1) 4991702 is too low

def ints(s):
    return [int(i) for i in re.findall(r'-?\d+', s)]

def p1(inp, Y):
    ly = dict()
    sl = []
    bl = []
    for l in inp.splitlines():
        sx, sy, bx, by = ints(l)
        sl.append((sx, sy))
        bl.append((bx, by))
        d = abs(sy - by) + abs(sx - bx)
        if sy - d <= Y <= sy + d:
            dy = abs(Y - sy)
            dx = d - dy
            r = (sx - dx, sx + dx)
            for i in range(r[0], r[1]+1):
                ly[i] = True

    minx, maxx = min(ly.keys()), max(ly.keys())
    ic(minx, maxx)
    c = 0
    for i in range(minx, maxx+1):
        if ly.get(i) and not (i, Y) in bl:
            c += 1

    return c

def p2(inp, lim):
    sl = []
    for l in inp.splitlines():
        sx, sy, bx, by = ints(l)
        d = abs(sy - by) + abs(sx - bx)
        sl.append((sx, sy, d))

    for i, s1 in enumerate(sl):
        ss = f"{i}/{len(sl)}"
        ic(ss)
        sx, sy, d = s1
        D = d + 1
        for dx in range(D+1):
            dy = D - dx
            for x,y in [(sx-dx,sy-dy),
                        (sx-dx,sy+dy),
                        (sx+dx,sy-dy),
                        (sx+dx,sy+dy)]:
                if x < 0 or x > lim or y < 0 or y > lim:
                    continue
                for s2 in sl:
                    if s1 == s2:
                        continue
                    sx2, sy2, d2 = s2
                    d21 = abs(sx2 - x) + abs(sy2 - y)
                    if d21 <= d2:
                        break
                else:
                    ic(x, y)
                    return 4000000 * x + y

    return 0

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        if len(inp) < 1000:
            print(p1(inp, 10))
        else:
            print(p1(inp, 2000000))
    if '1' not in sys.argv:
        if len(inp) < 1000:
            print(p2(inp, 20))
        else:
            print(p2(inp, 4000000))
