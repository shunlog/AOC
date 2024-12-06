#!/bin/env python3
import sys
from icecream import ic

from dataclasses import dataclass


@dataclass
class State:
    m: list[str]  # list of rows
    pos: tuple[int, int]  # guard position (row, column)
    dirn: str  # direction, one of [^>v<]
    # list of directions the guard had in each cell
    # e.g. visited = {(5, 5): ['^', 'v']}
    visited: dict[tuple[int, int], list[str]]


def mark(s):
    '''Mark the guard's position on the map as visited with X.'''
    r, c = s.pos
    s.m[r] = s.m[r][:c] + 'X' + s.m[r][c+1:]


def take_turn(s: State):
    '''The guard takes a turn:
    either a step forward, or a rotation.
    If the guard winds up outside the map, raise exception. '''
    rows, cols = len(s.m), len(s.m[0])
    posdiff = {'^': (-1, 0),
               '>': (0, 1),
               'v': (1, 0),
               '<': (0, -1)}
    rot_dirn = {'^': '>',
                '>': 'v',
                'v': '<',
                '<': '^'}
    npos = tuple(a+b for a, b in zip(s.pos, posdiff[s.dirn]))

    if npos[0] < 0 or npos[1] < 0 or npos[0] >= rows or npos[1] >= cols:
        raise ValueError("Guard has walked outside the map.")

    if s.m[npos[0]][npos[1]] == '#':
        # rotate
        s.dirn = rot_dirn[s.dirn]
        return

    # step forward
    s.pos = npos
    mark(s)
    return


def solve1(s: State):

    while True:
        try:
            take_turn(s)
        except:
            break

    ic(s)
    cnt = 0
    for row, rs in enumerate(s.m):
        for col, ch in enumerate(rs):
            if ch in 'X':
                cnt += 1

    return cnt


def solve2(m):
    return


def solve(inp, part2=False, debug=False):
    if not debug:
        ic.disable()

    # pre-process for both parts
    m = inp.strip().splitlines()
    for row, rs in enumerate(m):
        for col, ch in enumerate(rs):
            if ch in 'v^<>':
                pos = (row, col)
                dirn = ch
                break
    # initial state
    s = State(m, pos, dirn, {pos: [dirn]})
    # remove guard symbol from map, mark it as visited
    mark(s)
    ic(s)

    if part2:
        return solve2(s)

    return solve1(s)


if __name__ == "__main__":
    # read the file from stdin and pass to solve()
    debug = '-d' in sys.argv
    inp = sys.stdin.read()
    if '2' not in sys.argv:
        print(solve(inp, False, debug))
    if '1' not in sys.argv:
        print(solve(inp, True, debug))
