#!/bin/env python3
from icecream import ic
from itertools import cycle
import re
from math import lcm


def p1(steps, d, node='AAA', end=lambda n: n == 'ZZZ'):
    for i, s in enumerate(cycle(steps), start=1):
        node = d[node][0] if s == 'L' else d[node][1]
        if end(node):
            return i

    assert False


def p2(steps, d):
    # find all nodes that end in "A"
    nodes = [n for n in d.keys() if n[-1] == 'A']
    ic(nodes)

    periods = [p1(steps, d, n, lambda n: n[-1] == 'Z') for n in nodes]


    return lcm(*periods)


def solve(inp, part2=False):
    lines = inp.splitlines()
    steps = lines[0]
    ic(steps)

    r = re.compile(r'(\S+) = \((\S+), (\S+)\)')

    d = dict()
    for l in lines[2:]:
        k, vl, vr = r.match(l).groups()
        d[k] = (vl, vr)

    if not part2:
        return p1(steps, d)
    return p2(steps, d)


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
