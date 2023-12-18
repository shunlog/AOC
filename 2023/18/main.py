#!/bin/env python3
from icecream import ic
import queue
from collections import defaultdict

def flood_fill(m, pos, setf, inside):
    '''Floof fill the matrix in-place'''
    Q = queue.SimpleQueue()
    Q.put(pos)
    while not Q.empty():
        x, y = Q.get()
        if not inside(m, x, y):
            continue
        setf(m, x, y)
        Q.put((x+1, y))
        Q.put((x-1, y))
        Q.put((x, y+1))
        Q.put((x, y-1))


def parse_input(inp):
    d = defaultdict(lambda: '.')
    pos = (0, 0)
    d[pos] = '#'
    trans = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}

    for ins in inp.splitlines():
        s1, s2, s3 = ins.split()
        dirn, n, col = s1, int(s2), s3[2:-1]
        dx, dy = trans[dirn]
        for _ in range(n):
            pos = pos[0] + dx, pos[1] + dy
            d[pos] = '#'

    return d


# Using a dictionary for main
def inside(d, x, y):
    return d[(x, y)] == '.'

def setf(d, x, y):
    d[(x, y)] = '#'


def solve(inp, part2=False):
    d = parse_input(inp)

    flood_fill(d, (1, 1), setf, inside)  # modify in-place

    return len(d)


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not ('--debug' in sys.argv or '-d' in sys.argv):
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
