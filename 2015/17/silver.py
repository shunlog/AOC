#!/usr/bin/env python3
from itertools import combinations as comb

ls = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]

res = len([list(j) for i in range(1,len(ls)) for j in comb(ls,i) if sum(list(j))==150])

print(res)
