#!/bin/env python3
from icecream import ic
import re

class Board:
    def __init__(self, board):
        self.board = {}
        for y,l in enumerate(board.split('\n'), 1):
            for x,ch in enumerate(l, 1):
                if ch != ' ':
                    self.board[x,y] = ch

        x = min(x for x,y in [k for k in self.board.keys() if k[1] == 1])
        y = 1
        self.p = x,y
        # Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
        self.d = 0

    def __str__(self):
        w, h = [max(l) for l in zip(*self.board.keys())]
        s = ''
        for y in range(1, h+1):
            for x in range(1, w+1):
                if (x,y) == self.p:
                    ch = 'o'
                else:
                    ch = self.board.get((x,y), ' ')
                s += ch
            s += '\n'
        return s

    def __repr__(self):
        return self.__str__()

    def __wrap1__(self):
        if self.d == 0:
            return min(x for x,y in [k for k in self.board.keys() if k[1] == self.p[1]]), self.p[1]
        elif self.d == 1:
            return self.p[0], min(y for x,y in [k for k in self.board.keys() if k[0] == self.p[0]])
        elif self.d == 2:
            return max(x for x,y in [k for k in self.board.keys() if k[1] == self.p[1]]), self.p[1]
        elif self.d == 3:
            return self.p[0], max(y for x,y in [k for k in self.board.keys() if k[0] == self.p[0]])

    def __wrap2__(self):
        # TODO wrap around the cube
        return self.p

    def move(self, steps, part2=False):
        for _ in range(steps):
            dp = [(1, 0), (0, 1), (-1, 0), (0, -1)][self.d]
            np = self.p[0] + dp[0], self.p[1] + dp[1]
            if not self.board.get(np):
                if part2:
                    np = self.__wrap2__()
                else:
                    np = self.__wrap1__()
            if self.board[np] == '#':
                break
            elif self.board[np] == '.':
                self.p = np

    def rotate(self, d):
        if d == 'L':
            self.d = (self.d - 1) % 4
        elif d == 'R':
            self.d = (self.d + 1) % 4

def solve(inp, part2=False):
    b, insl = inp.split('\n\n')

    brd = Board(b)

    for ins in re.split(r'(\D+)', insl):
        if ins in ['L', 'R']:
            brd.rotate(ins)
        else:
            brd.move(int(ins), part2)
        ic(ins, brd.d, brd)

    return 1000 * brd.p[1] + 4 * brd.p[0] + brd.d

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().rstrip()
    if not '--debug' in sys.argv:
        ic.disable()
    if '2' not in sys.argv:
        print(solve(inp))
    if '1' not in sys.argv:
        print(solve(inp, True))
