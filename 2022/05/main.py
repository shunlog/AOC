#!/bin/env python3
from icecream import ic

def transpose(l):
    return list(zip(*l))

def p1(inp):
    inp, ins = inp.split('\n\n')
    inp = inp.splitlines()[:-1]
    ins = [[int(l.split(" ")[i]) for i in [1, 3, 5]] for l in ins.splitlines()]

    arr = []
    import re
    for l in inp:
        l = l.ljust(len(inp[-1]))
        t = re.findall(r'(    )|(?:\[(\w)\])', l)
        t = [p[1] for p in t]
        arr.append(t)
    tr = transpose(arr)
    cr = [list(filter(lambda x: x!='', l)) for l in tr]

    for l in ins:
        n, s, d = l
        cr[d-1] = cr[s-1][:n][::-1] + cr[d-1]
        cr[s-1] = cr[s-1][n:]
        ic(cr)

    return ''.join([l[0] for l in cr])

def p2(inp):
    inp, ins = inp.split('\n\n')
    inp = inp.splitlines()[:-1]
    ins = [[int(l.split(" ")[i]) for i in [1, 3, 5]] for l in ins.splitlines()]

    arr = []
    import re
    for l in inp:
        l = l.ljust(len(inp[-1]))
        t = re.findall(r'(    )|(?:\[(\w)\])', l)
        t = [p[1] for p in t]
        arr.append(t)
    tr = transpose(arr)
    cr = [list(filter(lambda x: x!='', l)) for l in tr]

    for l in ins:
        n, s, d = l
        cr[d-1] = cr[s-1][:n] + cr[d-1]
        cr[s-1] = cr[s-1][n:]
        ic(cr)

    return ''.join([l[0] for l in cr])

if __name__ == "__main__":
    import sys
    # don't forget the dot!
    inp = sys.stdin.read().rstrip()[1:]

    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
