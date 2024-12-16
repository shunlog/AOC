#!/bin/env python3
import sys
from icecream import ic

import os
import re
from math import prod
import sys
import time

FILE = sys.argv[1]

# # For examples:
# w = 11
# h = 7

w = 101
h = 103


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_step(state, t):
    clear_screen()
    print(f't = {t}')
    print('-'*10)

    posns = set(state.values())
    for y in range(h):
        for x in range(w):

            ch = '*' if (x, y) in posns else ' '
            sys.stdout.write(ch)
        sys.stdout.write('\n')
    sys.stdout.flush()


def detect_pattern(s) -> bool:
    posns = set(s.values())
    height = 5  # looking for a pillar of this height

    for y in range(h):
        for x in range(w):
            pos_to_check = [(x, y+dy) for dy in range(height)]
            if all(p in posns for p in pos_to_check):
                return True
    return False


# pre-process for both parts
with open(FILE) as f:
    inp = f.read()

ls = []
for l in inp.splitlines():
    nums = re.findall(r'-?\d+', l)
    assert len(nums) == 4
    nums_int = [int(n) for n in nums]
    ls.append(nums_int)

# ls now hold a list of tuples of 4 integers

# state at t=0
# state0 = {(0, 4, 3, -3): (0, 4), ...}

# simulate_step(state0) -> state1
# draw_step(state1)


def simulate_step(s, backwards=False):
    for k, v in s.items():
        x, y = v
        sx, sy, vx, vy = k
        if backwards:
            nx = (x - vx) % w
            ny = (y - vy) % h
        else:
            nx = (x + vx) % w
            ny = (y + vy) % h
        s[k] = (nx, ny)


# compute state0
s = {}
for l in ls:
    x, y, vx, vy = l
    s[(x, y, vx, vy)] = (x, y)

t = 0

# initial simulation
for _ in range(7861):
    simulate_step(s)
    t += 1
draw_step(s, t)
key = input('Press enter...')


key = ''
while True:
    if key != '':
        simulate_step(s, True)
        t += -1
    else:
        simulate_step(s)
        t += 1

    if detect_pattern(s):
        draw_step(s, t)

        # time.sleep(0.15)
        key = input('Press enter...')


print(key)
