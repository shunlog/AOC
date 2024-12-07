#!/bin/env python3
import sys
from icecream import ic

import copy
from itertools import product
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class State:
    _m: list[str]  # list of rows
    _pos: tuple[int, int]  # guard position (row, column)
    _dirn: str  # direction, one of [^>v<]

    # 1. to disalolw the user to set the fields directly,
    # make them "private" with the _x notation
    # 2. to still allow the user to read the data,
    # give him immutable counterparts for each private method
    # e.g. list -> tuple, dict -> MappingProxyType, set -> frozenset
    # list[list] -> deep copy

    # This still doesn't protect from mutating elements of containers
    # e.g. mutating the list of the returned tuple,
    # so as a rule of thumb, there should be no mutations outside the class methods.

    @property
    def m(self):
        return tuple(self._m)

    @property
    def pos(self):
        return self._pos

    @property
    def dirn(self):
        return self._dirn

    posdiff = {'^': (-1, 0),
               '>': (0, 1),
               'v': (1, 0),
               '<': (0, -1)}

    rot_dirn = {'^': '>',
                '>': 'v',
                'v': '<',
                '<': '^'}

    def __post_init__(self):
        # make sure the guard is not placed on a wall
        r, c = self._pos
        assert self._m[r][c] != '#'

        # make sure the position is marked as visited
        self._mark()

    def _mark(self):
        '''Mark the guard's position on the map as visited with X'''
        r, c = self._pos
        # skip if the position is already marked
        if self._m[r][c] == 'X':
            return
        self._m[r] = self._m[r][:c] + 'X' + self._m[r][c+1:]

    def place_guard(self, npos, dirn=None):
        r, c = npos
        # check that the guard isn't placed on a wall
        assert self._m[r][c] != '#'

        self._pos = npos
        if dirn:
            self._dirn = dirn
        self._mark()

    def put_wall(self, pos):
        # make sure the wall is not placed on the guard
        assert self._pos != pos
        r, c = pos
        self._m[r] = self._m[r][:c] + '#' + self._m[r][c+1:]

    def rotate_guard(self):
        '''Rotate guard clockwise'''
        self._dirn = self.rot_dirn[self._dirn]

    def take_turn(self):
        '''The guard takes a turn:
        either a step forward, or a rotation.
        Return False if the guard winds up outside the map.'''

        # the position in front of the guard
        p = self._pos
        d = self.posdiff[self._dirn]  # delta
        npos = (p[0] + d[0], p[1] + d[1])

        rows, cols = len(self._m), len(self._m[0])
        if npos[0] < 0 or npos[1] < 0 or npos[0] >= rows or npos[1] >= cols:
            return False

        # rotate if wall in front
        if self._m[npos[0]][npos[1]] == '#':
            self.rotate_guard()
            return True

        # otherwise just step forward
        self.place_guard(npos)
        return True


def run_until_complete(s: State):
    '''Run the simulation until the guard exits the map,
    assuming she will eventually.'''
    while True:
        res = s.take_turn()
        if res is False:
            break
    return s


def solve1(s: State):
    run_until_complete(s)
    cnt = 0
    for row, rs in enumerate(s.m):
        for col, ch in enumerate(rs):
            if ch == 'X':
                cnt += 1
    return cnt


def simulate_until_rot(s: State):
    '''Given a state, simulate it until the next rotation and return True,
    or return False if the edge was reached'''
    while True:
        dirn0 = s.dirn
        if s.take_turn() is False:
            return False
        dirn1 = s.dirn
        if dirn1 != dirn0:  # last turn was a rotation
            return True


def compute_jump_table(s: State):
    # given a combination (pos, dirn), return the next (pos, dirn) after a wall is hit,
    # or return False if the map edge is reached
    t: dict[tuple[tuple[int, int], str], tuple[tuple[int, int], str]]
    t = {}
    for ri, row in enumerate(s.m):
        for ci, ch in enumerate(row):
            # don't pre-compute for walls or for the original position
            if ch not in '.X':
                continue
            for dirn in '^>v<':
                s.place_guard((ri, ci), dirn)
                if simulate_until_rot(s) is False:
                    dest = False
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
            res = s.take_turn()
            if res is False:
                return False
        else:
            # use the pre-computed location to jump to next wall
            res = jump_table[(s.pos, s.dirn)]
            if res is False:
                return False
            pos, dirn = res
            s.place_guard(pos, dirn)

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
    it = 0  # count the number of walls placed and  simulated

    # try putting a wall in every free spot
    for r, c in product(range(len(s.m)), range(len(s.m[0]))):
        # skip if this cell won't be visited
        if s_fin.m[r][c] != 'X':
            continue
        # skip the starting position of the guard
        if r == s.pos[0] and c == s.pos[1]:
            continue

        s_copy = copy.deepcopy(s)
        s_copy.put_wall((r, c))

        res = check_cycle(s_copy, jump_table, (r, c))
        it += 1
        if res is True:
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
