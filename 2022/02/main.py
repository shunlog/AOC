#!/bin/env python3
from icecream import ic

def format_input(inp):
    inp = [(l.split()) for l in inp.splitlines()]
    ic(inp)
    inp = [(ord(l[0])-ord('A')+1, ord(l[1])-ord('X')+1) for l in inp]
    ic(inp)
    return inp

# 1st wins
# 1 3
# 2 1
# 3 2
#   ^ shifted down (shift == 1)
# draw
# 1 1
# 2 2
# 3 3
# 2nd wins (shift == 0)
# 1 2
# 2 3
# 3 1
#   ^ shifted up (shift == 2)

def score1(p):
    shp = {0: 3,
           1: 0,
           2: 6}
    sh = (p[0] - p[1]) % 3
    return shp[sh] + p[1]

def score2(l):
    t = [[3, 1, 2],
         [1, 2, 3],
         [2, 3, 1]]
    s = t[ord(l[2])-ord('X')][ord(l[0])-ord('A')]
    if l[2] == 'X':
        s += 0
    if l[2] == 'Y':
        s += 3
    if l[2] == 'Z':
        s += 6
    ic(s)
    return s

def sol(inp, part2=False):
    s = 0
    if not part2:
        return sum(map(score1, inp))
    else:
        return sum(map(score2, inp))

if __name__ == "__main__":
    inp = open("test.txt", 'r').read()
    inp = format_input(inp)
    print(sol(inp))
    # print(sol(inp, True))
