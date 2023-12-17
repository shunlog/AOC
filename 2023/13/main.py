#!/bin/env python3
from icecream import ic


def transpose(m):
    return [*map(list, zip(*m))]


def find_mirror(m, part2):
    ''' The same as find_mirror,
    but there has to be exactly one error (smudge).'''

    def find_vertical(m):
        '''Returns column after which the mirror can be, or False'''

        def count_errors_in_column(m, i):
            '''Returns the number of errors (smudges) if the mirror is after column i'''
            s = 0
            for r in m:
                left = r[:i+1]
                right = r[i+1:]
                s += sum(int(p[0] != p[1]) for p in zip(left[::-1], right))
            return s

        for i in range(len(m[0])-1):
            if count_errors_in_column(m, i) == (1 if part2 else 0):
                return i
        return False

    # try all vertical positions
    if not isinstance(i := find_vertical(m), bool):
        return (i, False)

    # else try all horizontal positions
    return (find_vertical(transpose(m)), True)


def value(m, part2):
    '''Returns the value of pattern'''
    i, horiz = find_mirror(m, part2)
    if horiz:
        return 100 * (i + 1)
    return i + 1


def solve(inp, part2=False):
    patterns = [p.splitlines() for p in inp.split('\n\n')]
    return sum(value(m, part2) for m in patterns)


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
