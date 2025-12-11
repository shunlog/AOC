#!/usr/bin/env python3
from builtins import ValueError
import sys
from icecream import ic
import itertools
import heapq
from dataclasses import dataclass

ic.disable()


@dataclass(frozen=True)
class Posn:
    x: int
    y: int


@dataclass(frozen=True)
class Seg:
    '''A rectilinear segment (parallel to one of the Cartesian axes).
    Invariants:
    - either min_x == max_x or min_y == max_y
    '''
    min_x: int
    min_y: int
    max_x: int
    max_y: int

    @classmethod
    def from_posns(cls, p1: Posn, p2: Posn):
        min_x, max_x = min(p1.x, p2.x), max(p1.x, p2.x)
        min_y, max_y = min(p1.y, p2.y), max(p1.y, p2.y)
        return cls(min_x, min_y, max_x, max_y)

    def __post_init__(self):
        if not ((self.min_x == self.max_x) or (self.min_y == self.max_y)):
            raise ValueError("Segment must be rectilinear")

    def is_horiz(self) -> bool:
        return self.min_y == self.max_y


def segs_intersect(s1: Seg, s2: Seg) -> bool:
    '''Returns whether the two Seg's intersect.
    Overlapping does not count, thus they must be perpendicular to intersect.
    Endpoints touching the other segment does not count either.
    '''
    if s1.is_horiz() == s2.is_horiz():
        return False

    # name as horizontal and vertical
    hs, vs = (s1, s2) if s1.is_horiz() else (s2, s1)
    return ((hs.min_x < vs.min_x < hs.max_x)
            and (vs.min_y < hs.min_y < vs.max_y))


def test_intersect_segs():
    assert segs_intersect(Seg.from_posns(Posn(0, 2), Posn(4, 2)),
                          Seg.from_posns(Posn(1, 1), Posn(1, 4)))
    assert not segs_intersect(Seg.from_posns(Posn(0, 2), Posn(4, 2)),
                              Seg.from_posns(Posn(1, 1), Posn(1, 2)))


@dataclass(frozen=True)
class Rect:
    '''A rectilinear Rectangle (sides are parallel to the Cartesian axes).
    Invariants:
    - min_x <= max_x
    - min_y <= max_y
    '''
    min_x: int
    min_y: int
    max_x: int
    max_y: int

    @classmethod
    def from_posns(cls, p1: Posn, p2: Posn):
        min_x, max_x = min(p1.x, p2.x), max(p1.x, p2.x)
        min_y, max_y = min(p1.y, p2.y), max(p1.y, p2.y)
        return cls(min_x, min_y, max_x, max_y)

    def width(self) -> int:
        return self.max_x - self.min_x + 1

    def height(self) -> int:
        return self.max_y - self.min_y + 1

    def area(self) -> int:
        return self.width() * self.height()

    def contains(self, p: Posn) -> bool:
        '''Returns True if point is inside rect.
        Touching the side doesn't count as inside'''
        return ((self.min_x < p.x < self.max_x)
                and (self.min_y < p.y < self.max_y))

    def segments(self) -> list[Seg]:
        '''Returns the sides of the Rect as Seg's'''
        # get the 4 corners
        tl, tr = Posn(self.min_x, self.min_y), Posn(self.max_x, self.min_y)
        bl, br = Posn(self.min_x, self.max_y), Posn(self.max_x, self.max_y)
        return [Seg.from_posns(tl, tr),
                Seg.from_posns(tl, bl),
                Seg.from_posns(br, bl),
                Seg.from_posns(br, tr)]

    def intersects(self, s: Seg) -> bool:
        '''Return True if a segment intersects the Rect.
        It intersects if either the segment intersects any of the sides,
        or the segment is on the inside but touching the sides.
        A segment that is fully inside (maybe touching sides) also intersects it.
        '''
        intersects_side = any(segs_intersect(side, s)
                              for side in self.segments())
        # inside or touching, maybe overlapping
        inside = (s.min_x >= self.min_x
                  and s.max_x <= self.max_x
                  and s.min_y >= self.min_y
                  and s.max_y <= self.max_y)
        overlapping = s.min_y in (self.min_y, self.max_y) if s.is_horiz() else \
            s.min_x in (self.min_x, self.max_x)
        return intersects_side or (inside and not overlapping)


def test_rect_intersects():
    # Test partitions:
    # 1. Vertical/horizontal segment
    # 2. Segment position:
    #    outside, outside but touching, overlapping with side,
    #    point inside, point touching second side, crossing over,
    #    inside but touching sides
    r = Rect(2, 2, 4, 4)
    # horizontal segment, centered vertically
    assert not r.intersects(Seg(0, 3, 1, 3))  # outside
    assert not r.intersects(Seg(0, 3, 2, 3))  # point touching
    assert r.intersects(Seg(0, 3, 3, 3))  # point inside
    assert r.intersects(Seg(0, 3, 4, 3))  # point on second side
    assert r.intersects(Seg(0, 3, 5, 3))  # crossing over
    assert r.intersects(Seg(2, 3, 4, 3))  # inside, touching both sides
    # horizontal, below
    assert not r.intersects(Seg(0, 5, 3, 5))
    # vertical, overlapping
    assert not r.intersects(Seg(2, 1, 2, 3))
    assert not r.intersects(Seg(4, 2, 4, 4))  # other side, fully overlapping


def solve1(red_tiles: list[Posn]):
    pairs = itertools.combinations(red_tiles, 2)
    return max(Rect.from_posns(p1, p2).area() for (p1, p2) in pairs)


# The shape looks like a circle with a narrow island cutting it in half:
# 2287,50126
# 94997,50126
# 94997,48641
# 1738,48641

def solve2(red_tiles: list[Posn]):
    segments: list[Seg] = list(Seg.from_posns(p1, p2)
                               for (p1, p2) in itertools.pairwise(red_tiles+red_tiles[:1]))

    def valid_rect(r: Rect) -> bool:
        return not any(r.intersects(seg) for seg in segments)

    # There are 500 corners, so combi(500, 2) ~ 120k combinations
    max_area = 0
    combi = itertools.combinations(red_tiles, 2)
    for (p1, p2) in combi:
        r = Rect.from_posns(p1, p2)
        # Important: check area first for a speed-up
        if r.area() > max_area and valid_rect(r):
            max_area = r.area()

    return max_area


def solve(inp, part2=False):
    tiles = [Posn(*(int(n) for n in l.split(',')))
             for l in inp.strip().split()]
    if part2:
        return solve2(tiles)
    return solve1(tiles)


if __name__ == "__main__":
    '''
    $ ./main.py                    # reads input.txt
    $ ./main.py -v -1 example.txt   # turns on logging, run only part 1
    '''

    last_arg = sys.argv[-1]
    if '.txt' in last_arg:
        fn = last_arg
    else:
        fn = "input.txt"
    with open(fn) as f:
        inp = f.read()

    if '-v' in sys.argv:
        ic.enable()

    if '-2' not in sys.argv:
        print(solve(inp, False))
    if '-1' not in sys.argv:
        print(solve(inp, True))
