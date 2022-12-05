#!/bin/env python3
from icecream import ic

def transpose(l):
    return list(zip(*l))

def solve(inp, part2=False):
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
        if not part2:
            cr[d-1] = cr[s-1][:n][::-1] + cr[d-1]
        else:
            cr[d-1] = cr[s-1][:n] + cr[d-1]
        cr[s-1] = cr[s-1][n:]

    return ''.join([l[0] for l in cr])

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().rstrip()

    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
