#!/bin/env python3
from itertools import *
from icecream import ic

blocks_raw = '''####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
'''

blocks = []
for bl in blocks_raw.split('\n\n'):
    b = {}
    for y, l in enumerate(bl.splitlines()[::-1]):
        for x, ch in enumerate(l):
            if ch == "#":
                b[(x,y)] = True
    blocks.append(b)
ic(blocks)

def move(block, dx, dy, board):
    nblock = {(x+dx, y+dy):True for x,y in block.keys()}
    for x,y in nblock.keys():
        if (x,y) in board.keys() or x < 0 or x > 6 or y < 0:
            return block
    return nblock

def spawn(i, board, h):
    global blocks
    b = {(x+2, y+h+3):True for x,y in blocks[i].keys()}
    return b

def freeze_block(b, board, h):
    board.update(b)
    newh = max([y+1 for x,y in b.keys()])
    return board, max(newh, h)

def show(board, block, h):
    newh = max([y+1 for x,y in block.keys()])
    h = max(newh, h)
    for y in range(h, -1, -1):
        for x in range(7):
            ch = '#' if (x,y) in board or (x,y) in block else ' '
            print(ch, end='')
        print()

def p1(inp):
    board = {}
    h = 0

    bi = 0
    block = spawn(bi, board, h)
    cnt = 1
    for dir in cycle(inp):
        if dir == '<':
            block = move(block, -1, 0, board)
        else:
            block = move(block, 1, 0, board)

        prev = block
        block = move(block, 0, -1, board)
        if block == prev:
            board, h = freeze_block(block, board, h)
            bi = (bi + 1) % len(blocks)
            block = spawn(bi, board, h)
            cnt += 1
            ic(cnt)
            if cnt == 2023:
                break

    # show(board, block, h)
    return h

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
