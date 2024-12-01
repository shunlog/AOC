#!/bin/env python3
from icecream import ic
from collections import Counter

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

ls1 = sorted(l1)
ls2 = sorted(l2)

s = 0
for x, y in zip(ls1, ls2):
    d = abs(x - y)
    s += d

print(s)


c = Counter(l2)
ic(c)

s = 0
for x in l1:
    s += x * c[x]
print(s)
