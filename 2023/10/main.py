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
    while (npos := find_next_pipe(m, path[-1], path[-2])) != S:
        path.append(npos)

    return path


def enclosed_area(m, loop):
    '''Return the number of tiles enclosed by the loop.
    - `m` is the matrix
    - `loop` is a set of coordinates'''

    h, w = len(m), len(m[0])

    def inside_loop(x, y):
        '''Use ray casting to determine if point (x, y) is inside loop.'''
        ic(x, y)

        if (x, y) in loop:
            return False

        # count hits
        cnt = 0
        # pick shortest ray
        r = range(x+1, w) if x > w//2 else range(x-1, -1, -1)
        for nx in r:
            if (nx, y) in loop and (m[y][nx] not in ('-', '7', 'F', 'S')):
                cnt += 1

        if cnt % 2 == 0:
            return False

        ic(x, y, m[y][x], cnt)
        return True

    return sum(int(inside_loop(x, y)) for y in range(h) for x in range(w))


def loop_to_str(m, loop):
    s = ''
    for y, row in enumerate(m):
        for x, ch in enumerate(row):
            if (x, y) not in loop:
                s += ' '
                continue
            s += ch
        s += '\n'
    return s


def solve(inp, part2=False):
    m = inp.splitlines()
    path = find_path(m)

    if not part2:
        return len(path) // 2

    return enclosed_area(m, set(path))


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
