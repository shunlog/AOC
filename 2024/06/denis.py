#!/bin/env python3

import time
f = open("input.txt", "r")
gmap = {}

y = 0
start = None
for line in f.readlines():
    line = line.strip()
    for x in range(len(line)):
        if line[x] == "^":
            start = (x, y)
        gmap[(x, y)] = line[x]
    y += 1
f.close()


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper


def simulate_cycle(start, gmap):
    moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    state = set()
    state.add((start, 0))
    current_move = 0
    while start in gmap:
        if (start[0] + moves[current_move][0], start[1] + moves[current_move][1]) not in gmap:
            break
        if gmap[(start[0] + moves[current_move][0], start[1] + moves[current_move][1])] == "#":
            current_move += 1
            current_move %= 4
            continue

        start = (start[0] + moves[current_move][0],
                 start[1] + moves[current_move][1])
        if (start, current_move) in state:
            return True
        state.add((start, current_move))

    return False


@measure_time
def count_possible_cycles(start, gmap):
    cycle_count = 0
    for pos, value in gmap.items():
        if value == ".":
            gmap[pos] = "#"
            if simulate_cycle(start, gmap):
                cycle_count += 1
            gmap[pos] = "."
    return cycle_count


cycles = count_possible_cycles(start, gmap)
print(cycles)
