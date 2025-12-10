#!/usr/bin/env python3
import sys
from icecream import ic
import itertools
import heapq

ic.disable()

# A Tile is represented as a tuple (x, y)
# interpreted as the coordinates of the tile


def area(t1, t2):
    return (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)


def solve1(tiles):
    combi = list(itertools.combinations(tiles, 2))
    return max(ic(area(t1, t2)) for (t1, t2) in combi)


def draw_margins(red_tiles, t1=None, t2=None):
    all_tiles = set()
    for rt1, rt2 in zip(red_tiles, red_tiles[1:]+red_tiles[:0]):
        if rt1[1] == rt2[1]:
            start, fin = min(rt1[0], rt2[0]), max(rt1[0], rt2[0])
            for dx in range(fin-start+1):
                all_tiles.add((start+dx, rt1[1]))
        elif rt1[0] == rt2[0]:
            start, fin = min(rt1[1], rt2[1]), max(rt1[1], rt2[1])
            for dy in range(fin-start+1):
                all_tiles.add((rt1[0], start+dy))
    draw(all_tiles, t1, t2)


def draw(points, t1=None, t2=None):
    import matplotlib.pyplot as plt
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    plt.figure(figsize=(5, 5))
    plt.scatter(xs, ys, marker='s', s=1)  # s controls pixel size (square)

    if t1 and t2:
        # draw segments
        x1, y1 = t1
        x2, y2 = t2
        c1, c2, c3, c4 = ((x1, y1), (x1, y2), (x2, y2), (x2, y1))
        for (x1, y1), (x2, y2) in ((c1, c2), (c2, c3), (c3, c4), (c1, c4)):
            plt.plot([x1, x2], [y1, y2], color="red", linewidth=2)

    plt.gca().invert_yaxis()                # optional, for matrix-style orientation
    plt.gca().set_aspect('equal', 'box')
    plt.grid(True, color='lightgray')
    plt.show()


def intersect_segs(seg1, seg2):
    '''Returns whether the two segments intersect.
    Assuming the segments are parallel with x- or y-axis.
    Overlapping does not count as intersection.'''
    if seg1[0][0] == seg1[1][0] and seg2[0][0] == seg2[1][0]:
        # segments must be perpendicular to intersect
        return False

    V, H = (seg1, seg2) if seg1[0][0] == seg1[1][0] else (seg2, seg1)
    Vymin, Vymax = min(V[0][1], V[1][1]), max(V[0][1], V[1][1])
    Hxmin, Hxmax = min(H[0][0], H[1][0]), max(H[0][0], H[1][0])
    Vx, Hy = V[0][0], H[0][1]
    return (Hxmin < Vx < Hxmax) and (Vymin < Hy < Vymax)


def test_intersect_segs():
    assert intersect_segs(((0, 2), (4, 2)), ((1, 1), (1, 4)))
    assert not intersect_segs(((0, 2), (4, 2)), ((1, 1), (1, 2)))


def intersect_shapes(sh1: list[tuple], sh2: list[tuple]):
    sh1_segs = itertools.pairwise(sh1+sh1[:1])
    sh2_segs = itertools.pairwise(sh2+sh2[:1])
    return any(intersect_segs(s1, s2)
               for s1 in sh1_segs
               for s2 in sh2_segs)


def solve2(tiles):

    def intersects_middle_gap(t1, t2):
        # Find the outliers by looking at viz:
        # 2287,50126
        # 94997,50126
        # 94997,48641
        # 1738,48641
        y1, y2 = t1[1], t2[1]
        miny, maxy = min(y1, y2), max(y1, y2)
        no_intersection = maxy < 48641 or miny > 50126
        return not no_intersection

    combi = list(itertools.combinations(tiles, 2))
    # -> ((tile1, tile2), area)
    areas = (((t1, t2), area(t1, t2))
             for (t1, t2) in combi
             if not intersects_middle_gap(t1, t2))
    top = heapq.nlargest(100,
                         areas,
                         lambda t: t[1])

    def rect_corners_to_points(p1, p2) -> list[tuple]:
        x1, y1 = p1
        x2, y2 = p2
        return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

    for ((t1, t2), ar) in top:
        rect_points = rect_corners_to_points(t1, t2)
        if intersect_shapes(rect_points, tiles):
            ic("skip", (t1, t2, ar))
            continue
        ic(t1, t2, ar)
        break

    if ic.enabled:
        draw_margins(tiles, t1, t2)

    return


def solve(inp, part2=False):
    tiles = [[int(n) for n in l.split(',')]
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
