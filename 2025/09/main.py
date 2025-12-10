#!/usr/bin/env python3
import sys
from icecream import ic
import itertools

ic.disable()

# A Tile is represented as a tuple (x, y)
# interpreted as the coordinates of the tile


def area(t1, t2):
    return (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)


def solve1(tiles):
    combi = list(itertools.combinations(tiles, 2))
    return max(ic(area(t1, t2)) for (t1, t2) in combi)


def draw_margins(red_tiles):
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
    draw(all_tiles)


def draw(points):
    import matplotlib.pyplot as plt
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    plt.figure(figsize=(5, 5))
    plt.scatter(xs, ys, marker='s', s=1)  # s controls pixel size (square)
    plt.gca().invert_yaxis()                # optional, for matrix-style orientation
    plt.gca().set_aspect('equal', 'box')
    plt.grid(True, color='lightgray')
    plt.show()


# Find the outliers:
# 2287,50126
# 94997,50126
# 94997,48641
# 1738,48641


def solve2(tiles):
    def intersects_middle_gap(t1, t2):
        y1, y2 = t1[1], t2[1]
        miny, maxy = min(y1, y2), max(y1, y2)
        no_intersection = maxy < 48641 or miny > 50126
        return not no_intersection

    combi = list(itertools.combinations(tiles, 2))
    return max(ic(area(t1, t2)) for (t1, t2) in combi
               if not intersects_middle_gap(t1, t2))


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
