#!/bin/env python3

from icecream import ic

with open("my.in") as f:
    inp = f.read()

l1 = []
l2 = []

for l in inp.split('\n'):
    if not l:
        break
    a, b = l.split()
    l1.append(int(a))
    l2.append(int(b))

ic(l1, l2)

ls1 = sorted(l1)
ls2 = sorted(l2)

s = 0
for x, y in zip(ls1, ls2):
    d = abs(x - y)
    s += d

print(s)
