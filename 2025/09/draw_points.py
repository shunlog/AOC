
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
