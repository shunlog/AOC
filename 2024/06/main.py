#!/bin/env python3
import sys
from icecream import ic

import copy
from itertools import product
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class State:
    m: list[str]  # list of rows
    pos: tuple[int, int]  # guard position (row, column)
    dirn: str  # direction, one of [^>v<]


def mark(s):
    '''Mark the guard's position on the map as visited with X'''
    r, c = s.pos
    s.m[r] = s.m[r][:c] + 'X' + s.m[r][c+1:]


posdiff = {'^': (-1, 0),
           '>': (0, 1),
           'v': (1, 0),
           '<': (0, -1)}
rot_dirn = {'^': '>',
            '>': 'v',
            'v': '<',
            '<': '^'}


def take_turn(s: State):
    '''The guard takes a turn:
    either a step forward, or a rotation.
    Return None if the guard winds up outside the map.
    Return True if a cycle is detected.'''
    rows, cols = len(s.m), len(s.m[0])

    npos = tuple(a+b for a, b in zip(s.pos, posdiff[s.dirn]))

    if npos[0] < 0 or npos[1] < 0 or npos[0] >= rows or npos[1] >= cols:
        return None

    if s.m[npos[0]][npos[1]] == '#':
        # rotate
        s.dirn = rot_dirn[s.dirn]
        mark(s)
        return False

    # step forward
    s.pos = npos
    mark(s)
    return False


def run_until_complete(s: State):
    '''Run the simulation until the guard exits the map,
    assuming she will eventually.'''
    while True:
        res = take_turn(s)
        if res == None:
            break
    return s


def solve1(s: State):
    run_until_complete(s)
    cnt = 0
    for row, rs in enumerate(s.m):
        for col, ch in enumerate(rs):
            if ch in 'X':
                cnt += 1
    return cnt


def check_cycle(s: State):
    '''Returns True if there's a cycle,
    otherwise False'''
    # stores the combinations of (position, direction) that the guard had
    # e.g. visited = {((1, 1), '^'), ...}
    visited: set[tuple[tuple[int, int], str]] = set()

    while True:
        res = take_turn(s)
        if res == None:
            return False

        if (s.pos, s.dirn) in visited:
            return True

        visited.add((s.pos, s.dirn))


def solve2(s: State):
    ans = []

    # we only have to try and block the original path of the guard,
    # so the other squares can be ignored
    # for that, we first simulate the grid to get the original visited ceills
    s_fin = copy.deepcopy(s)
    run_until_complete(s_fin)

    it = 0  # count the number of obstacles tried
    for r, c in product(range(len(s.m)), range(len(s.m[0]))):
        # skip if this cell won't be visited
        if s_fin.m[r][c] != 'X':
            continue

        s_copy = copy.deepcopy(s)
        s_copy.m[r] = s.m[r][:c] + '#' + s.m[r][c+1:]

        res = check_cycle(s_copy)
        it += 1
        if res == True:
            ans.append((r, c))

    ic(it)
    return len(ans)


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
    s = State(m, pos, dirn)
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
