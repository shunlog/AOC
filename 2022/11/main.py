#!/bin/env python3
import math
import re
from icecream import ic

def ints(s):
    return [int(i) for i in re.findall(r'\d+', s)]

def parse(inp):
    '''
    Array of dicts: "items", "op", "div", "true", "false", "inspcnt"
    '''
    monkeys = []
    for p in inp.split('\n\n'):
        ls = p.splitlines()
        m = {}
        m['items'] = ints(ls[1])
        ins = ls[2][ls[2].find('=')+2:]
        m['op'] = lambda old,ins=ins: eval(ins)
        m['div'] = ints(ls[3])[0]
        m['true'] = ints(ls[4])[0]
        m['false'] = ints(ls[5])[0]
        m['inspcnt'] = 0
        monkeys.append(m)

    return monkeys

def business(ms, rounds, calm):
    for r in range(rounds):
        for m in ms:
            for it in m['items']:
                it = m['op'](it)
                it = calm(it)
                mi = m['true'] if it % m['div'] == 0 else m['false']
                ms[mi]['items'].append(it)
                m['inspcnt'] += 1
            m['items'] = []
    return ms

def p1(inp):
    ms = parse(inp)

    ms = business(ms, 20, lambda it: it // 3)
    inspls = [m['inspcnt'] for m in ms]
    return math.prod(sorted(inspls)[-2:])

def p2(inp):
    ms = parse(inp)

    divs = [m['div'] for m in ms]
    lcm = math.prod(divs)

    ms = business(ms, 10000, lambda it: it % lcm)
    inspls = [m['inspcnt'] for m in ms]
    return math.prod(sorted(inspls)[-2:])

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
