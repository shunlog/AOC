#!/bin/env python3

def format_input(inp):
    inp = inp.split('\n\n')
    inp = [[int(x) for x in s.splitlines()] for s in inp]
    return inp

def sol(inp):
    inp = format_input(inp)
    # ss = [sum(s) for s in inp]
    ss = map(sum, inp)
    print(max(ss))

t = open("test.txt", 'r').read()
sol(t)
