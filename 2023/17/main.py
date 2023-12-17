#!/bin/env python3
from icecream import ic
from dataclasses import dataclass
import queue
import time
from collections import defaultdict


@dataclass(frozen=True)
class Coord:
    x: int
    y: int

    def __add__(self, other):
        if isinstance(other, Coord):
            return Coord(other.x + self.x, other.y + self.y)

    def inside(self, w, h):
        return self.x in range(w) and self.y in range(h)


RIGHT = Coord(1, 0)
LEFT = Coord(-1, 0)
UP = Coord(0, -1)
DOWN = Coord(0, 1)

turn_left = {
    RIGHT: UP,
    UP: LEFT,
    LEFT: DOWN,
    DOWN: RIGHT
}

turn_right = {
    RIGHT: DOWN,
    UP: RIGHT,
    LEFT: UP,
    DOWN: LEFT
}


@dataclass
class State:
    pos: Coord
    dirn: Coord
    cost: int
    inrow: int
    # hist: list[Coord]

    # def path_to_str(self, w, h):
    #     m = [[' .. ' for _ in range(w)] for _ in range(h)]
    #     for i, s in enumerate(self.hist + [self]):
    #         m[s.pos.y][s.pos.x] = str(s.cost).center(4)
    #     return '\n'.join(''.join(l) for l in m)


def min_path(m, part2):
    '''Given a matrix of numbers `m`,
    return the minimum sum of numbers on a path from (0,0) to bottom-right corner.'''

    def next_states(s):
        nexts = []

        if part2 and s.inrow < 4:
            possible_dirs = (s.dirn,)
        else:
            possible_dirs = (turn_right[s.dirn], s.dirn, turn_left[s.dirn])
        max_inrow = 10 if part2 else 3

        for ndirn in possible_dirs:
            inrow = 1 if ndirn != s.dirn else s.inrow + 1
            if s.inrow > max_inrow:
                continue
            npos = s.pos + ndirn
            if not npos.inside(w, h):
                continue
            ncost = s.cost + m[npos.y][npos.x]
            ns = State(npos, ndirn, ncost, inrow)
            nexts.append(ns)

        return nexts


    w, h = len(m[0]), len(m)
    states = queue.SimpleQueue()

    # The very first state has a direction of None,
    # so we manually add the next two states cuz it's easier
    start = State(Coord(0, 0), None, 0, 0) # you don't incur the first block's heat loss
    state1 = State(Coord(1, 0), RIGHT, start.cost + m[0][1], 1)
    state2 = State(Coord(0, 1), DOWN, start.cost + m[1][0], 1)
    states.put(state1)
    states.put(state2)

    # pos -> (dir, inrow -> cost)
    minpaths = {Coord(x, y): defaultdict(lambda: 1_000_000_000) for x in range(w) for y in range(h)}

    # debug speed
    maxrow = 0
    maxcol = 0

    while not states.empty():
        s = states.get()

        # skip this state if there was a better one
        worse = False
        for k, cost in minpaths[s.pos].items():
            dirn, inrow = k
            if s.dirn == dirn and s.inrow >= inrow and s.cost >= cost:
                worse = True
                break
        if worse:
            continue

        # clean up minpaths
        topop = []
        for k, cost in minpaths[s.pos].items():
            dirn, inrow = k
            if s.dirn == dirn and s.inrow <= inrow and s.cost <= cost and (not part2 or inrow > 4):
                topop.append(k)
        for k in topop:
            minpaths[s.pos].pop(k, None)

        # add to minpaths
        if not part2 or s.inrow >= 4:
            minpaths[s.pos][(s.dirn, s.inrow)] = s.cost

        # debug speed
        if s.pos.x > maxrow:
            maxrow = s.pos.x
            ic(maxrow)
        if s.pos.y > maxcol:
            maxcol = s.pos.y
            ic(maxcol)

        for nstate in next_states(s):
            states.put(nstate)

    ic(minpaths[Coord(w-1, h-1)].values())
    return min(minpaths[Coord(w-1, h-1)].values())


def solve(inp, part2=False):
    m = [[int(n) for n in l] for l in inp.splitlines()]

    return min_path(m, part2)



if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not ('--debug' in sys.argv or '-d' in sys.argv):
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
