#!/bin/env python3
import math
import re
from icecream import ic

class Monkey:
    def __init__(self, items, newf, test, monkeys):
        self.id = len(monkeys)
        self.items = items
        self.newf = newf
        self.test = test
        self.monkeys = monkeys
        self.inspcnt = 0

    def turn(self):
        for it in self.items:
            it = self.inspect(it)
            it = it // 3
            self.throw(it)
        self.items = []

    def catch(self, it):
        self.items.append(it)

    def throw(self, it):
        to = self.test(it)
        if self.monkeys[to] == self:
            raise Exception (to)
        self.monkeys[to].catch(it)

    def inspect(self, item):
        self.inspcnt += 1
        return self.newf(item)

def ints(s):
    return list(map(int, re.findall(r'\d+', s)))

def p1(inp):
    monkeys = []
    for p in inp.split('\n\n'):
        ls = p.splitlines()
        items = ints(ls[1])
        newf = lambda old,ls=ls: eval(' '.join(ls[2].split()[-3:]))

        div = ints(ls[3])[0]
        mt = ints(ls[4])[0]
        mf = ints(ls[5])[0]
        test = lambda it,mt=mt,mf=mf,div=div: mt if (it % div == 0) else mf
        m = Monkey(items, newf, test, monkeys)
        monkeys.append(m)

    for r in range(20):
        for m in monkeys:
            m.turn()
    l = [m.inspcnt for m in monkeys]
    return math.prod(sorted(l)[-2:])

def p2(inp):
    return 0

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
