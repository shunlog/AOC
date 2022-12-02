#!/bin/env python3
from icecream import ic

# 1st wins
# 1 3
# 2 1
# 3 2
#   ^ (shift == 2)
# draw
# 1 1
# 2 2
# 3 3
# (shift == 0)
# 2nd wins
# 1 2
# 2 3
# 3 1
#   ^ (shift == 1)

def format_input(inp):
    inp = [(l.split()) for l in inp.splitlines()]
    ic(inp)
    inp = [(ord(l[0])-ord('A'), ord(l[1])-ord('X')) for l in inp]
    ic(inp)
    return inp

wt = [0, 3, 6]
p2sh = [2, 0, 1]
stw = [1, 2, 0]

def score1(p):
    sh = (p[1] - p[0]) % 3
    ws = wt[stw[sh]]
    ic(ws)
    return ws + p[1] + 1

def score2(p):
    ic(p)
    w = wt[p[1]]
    ic(w)
    p2 = (p[0] + p2sh[p[1]]) % 3 + 1
    ic(p2)
    return w + p2


def sol(inp, part2=False):
    s = 0
    if not part2:
        return sum(map(score1, inp))
    else:
        return sum(map(score2, inp))

def test():
    inp = open("test.txt", 'r').read()
    inp = format_input(inp)
    print(sol(inp))
    # print(sol(inp, True))

def p2():
    ic.disable()
    inp = open("input.txt", 'r').read()
    inp = format_input(inp)
    print(sol(inp, True))


def p1():
    ic.disable()
    inp = open("input.txt", 'r').read()
    inp = format_input(inp)
    print(sol(inp))

if __name__ == "__main__":
    # test()
    p1()
    # p2()
