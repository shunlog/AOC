#!/bin/env python3
import sys
from icecream import ic

import copy
from itertools import product
from collections import defaultdict
from dataclasses import dataclass
from types import MappingProxyType


@dataclass
class State:
    _m: list[str]  # list of rows
    _pos: tuple[int, int]  # guard position (row, column)
    _dirn: str  # direction, one of [^>v<]
    # map the visited position to the direction the guard had
    # when she first visited it
    _visited: dict[tuple[int, int], str]

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
    def pos(self) -> tuple[int, int]:
        return self._pos

    @property
    def dirn(self) -> str:
        return self._dirn

    @property
    def visited(self) -> MappingProxyType[tuple[int, int], str]:
        return MappingProxyType(self._visited)

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
        '''Mark the guard's position on the map as visited.'''
        # skip if the position is already marked
        if self._visited.get(self._pos):
            return
        self._visited[self._pos] = self._dirn

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
    return len(s.visited)


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
    # Jump table dict:
    # given a combination (pos, dirn), gives the next (pos, dirn) after a wall is hit,
    # or False if the map edge is reached
    t: dict[tuple[tuple[int, int], str],
            [tuple[tuple[int, int], str] | False]] = {}

    for ri, row in enumerate(s.m):
        for ci, ch in enumerate(row):
            # don't pre-compute for walls
            if ch != '.':
                continue
            for dirn in '^>v<':
                s.place_guard((ri, ci), dirn)
                if simulate_until_rot(s) is False:
                    t[((ri, ci), dirn)] = False
                else:
                    t[((ri, ci), dirn)] = (s.pos, s.dirn)
    return t


def check_cycle(s: State, jump_table, new_wall_pos):
    '''Returns True if there's a cycle,
    otherwise False'''
    # stores the combinations of (position, direction) that the guard had
    # e.g. posdirs_had = {((1, 1), '^'), ...}
    posdirs_had: set[tuple[tuple[int, int], str]] = set()

    while True:
        if (s.pos[0] == new_wall_pos[0]) or (s.pos[1] == new_wall_pos[1]):
            # simulate normally if there might be the new wall in the path
            res = s.take_turn()
            # finish if the guard walks outside the bounds
            if res is False:
                return False
        else:
            # use the pre-computed location to jump to next wall
            res = jump_table[(s.pos, s.dirn)]
            # finish if the jump goes outside the bounds
            if res is False:
                return False
            pos, dirn = res
            s.place_guard(pos, dirn)

        if (s.pos, s.dirn) in posdirs_had:
            return True

        posdirs_had.add((s.pos, s.dirn))


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
        if s_fin._visited.get((r, c)) is None:
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
    # remove the guard mark from the matrix
    r, c = pos
    m[r] = m[r][:c] + '.' + m[r][c+1:]
    # initial state
    s = State(m, pos, dirn, {})

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
