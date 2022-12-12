#!/bin/env python3
from icecream import ic
from collections import namedtuple, deque
from pprint import pprint as pp
import dijkstra

def easy(h1, h2):
    if ord(h1) + 1 >= ord(h2):
        return True
    return False

def getedges(mp):
    W, H = len(mp[0]), len(mp)
    edges = []
    for y,l in enumerate(mp):
        for x,h in enumerate(l):
            if x < W - 1:
                hd = mp[y][x+1]
                if easy(h, hd):
                    edges.append(((x,y), (x+1,y),1))
            if y < H - 1:
                hd = mp[y+1][x]
                if easy(h, hd):
                    edges.append(((x,y), (x,y+1),1))
            if x != 0:
                hd = mp[y][x-1]
                if easy(h, hd):
                    edges.append(((x,y), (x-1,y),1))
            if y != 0:
                hd = mp[y-1][x]
                if easy(h, hd):
                    edges.append(((x,y), (x,y-1),1))
    return edges

def p1(inp):
    start = fin = None
    starts = []

    mp = []
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

    edges = getedges(mp)
    g = dijkstra.Graph()
    for e in edges:
        g.add_edge(e[0], e[1], e[2])

    d = dijkstra.DijkstraSPF(g, start)
    dist = d.get_distance(fin)
    return dist

def p2(inp):
    fin = None
    starts = []
    mp = []
    for y,l in enumerate(inp.splitlines()):
        mp.append([])
        for x,ch in enumerate(l):
            if ch == 'E':
                fin = (x,y)
                mp[y].append('z')
                continue
            if ch in ['a', 'S']:
                starts.append((x,y))
            mp[y].append(ch)

    edges = getedges(mp)
    g = dijkstra.Graph()
    for e in edges:
        g.add_edge(e[1], e[0], e[2])
    d = dijkstra.DijkstraSPF(g, fin)

    dist = []
    for start in starts:
        dist.append(d.get_distance(start))

    return min(dist)

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
