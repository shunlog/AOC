#!/bin/env python3
import math
import re
from icecream import ic

class Monkey:
    def __init__(self, items, newf, test, calm, monkeys):
        self.id = len(monkeys)
        self.items = items
        self.newf = newf
        self.test = test
        self.calm = calm
        self.monkeys = monkeys
        self.inspcnt = 0

    def turn(self):
        for it in self.items:
            it = self.inspect(it)
            it = self.calm(it)
            # it = it // 3
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

def p2(inp):
    monkeys = []
    divall = 1
    for p in inp.split('\n\n'):
        ls = p.splitlines()
        items = ints(ls[1])
        ins = ' '.join(ls[2].split()[-3:])
        newf = lambda old,ins=ins: eval(ins)

        div = ints(ls[3])[0]
        mt = ints(ls[4])[0]
        mf = ints(ls[5])[0]
        test = lambda it,mt=mt,mf=mf,div=div: mt if (it % div == 0) else mf
        divall *= div
        calm = lambda it: it % divall
        m = Monkey(items, newf, test, calm, monkeys)
        monkeys.append(m)

    for r in range(10000):
        ic(r)
        for m in monkeys:
            m.turn()
    l = [m.inspcnt for m in monkeys]
    ic(l)
    return math.prod(sorted(l)[-2:])

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
