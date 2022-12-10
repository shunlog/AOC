#!/bin/env python3
from icecream import ic

def p1(inp):
    inp = inp.splitlines()
    X = 1
    c = 0
    Xh = []
    for l in inp:
        if 'noop' in l:
            Xh.append(X)
        else:
            t = l.split()
            Xh.append(X)
            Xh.append(X)
            X += int(t[-1])

    v = [Xh[i-1] * i for i in range(20, len(Xh), 40)]
    ic(v)
    return sum(v)

def p2(inp):
    inp = inp.splitlines()
    X = 1
    scr = []
    y = 0
    x = 0
    lp = '#'
    dp = '.'
    t = 0
    ins = ''
    line = []

    for c in range(40*6):
        if t == 0:
            if 'addx' in ins:
                X += int(ins.split()[-1])
            ins = inp.pop(0)
            if 'noop' in ins:
                t = 1
            else:
                t = 2
        line.append(lp if x in [X-1, X, X+1] else dp)
        x += 1
        t -= 1
        if x >= 40:
            x = 0
            scr.append(line)
            line = []

    return '\n'.join([''.join(l) for l in scr])

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
