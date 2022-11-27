#!/bin/env python3

fn = "part1"
data = open(f"/home/awh/Projects/mine/aoc/2021/01/{fn}.txt", 'r').read()
d = list(map(int, data.split()))
l = list(map(sum, zip(d, d[1:], d[2:])))
s = sum(map(lambda p: int(p[0] < p[1]), zip(l, l[1:])))
print(s)
