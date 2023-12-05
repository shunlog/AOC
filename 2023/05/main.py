#!/bin/env python3
from icecream import ic
import more_itertools

def map_value(m, v):
    for l in m:
        if v in range(l[1], l[1] + l[2] + 1):
            return l[0] + (v - l[1])
    return v

def solve(inp, part2=False):
    pl = inp.split('\n\n')

    if not part2:
        seeds = [int(n) for n in pl[0].split()[1:]]
    else:
        nums = [int(n) for n in pl[0].split()[1:]]
        seeds = []
        for st, sz in more_itertools.chunked(nums, 2):
            ic(st, sz)
            seeds += range(st, st+sz+1)
    ic(seeds)

    maps = []
    for p in pl[1:]: # paragraphs
        m = [[int(n) for n in l.split()] for l in p.splitlines()[1:]]
        maps.append(m)
    ic(seeds)
    ic(maps)

    source = seeds.copy()
    dest = [0] * len(source)
    for m in maps:
        for i, s in enumerate(source):
            dest[i] = map_value(m, s)
        ic(dest)
        source = dest.copy()

    return min(dest)


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
