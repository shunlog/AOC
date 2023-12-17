#!/bin/env python3
from icecream import ic
from collections import deque


def HASH(s):
    v = 0
    for ch in s:
        v += ord(ch)
        v *= 17
        v %= 256
    return v


boxes = [deque() for _ in range(256)]

def index_func(ls, f):
    for i, v in enumerate(ls):
        if f(v):
            return i, v
    return -1

assert index_func([1, 2, 3], lambda v: v == 2) == (1, 2)

def remove_lens(label):
    global boxes
    bi = HASH(label)

    if -1 != (r := index_func(boxes[bi], lambda v: v[0] == label)):
        i, v = r
        boxes[bi].remove(v)


def update_lens(label, n):
    global boxes
    bi = HASH(label)

    if -1 != (r := index_func(boxes[bi], lambda v: v[0] == label)):
        # found label
        i, v = r
        boxes[bi][i] = (label, n)
    else:
        boxes[bi].append((label, n))


def solve(inp, part2=False):
    assert HASH("HASH") == 52

    if not part2:
        return sum(HASH(s) for s in inp.split(','))


    for step in inp.split(','):
        if (p := step.find('-')) != -1:
            label = step[:p]
            ic(step, label, p)
            remove_lens(label)
        else:
            label, n = step.split('=')
            n = int(n)
            update_lens(label, n)

    s = 0
    for i, d in enumerate(boxes):
        for slot, v in enumerate(d):
            s += (i+1) * (slot+1) * v[1]
    return s


if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
