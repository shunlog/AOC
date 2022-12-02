#!/bin/env python3
from icecream import ic

def format_input(inp):
    return inp.splitlines()

def sol(inp, part2=False):
    ic(inp)
    s = 0
    for l in inp:
        ic(l)
        s += ord(l[2]) - ord('X') + 1
        if l in ['A Z', 'C Y', 'B X']:
            s += 0
        elif ord(l[0])-ord('A') == ord(l[2])-ord('X'):
            s += 3
        else:
            s += 6
        ic(s)
    return s

if __name__ == "__main__":
    inp = open("input.txt", 'r').read()
    inp = format_input(inp)
    ic.disable()
    print(sol(inp))
    # print(sol(inp, True))
