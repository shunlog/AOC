#!/bin/env python3
from icecream import ic
import copy

class Node:
    p = None
    n = None

    def __init__(self, v):
        self.v = v

    def __str__(self):
        return f"<-[{self.v}]->"

class DLL:
    sn = None

    def __init__(self, v=None):
        if type(v) == list:
            for i in v:
                self.append(i)
        elif type(v) == int:
            self.append(v)

    def append(self, v: int):
        if not self.sn:
            self.sn = Node(v)
            self.sn.n = self.sn
            self.sn.p = self.sn
        else:
            n = Node(v)
            n.p = self.sn.p
            n.n = self.sn
            self.sn.p.n = n
            self.sn.p = n

    def find(self, v):
        n = self.sn
        while True:
            if n.v == v:
                return n
            n = n.n
            if n == self.sn:
                break
        return None

    def insert_after(self, n1, v2):
        n2 = Node(v2)
        n2.n = n1.n
        n2.p = n1
        n1.n.p = n2
        n1.n = n2

    def move_after(self, na, n):
        if na == n:
            return
        n.p.n = n.n
        n.n.p = n.p
        n.n = na.n
        n.p = na
        na.n.p = n
        na.n = n

    def to_list(self):
        l = []
        n = self.sn
        while True:
            l.append(n.v)
            n = n.n
            if n == self.sn:
                break
        return l

    def __str__(self):
        s = ""
        n = self.sn
        while True:
            s += str(n)
            n = n.n
            if n == self.sn:
                break
        return s

    def __repr__(self):
        return self.__str__()

def mix(li, cnt=1):
    dll = DLL(li)

    for _ in range(cnt):
        ic(_)
        for i, v in li:
            n = dll.find((i, v))

            n2 = n
            if v > 0:
                for _ in range(v % (len(li) - 1)):
                    n2 = n2.n
                    if n2 == n:
                        n2 = n2.n
            else:
                for _ in range((-v + 1) % (len(li) - 1)):
                    n2 = n2.p
                    if n2 == n:
                        n2 = n2.p

            dll.move_after(n2, n)

    li = dll.to_list()

    return li

def p1(inp):
    l = [int(n) for n in inp.splitlines()]
    li = list(zip(range(len(l)), l))

    li = mix(li)

    zi = li.index((l.index(0), 0))
    a = [li[(zi + off) % len(l)][1] for off in [1000, 2000, 3000]]

    return sum(a)

def p2(inp):
    key = 811589153
    l = [int(n) * key for n in inp.splitlines()]
    li = list(zip(range(len(l)), l))

    li = mix(li, 10)

    zi = li.index((l.index(0), 0))
    a = [li[(zi + off) % len(l)][1] for off in [1000, 2000, 3000]]

    return sum(a)


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
