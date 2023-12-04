#!/bin/env python3
from icecream import ic

def p2(points_ls):
    c = [1] * len(points_ls)
    for cid, p in enumerate(points_ls):
        for i in range(1, p+1):
            c[cid + i] += c[cid]  # create copies of the following p cards
    return sum(c)


def p1(points_ls):
    return sum(2**(p - 1) for p in points_ls if p != 0)


def solve(inp, part2=False):
    points_ls = []
    for line in inp.splitlines():
        l, r = line.split(':')[1].split('|')
        win_ls = [int(n) for n in l.split()]
        have_ls = [int(n) for n in r.split()]
        p = sum(n in have_ls for n in win_ls)
        points_ls.append(p)

    if part2:
        return p2(points_ls)
    return p1(points_ls)


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
