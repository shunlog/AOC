#!/bin/env python3
from icecream import ic

def format_input(inp):
    return inp.splitlines()

def score1(l):
    s = ord(l[2]) - ord('X') + 1
    if l in ['A Z', 'C Y', 'B X']:
        return 0 + s
    elif ord(l[0])-ord('A') == ord(l[2])-ord('X'):
        return 3 + s
    else:
        return 6 + s

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
    ic(inp)
    s = 0
    if not part2:
        return sum(map(score1, inp))
    else:
        return sum(map(score2, inp))

if __name__ == "__main__":
    inp = open("test.txt", 'r').read()
    inp = format_input(inp)
    print(sol(inp))
    print(sol(inp, True))
