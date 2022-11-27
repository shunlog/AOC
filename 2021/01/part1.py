#!/usr/bin/env python3

fn = "part1"
data = open(f"/home/awh/Projects/mine/aoc/2021/01/{fn}.txt", 'r').read()
d = list(map(int, data.split()))
ps = list(zip(d, d[1:]))
s = sum(map(lambda p: int(p[1] > p[0]), ps))
print(s)
