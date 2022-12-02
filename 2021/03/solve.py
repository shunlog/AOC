#!/usr/bin/env python3
from icecream import ic
def format_input(inp):
    inp = inp.splitlines()
    return inp

def solve(inp, part2=False):
    inp = format_input(inp)
    tr = list(zip(*inp))
    ic(tr)
    from collections import Counter
    cl = ic([Counter(l) for l in tr])
    mc = ic([c.most_common(1)[0][0] for c in cl])
    g = ic(''.join(mc))
    e = ic(g.translate(g.maketrans({'1': '0', '0': '1'})))
    gn = int(g, 2)
    en = int(e, 2)
    return gn * en
