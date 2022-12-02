#!/bin/env python3
from icecream import ic

def format_input(inp):
    return inp.splitlines()

def sol(inp, part2=False):
    ic(inp)
    s = 0
    for l in inp:
        ic(l)
        t = [[3, 1, 2],
             [1, 2, 3],
             [2, 3, 1]]
        s += t[ord(l[2])-ord('X')][ord(l[0])-ord('A')]
        if l[2] == 'X':
            s += 0
        if l[2] == 'Y':
            s += 3
        if l[2] == 'Z':
            s += 6
        ic(s)
    return s

if __name__ == "__main__":
    inp = open("input.txt", 'r').read()
    inp = format_input(inp)
    # ic.disable()
    print(sol(inp))
    # print(sol(inp, True))
