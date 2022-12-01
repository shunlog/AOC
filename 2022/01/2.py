#!/bin/env python3

def sol(inp):
    inp = inp.split('\n\n')
    inp = [s.splitlines() for s in inp]
    ss = [sum([int(x) for x in s]) for s in inp]
    st = sorted(ss)[::-1]
    print(sum(st[:3]))

t = open("input.txt", 'r').read()
sol(t)
