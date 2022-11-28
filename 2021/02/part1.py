#!/usr/bin/env python3

fn = "part1.txt"

from icecream import ic
ic.disable()
from collections import Counter

txt = ic([l.strip().split() for l in open(fn, "r").readlines()])
data = ic([(a,int(b)) for a,b in txt])
c = Counter()
for d,s in data:
    c[d] += s
ic(c)

dep = ic(c['down'] - c['up'])
hor = ic(c['forward'])
sol = ic(dep * hor)
print(sol)
