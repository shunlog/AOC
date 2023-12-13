#!/bin/env python3
from icecream import ic


def transpose(m):
    return [*map(list, zip(*m))]


def find_mirror(m):
    ''' Finds the mirror position in the pattern matrix m.
    Returns tuple:
    - [0]: col/row after which is the split (0-indexed)
    - [1]: True if horizontal mirror, False if vertical.'''

    def test_column(m, i):
        '''Returns True if the mirror is after column i'''
        for r in m:
            left = r[:i+1]
            right = r[i+1:]
            if not all(p[0] == p[1] for p in zip(left[::-1], right)):
                return False
        return True

    def find_vertical(m):
        '''Returns column after which is the mirror, or False'''
        for i in range(len(m[0])-1):
            if test_column(m, i):
                return i
        return False


    if type(i := find_vertical(m)) != bool:
        return (i, False)

    return (find_vertical(transpose(m)), True)


def value(m):
    '''Returns value of pattern for part 1'''
    i, horiz = find_mirror(m)
    if horiz:
        return 100 * (i + 1)
    return i + 1


def solve(inp, part2=False):
    patterns = [p.splitlines() for p in inp.split('\n\n')]

    return sum(value(m) for m in patterns)


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
