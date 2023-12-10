#!/bin/env python3
from icecream import ic


def find_path(m):
    '''Given the matrix, return a list of coordinates are stored as tuples (x, y)
    which represents the closed cycle starting from S.'''
    def find_S(m):
        for y, row in enumerate(m):
            for x, ch in enumerate(row):
                if ch == 'S':
                    return (x, y)

    def find_next_pipe(m, pos, prev=None):
        exits = { # the directions in which you can exit the pipe
            '-': ((1, 0), (-1, 0)),
            '|': ((0, 1), (0, -1)),
            'F': ((1, 0), (0, 1)),
            'L': ((1, 0), (0, -1)),
            'J': ((0, -1), (-1, 0)),
            '7': ((0, 1), (-1, 0)),
        }
        x, y = pos
        ch = m[y][x]

        def can_enter(dx, dy):
            '''Return True if you can go in the given direction from current pos'''
            nch = m[y+dy][x+dx]
            if nch == '.':
                return False
            return (-dx, -dy) in exits[nch]

        # if on 'S', go wherever you can enter the pipe
        if ch == 'S':
            for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                if can_enter(dx, dy):
                    return (x+dx, y+dy)

         # else, just go in the direction that doesn't lead to `prev`
        for dx, dy in exits[ch]:
            nx, ny = x+dx, y+dy
            if (nx, ny) == prev:
                continue
            return nx, ny

    S = find_S(m)
    path = [S, find_next_pipe(m, S)]
    while path[-1] != S:
        npos = find_next_pipe(m, path[-1], path[-2])
        path.append(npos)

    return path


def solve(inp, part2=False):
    m = inp.splitlines()
    path = find_path(m)

    if not part2:
        return len(path) // 2


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
