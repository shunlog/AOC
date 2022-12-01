#!/bin/env python3

def format_input(inp):
    inp = inp.split('\n\n')
    inp = [[int(x) for x in s.splitlines()] for s in inp]
    return inp

def sol(inp, part2=False):
    ss = map(sum, inp)
    if not part2:
        return max(ss)
    else:
        from heapq import nlargest
        return sum(nlargest(3, ss))

if __name__ == "__main__":
    inp = open("input.txt", 'r').read()
    inp = format_input(inp)
    print(sol(inp))
    print(sol(inp, True))
