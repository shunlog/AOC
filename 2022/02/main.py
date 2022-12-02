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
    inp = [(ord(l[0])-ord('A'), ord(l[1])-ord('X')) for l in inp]
    return inp

ots = [0, 3, 6] # outcome to score
otsh = [2, 0, 1] # outcome to shift
shto = [1, 2, 0] # shift to outcome

def p1(inp):
    s = lambda p: ots[shto[(p[1] - p[0]) % 3]] + p[1] + 1
    return sum(map(s, inp))

def p2(inp):
    s = lambda p: ots[p[1]] + (p[0] + otsh[p[1]]) % 3 + 1
    return sum(map(s, inp))

if __name__ == "__main__":
    inp = open("input.txt", 'r').read()
    inp = format_input(inp)
    print(p1(inp))
    print(p2(inp))
