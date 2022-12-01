#!/bin/env python3

def format_input(inp):
    inp = inp.split('\n\n')
    inp = [[int(x) for x in s.splitlines()] for s in inp]
    return inp

def sol(inp):
    inp = format_input(inp)
    ss = map(sum, inp)
    st = sorted(ss)[::-1]
    print(sum(st[:3]))

t = open("test.txt", 'r').read()
sol(t)
