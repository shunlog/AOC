#!/usr/bin/env python3

fn = "part1.txt"

from icecream import ic
# ic.disable()
from collections import Counter

txt = ic([l.strip().split() for l in open(fn, "r").readlines()])
data = ic([(a,int(b)) for a,b in txt])
dh = 0
aim = 0
h = 0
for d,s in data:
    if d == 'up':
        aim -= s
    elif d == 'down':
        aim += s
    else:
        h += s
        dh += aim * s
    ic(d,s,aim,dh,h)

sol = ic(h * dh)
print(sol)
