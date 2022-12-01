#!/bin/env python3

def format_input(inp):
    inp = inp.split('\n\n')
    inp = [[int(x) for x in s.splitlines()] for s in inp]
    return inp

def sol(inp):
    inp = format_input(inp)
    ss = map(sum, inp)
    from heapq import nlargest
    print(sum(nlargest(3, ss)))

t = open("input.txt", 'r').read()
sol(t)
