#!/bin/env python3
from icecream import ic

def fill(p, filled, xlim, ylim, zlim):
    ''' returns the set of filled pixels if filling starts at pixel p '''
    nfilled = {p}
    x,y,z = p
    for dx, dy, dz in [[-1, 0, 0], [1, 0, 0],
                       [0, -1, 0], [0, 1, 0],
                       [0, 0, -1], [0, 0, 1]]:
        nx, ny, nz = x+dx, y+dy, z+dz
        if (nx, ny, nz) not in filled and nx >= -1 and nx <= xlim and ny >= -1 and ny <= ylim and nz >= -1 and nz <= zlim:
            nfilled |= fill((nx, ny, nz), filled | nfilled,
                            xlim, ylim, zlim)

    return nfilled

def getpixels(inp):
    return {tuple(map(int, l.split(','))) for l in inp.splitlines()}

def p1(inp):
    pixels = getpixels(inp)
    A = 0
    for x,y,z in pixels:
        nc = 0
        for dx, dy, dz in [[-1, 0, 0], [1, 0, 0],
                           [0, -1, 0], [0, 1, 0],
                           [0, 0, -1], [0, 0, 1]]:
            nc += int((x+dx, y+dy, z+dz) in pixels)
        A += 6 - nc

    return A

def p2(inp):
    pixels = getpixels(inp)
    xlim = ylim = zlim = 0
    for x,y,z in pixels:
        xlim = max(x+1, xlim)
        ylim = max(y+1, ylim)
        zlim = max(z+1, zlim)

    import sys
    sys.setrecursionlimit(xlim * ylim * zlim * 10)

    f = fill((0,0,0), pixels, xlim, ylim, zlim)

    A = 0
    for x,y,z in pixels:
        for dx, dy, dz in [[-1, 0, 0], [1, 0, 0],
                           [0, -1, 0], [0, 1, 0],
                           [0, 0, -1], [0, 0, 1]]:
            A += int((x+dx, y+dy, z+dz) in f)

    return A

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
