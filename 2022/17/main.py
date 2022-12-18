#!/bin/env python3
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
    for y, l in enumerate(bl.split('\n')[::-1]):
        for x, ch in enumerate(l):
            if ch == "#":
                b[(x,y)] = True
    blocks.append(b)
ic(blocks)

def move(dx, dy, b):
    '''
    Return false if movement didn't take place
    '''
    global board
    newb = {(xy[0] + dx, xy[1] + dy): True for xy,v in b.items()}
    for xy in b.keys():
        if board.get(xy) or xy[1] < 0 or xy[0] < 0 or xy[0] > 6:
            return False
    return newb

def move_left(b):
    newb = move(-1, 0, b)
    if not newb:
        newb = b
    return b

def move_right(b):
    newb = move(1, 0, b)
    if not newb:
        newb = b
    return b

def fall(b):
    '''
    Return False if the block doesn't fall further
    '''
    return move(0, -1, b)

def spawn(bi):
    global board
    global h
    x = 2
    y = h + 3
    return {(xy[0][0] + x, xy[0][1] + y): True for xy in blocks[bi].items()}

def add_block(block):
    global board
    global h
    board.update(block)
    bh = max(v[1] for v in block.keys())
    h = max(h, bh)

def show(block):
    global board
    global h
    for y in range(h+3-1, -1, -1):
        for x in range(7):
            ch = '#' if board.get((x,y)) or block.get((x,y)) else ' '
            print(ch, end='')
        print()

board = {}
h = 0

def p1(inp):
    bi = 0
    block = spawn(bi)
    for dir in inp:
        if dir == '<':
            block = move_left(block)
        else:
            block = move_right(block)

        nblock = fall(block)
        if not nblock:
            add_block(block)
            bi = (bi + 1) % 5
            block = spawn(bi)
        else:
            block = nblock
        ic(block)
        print("Moved",dir)
        show(block)

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
