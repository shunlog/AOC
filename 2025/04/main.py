#!/usr/bin/env python3
import sys
from icecream import ic
from collections import defaultdict

ic.disable()

neighbor_deltas = ((-1, -1), (-1, 0), (-1, 1),
                   (0, -1),           (0, 1),
                   (1, -1),  (1, 0),  (1, 1))


def removable_rolls(m: list[list[str]]) -> set[tuple[int, int]]:
    # (row, col) -> num. of neighbors
    nm: dict[tuple[int, int], int] = defaultdict(lambda: 0)
    # set of (row, col) of rolls
    rolls: set[tuple[int, int]] = set()
    for row, line in enumerate(m):
        for col, cell in enumerate(line):
            if cell != '@':
                continue
            rolls.add((row, col))
            for dx, dy in neighbor_deltas:
                nx, ny = row+dx, col+dy
                nm[(nx, ny)] += 1
    return set(coord for coord in rolls if nm[coord] < 4)


def solve1(m: list[list[str]]):
    return len(removable_rolls(m))


def solve2(m: list[list[str]]):
    removed = 0
    while True:
        to_remove = removable_rolls(m)
        if not to_remove:
            break
        removed += len(to_remove)
        for row, col in to_remove:
            m[row][col] = '.'
    return removed


def solve(inp, part2=False):
    m = [list(line) for line in inp.strip().split()]
    if part2:
        return solve2(m)
    return solve1(m)


if __name__ == "__main__":
    '''
    $ ./main.py                    # reads input.txt
    $ ./main.py -v -1 example.txt   # turns on logging, run only part 1
    '''

    last_arg = sys.argv[-1]
    if '.txt' in last_arg:
        fn = last_arg
    else:
        fn = "input.txt"
    with open(fn) as f:
        inp = f.read()

    if '-v' in sys.argv:
        ic.enable()

    if '-2' not in sys.argv:
        print(solve(inp, False))
    if '-1' not in sys.argv:
        print(solve(inp, True))
