#!/bin/env python3
from icecream import ic
from collections import namedtuple, deque
from pprint import pprint as pp
import dijkstra

def easy(h1, h2):
    if ord(h1) + 1 >= ord(h2):
        return True
    return False

def p1(inp):
    mp = []
    start = fin = None
    starts = []
    for y,l in enumerate(inp.splitlines()):
        mp.append([])
        for x,ch in enumerate(l):
            if ch == 'S':
                start = (x,y)
                mp[y].append('a')
                continue
            if ch == 'E':
                fin = (x,y)
                mp[y].append('z')
                continue
            if ch in ['a', 'S']:
                starts.append((x,y))
            mp[y].append(ch)
    assert start
    assert fin

    edges = []
    for y,l in enumerate(mp):
        for x,h in enumerate(l):
            try:
                hd = mp[y][x+1]
                if easy(h, hd):
                    edges.append(((x,y), (x+1,y),1))
                    ic(h, hd)
            except:
                pass
            try:
                hd = mp[y+1][x]
                if easy(h, hd):
                    edges.append(((x,y), (x,y+1),1))
                    ic(h, hd)
            except:
                pass
            try:
                if x == 0:
                    raise
                hd = mp[y][x-1]
                if easy(h, hd):
                    edges.append(((x,y), (x-1,y),1))
                    ic(h, hd)
            except:
                pass
            try:
                if y == 0:
                    raise
                hd = mp[y-1][x]
                if easy(h, hd):
                    edges.append(((x,y), (x,y-1),1))
                    ic(h, hd)
            except:
                pass

    g = dijkstra.Graph()
    for e in edges:
        g.add_edge(e[0], e[1], e[2])

    d = dijkstra.DijkstraSPF(g, start)
    dist = d.get_distance(fin)
    return dist

def p2(inp):
    mp = []
    start = fin = None
    starts = []
    for y,l in enumerate(inp.splitlines()):
        mp.append([])
        for x,ch in enumerate(l):
            if ch == 'S':
                start = (x,y)
                mp[y].append('a')
                continue
            if ch == 'E':
                fin = (x,y)
                mp[y].append('z')
                continue
            if ch in ['a', 'S']:
                starts.append((x,y))
            mp[y].append(ch)
    assert start
    assert fin

    edges = []
    for y,l in enumerate(mp):
        for x,h in enumerate(l):
            try:
                hd = mp[y][x+1]
                if easy(h, hd):
                    edges.append(((x,y), (x+1,y),1))
                    ic(h, hd)
            except:
                pass
            try:
                hd = mp[y+1][x]
                if easy(h, hd):
                    edges.append(((x,y), (x,y+1),1))
                    ic(h, hd)
            except:
                pass
            try:
                if x == 0:
                    raise
                hd = mp[y][x-1]
                if easy(h, hd):
                    edges.append(((x,y), (x-1,y),1))
                    ic(h, hd)
            except:
                pass
            try:
                if y == 0:
                    raise
                hd = mp[y-1][x]
                if easy(h, hd):
                    edges.append(((x,y), (x,y-1),1))
                    ic(h, hd)
            except:
                pass

    g = dijkstra.Graph()
    for e in edges:
        g.add_edge(e[1], e[0], e[2])

    mind = 100000000000

    d = dijkstra.DijkstraSPF(g, fin)

    for start in starts:
        dist = d.get_distance(start)
        mind = min(mind, dist)

    return mind

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
