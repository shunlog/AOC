#!/bin/env python3
from icecream import ic
import queue
import collections
from dataclasses import dataclass
from itertools import chain


@dataclass(frozen=True)
class Coord:
    x: int
    y: int

    def __add__(self, other):
        if isinstance(other, Coord):
            return Coord(other.x + self.x, other.y + self.y)

@dataclass
class Beam:
    pos: Coord
    dir: Coord

    def horiz(self):
        return self.dir in (RIGHT, LEFT)

    def vert(self):
        return self.dir in (UP, DOWN)


RIGHT = Coord(1, 0)
LEFT = Coord(-1, 0)
UP = Coord(0, -1)
DOWN = Coord(0, 1)


def traverse(m, initial_beam=Beam(Coord(0, 0), RIGHT)):
    '''Returns matrix of tuples, each tuple having 2 booleans:
    (traversed_horizontal, traversed_vertical)'''

    reflected_fwd = {
        RIGHT: UP,
        LEFT: DOWN,
        DOWN: LEFT,
        UP: RIGHT
    }

    reflected_bkwd = {
        RIGHT: DOWN,
        LEFT: UP,
        DOWN: RIGHT,
        UP: LEFT
    }

    traversed = [[[False, False] for _ in range(len(m[0]))] for _ in range(len(m))]

    # each beam has an X, an Y, and a direction
    # first beam starts at (0, 0), facing right
    beams = queue.SimpleQueue()
    beams.put(initial_beam)


    while not beams.empty():
        beam = beams.get()
        ic(beam)

        # skip beam if out of bounds
        if not (beam.pos.x in range(0, len(m[0])) and beam.pos.y in range(0, len(m))):
            continue

        # skip this beam if this path has been traversed
        # (doesn't work for any char, for some reason)
        if m[beam.pos.y][beam.pos.x] == '.' and traversed[beam.pos.y][beam.pos.x][0 if beam.horiz() else 1]:
            continue

        # mark this path as traversed
        traversed[beam.pos.y][beam.pos.x][0 if beam.horiz() else 1] = True

        # move this beam one step
        match m[beam.pos.y][beam.pos.x]:
            case '.':
                beam.pos += beam.dir
                beams.put(beam)
            case '/':
                beam.dir = reflected_fwd[beam.dir]
                beam.pos += beam.dir
                beams.put(beam)
            case '\\':
                ic("bckwd", beam)
                beam.dir = reflected_bkwd[beam.dir]
                beam.pos += beam.dir
                ic("bckwd", beam)
                beams.put(beam)
            case '|':
                if beam.vert():
                    beam.pos += beam.dir
                    beams.put(beam)
                    continue
                beams.put(Beam(beam.pos + UP, UP))
                beams.put(Beam(beam.pos + DOWN, DOWN))
            case '-':
                if beam.horiz():
                    beam.pos += beam.dir
                    beams.put(beam)
                    continue
                beams.put(Beam(beam.pos + RIGHT, RIGHT))
                beams.put(Beam(beam.pos + LEFT, LEFT))
            case _:
                raise ValueError("Bad character in input")

    return traversed


def count_energized(traversed):
    def print_traversed():
        s = ''
        for l in traversed:
            for d in l:
                s += '#' if any(d) else '.'
            s += '\n'
        print(s)


    # print_traversed()
    return sum(1 if any(d) else 0 for l in traversed for d in l)


def solve(inp, part2=False):
    # m = matrix of characters
    m = [l for l in inp.splitlines()]

    if not part2:
        return count_energized(traversed)

    max_energized = 0
    for coord, direction in chain(zip(((0, y) for y in range(len(m))), [RIGHT]*len(m)),
             zip(((len(m[0])-1, y) for y in range(len(m))), [LEFT]*len(m)) ,
             zip(((x, 0) for x in range(len(m[0]))), [DOWN]*len(m[0])) ,
             zip(((x, len(m)-1) for x in range(len(m[0]))), [UP]*len(m[0]))) :
        ic(coord, direction)
        traversed = traverse(m, Beam(Coord(*coord), direction))
        energized = count_energized(traversed)
        max_energized = max(max_energized, energized)

    return max_energized


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
