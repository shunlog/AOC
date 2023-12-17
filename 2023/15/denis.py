#!/usr/bin/env python3
from icecream import ic


def hash(string:str):
    current_value = 0
    for char in string:
        current_value = ((current_value + ord(char)) * 17) % 256
    return current_value


def find_lens(lens, lenses):
    for index, l in enumerate(lenses):
        if lens == l[0]:
            return index
    return -1


def update_lens(label, N, boxes):
    box_i = str(hash(label))
    lenses = boxes[box_i]
    res = find_lens(label, lenses)
    if res != -1:
        lenses[res] = (label, N)
    else:
        lenses.append((label, N))


def remove_lens(label, boxes):
    box_i = str(hash(label))
    lenses = boxes[box_i]
    res = find_lens(label, lenses)
    if res != -1:
        del lenses[res]


def execute_instructions(strings):
    boxes = {str(i): [] for i in range(256)}

    for string in strings:
        if "-" in string:
            label = string[:-1]
            remove_lens(label, boxes)
        if "=" in string:
            label, N = string.split("=")
            update_lens(label, N, boxes)

    return boxes


def solve(inp, part2):
    strings = inp.replace("\n", "").split(",")
    boxes = execute_instructions(strings)

    s = 0
    for box in boxes.keys():
        for index, tup in enumerate(boxes[box]):
            s += (int(box) + 1) * (index + 1) * int(tup[1])

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
