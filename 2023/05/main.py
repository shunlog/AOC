#!/bin/env python3
from icecream import ic
from more_itertools import ichunked, chunked
from random import shuffle
import queue


def intersect(a, b):
    ''' Returns the intersection of two ranges, or None
    a, b: tuples representing ranges
    E.g.: (2, 5), (4, 7) --> (4, 5)
    '''
    if a[0] > b[1] or b[0] > a[1]:  # no intersection
        return None
    return (max(a[0], b[0]), min(a[1], b[1]))


def p2(inp):
    # Check ranges instead of values.
    # For each paragraph, "silt" the seed ranges through the "filter" ranges
    # by going through each pair of source range and map

    def map_ranges(src, maps):
        '''Apply the list of maps from a paragraph to all the ranges.
        rc = [(1, 10), ...]
        maps = [((2, 3) -5), ...]'''

        def map_range(r):
            # get a list of intersecting maps (for optimization)
            intersecting_maps = [mp for mp in maps if intersect(r, mp[0])]

            # use a queue to pass all the range parts through the maps
            Q = queue.Queue()
            Q.put(r)
            while not Q.empty():
                r = Q.get()
                for mr, offset in intersecting_maps:
                    I = intersect(r, mr)
                    if not I:
                        continue

                    # add the intersection
                    I2 = (I[0] + offset, I[1] + offset) # apply offset
                    dest.append(I2)

                    # push the split ranges back to the queue, if any
                    r_left = (r[0], I[0]-1)
                    if r_left[0] <= r_left[1]:
                        Q.put(r_left)
                    r_right = (I[1]+1, r[1])
                    if r_right[0] <= r_right[1]:
                        Q.put(r_right)

                    break # go back to check the split ranges

                else: # this range didn't intersect with any map
                    dest.append(r)

        dest = []
        ic(len(src))
        for r in src:
            map_range(r)

        return dest

    # parse input: seeds, maps_list
    pl = inp.split('\n\n')

    paragraphs = pl[1:]
    maps_list = []
    for p in paragraphs:
        mapl = []
        for l in p.splitlines()[1:]:
            nl = tuple(int(n) for n in l.split())
            start = nl[1]
            end = start + nl[2] - 1
            offset = nl[0] - start
            mapl.append(((start, end), offset))
        maps_list.append(mapl)

    seeds = [(start, start+sz-1) for start, sz in ichunked((int(n) for n in pl[0].split()[1:]), 2)]

    # apply maps from every paragraph
    for maps in maps_list:
        seeds = map_ranges(seeds, maps)

    return min(r[0] for r in seeds)


def p1(inp):
    def map_value(m, v):
        # (dest, source, len), z  --> mapped z
        # for each line in list of maps `m`
        for l in m:
            dest, src, size = l
            if v in range(src, src + size + 1):
                return dest + (v - src)
        return v

    pl = inp.split('\n\n')
    seeds = [int(n) for n in pl[0].split()[1:]]
    maps = []
    for p in pl[1:]: # paragraphs
        m = [[int(n) for n in l.split()] for l in p.splitlines()[1:]]
        maps.append(m)

    source = seeds.copy()
    dest = [0] * len(source)
    for m in maps:
        for i, s in enumerate(source):
            dest[i] = map_value(m, s)
        source = dest.copy()

    return min(dest)

def solve(inp, part2=False):
    if part2:
        return p2(inp)
    return p1(inp)



if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
