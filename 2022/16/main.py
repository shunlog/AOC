#!/bin/env python3
import re
from collections import defaultdict
from icecream import ic
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.shortestpaths.floydwarshall import FloydWarshall

def ints(s):
    return [int(i) for i in re.findall(r'-?\d+', s)]

def re_valves(s):
    return list(re.findall(r'[A-Z]{2}', s))

cnt = 0

def dfs(m, t, path, valves, FW):
    rem = dict(filter(lambda x: x[0] not in path, valves.items()))
    if len(rem) == 0:
        ic(path)
        return m
    global cnt
    cnt += 1
    # ic(cnt)

    maxm = m
    for vn, val in rem.items():
        tt = t + FW[vn][path[-1]]
        remt = 30 - tt
        if remt <= 0:
            continue
        sumval = remt * val
        newm = dfs(m + sumval, tt, path+[vn], valves, FW)
        maxm = max(maxm, newm)

    return maxm

mem = defaultdict(int)

def dfs2(m, t, path, valves, FW):
    global mem
    mem[frozenset(path)] = max(mem[frozenset(path)], m)

    rem = dict(filter(lambda x: x[0] not in path, valves.items()))
    if len(rem) == 0:
        return m
    global cnt
    cnt += 1
    # ic(cnt)

    maxm = m
    for vn, val in rem.items():
        tt = t + FW[vn][path[-1]]
        remt = 26 - tt
        if remt <= 0:
            continue
        sumval = remt * val
        newm = dfs2(m + sumval, tt, path+[vn], valves, FW)
        maxm = max(maxm, newm)

    return maxm

def parse_valves(inp):
    G = Graph(n=10, directed=True)
    valves = {}

    for l in inp.splitlines():
        vl = re_valves(l)
        v1 = vl[0]
        valves[v1] = ints(l)[0]
        for v2 in vl[1:]:
            try:
                G.add_edge(Edge(v1, v2, 1))
                G.add_edge(Edge(v2, v1, 1))
            except ValueError:
                pass

    valves = dict(filter(lambda x: x[1] > 0, valves.items()))

    algorithm = FloydWarshall(G)
    algorithm.run()
    FW = defaultdict(dict)
    for v in algorithm.distance.items():
        for v2 in v[1].items():
            FW[v[0]][v2[0]] = v2[1] + 1
    return valves, FW

def p1(inp):
    valves, FW = parse_valves(inp)
    return dfs(0, 0, ['AA'], valves, FW)

def p2(inp):
    valves, FW = parse_valves(inp)
    dfs2(0, 0, ['AA'], valves, FW)
    global mem

    maxv = 0
    for s1,v1 in mem.items():
        for s2,v2 in mem.items():
            if s1 == s2:
                continue
            sAA = frozenset({'AA'})
            s12 = s1 - sAA
            s22 = s2 - sAA
            if s12.isdisjoint(s22):
                maxv = max(maxv, v1 + v2)

    return maxv

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
