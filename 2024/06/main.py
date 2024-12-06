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


def simulate_until_rot(s: State):
    '''Given a state, simulate it until the next rotation and return True,
    or return None if the edge was reached'''
    while True:
        dirn0 = s.dirn
        if take_turn(s) is None:
            return None
        dirn1 = s.dirn
        if dirn1 != dirn0:  # last turn was a rotation
            return True


def compute_jump_table(s: State):
    # given a combination (pos, dirn), return the next (pos, dirn) after a wall is hit,
    # or return None if the map edge is reached
    t: dict[tuple[tuple[int, int], str], tuple[tuple[int, int], str]]
    t = {}
    for ri, row in enumerate(s.m):
        for ci, ch in enumerate(row):
            # no need to pre-compute for walls
            if ch not in '.X':
                continue
            for dirn in '^>v<':
                s.pos = (ri, ci)
                s.dirn = dirn
                if simulate_until_rot(s) is None:
                    dest = None
                else:
                    dest = (s.pos, s.dirn)
                t[((ri, ci), dirn)] = dest
    return t


def check_cycle(s: State, jump_table, new_wall_pos):
    '''Returns True if there's a cycle,
    otherwise False'''
    # stores the combinations of (position, direction) that the guard had
    # e.g. visited = {((1, 1), '^'), ...}
    visited: set[tuple[tuple[int, int], str]] = set()

    while True:
        if (s.pos[0] == new_wall_pos[0]) or (s.pos[1] == new_wall_pos[1]):
            # simulate normally if there might be the new wall in the path
            res = take_turn(s)
            if res is None:
                return False
        else:
            # use the pre-computed location to jump to next wall
            res = jump_table[(s.pos, s.dirn)]
            if res is None:
                return False
            s.pos, s.dirn = res[0], res[1]

        if (s.pos, s.dirn) in visited:
            return True

        visited.add((s.pos, s.dirn))


def solve2(s: State):
    # we only have to try and block the original path of the guard,
    # so the other squares can be ignored
    # for that, we first simulate the grid to get the original visited ceills
    s_fin = copy.deepcopy(s)
    run_until_complete(s_fin)

    s_precomp = copy.deepcopy(s)
    jump_table = compute_jump_table(s_precomp)

    ans = []
    it = 0  # count the number of obstacles tried
    for r, c in product(range(len(s.m)), range(len(s.m[0]))):
        # skip if this cell won't be visited
        if s_fin.m[r][c] != 'X':
            continue

        s_copy = copy.deepcopy(s)
        s_copy.m[r] = s.m[r][:c] + '#' + s.m[r][c+1:]

        res = check_cycle(s_copy, jump_table, (r, c))
        it += 1
        if res is True:
            ans.append((r, c))

    ic(ans[:20])
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
