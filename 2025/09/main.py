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



def solve1(red_tiles: list[Posn]):
    pairs = itertools.combinations(red_tiles, 2)
    return max(Rect.from_posns(p1, p2).area() for (p1, p2) in pairs)



# Find the outliers by looking at viz:
# 2287,50126
# 94997,50126
# 94997,48641
# 1738,48641

def solve2(red_tiles: list[Posn]):
    segs :list[Seg] = list(Seg.from_posns(p1, p2)
                           for (p1, p2) in itertools.pairwise(red_tiles+red_tiles[:1]))
    pairs = itertools.combinations(red_tiles, 2)

    def valid_rect(r: Rect) -> bool:
        no_points_inside = not any(r.contains(t) for t in red_tiles)
        no_intersections = not any(segs_intersect(rect_side, seg)
                for rect_side in r.segments()
                for seg in segs)
        return no_points_inside and no_intersections

    max_area = 0
    rect = None
    for (p1, p2) in pairs:
        r = Rect.from_posns(p1, p2)
        if valid_rect(r) and r.area() > max_area:
            rect, max_area = r, r.area()
            ic(rect, max_area)
        
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
