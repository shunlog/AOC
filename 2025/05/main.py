#!/usr/bin/env python3
import sys
from icecream import ic
from dataclasses import dataclass

ic.disable()


@dataclass
class Range:
    """An interval, with start and end inclusive,
    where start <= end"""
    start: int
    end: int


def overlap(r1: Range, r2: Range) -> bool:
    not_overlap = r1.end < r2.start or r2.end < r1.start
    return not not_overlap


def test_overlap():
    ic.enable()
    assert overlap(Range(0, 1), Range(1, 2))
    assert overlap(Range(0, 2), Range(1, 3))
    assert overlap(Range(0, 3), Range(1, 2))
    assert overlap(Range(0, 3), Range(-1, 1))
    assert not overlap(Range(0, 3), Range(4, 5))
    assert not overlap(Range(1, 1), Range(0, 0))


def merge(r1: Range, r2: Range) -> Range:
    '''Merge two ranges assuming they overlap'''
    min_start = min(r1.start, r2.start)
    max_end = max(r1.end, r2.end)
    return Range(min_start, max_end)


def solve1(ranges, ingrs):
    return sum(int(any(ing >= r[0] and ing <= r[1]
                       for r in ranges))
               for ing in ingrs)


def merge_all(ranges: list[Range]) -> list[Range]:
    def merge_iter(ranges):
        merged = []
        for r in ranges:
            for i, r2 in enumerate(merged):
                if overlap(r, r2):
                    merged[i] = merge(r, r2)
                    break
            else:
                merged.append(r)
        return merged

    while True:
        merged = merge_iter(ranges)
        if merged == ranges:
            break
        ranges = merged
    return ranges


def solve2(ranges):
    ranges = [Range(start, end) for start, end in ranges]
    merged = merge_all(ranges)
    return sum(r.end - r.start + 1 for r in merged)


def solve(inp, part2=False):
    inp = inp.strip()
    s_ranges, s_ingrs = inp.split('\n\n')
    ranges = [tuple(int(n) for n in l.split('-')) for l in s_ranges.split()]
    ingrs = [int(l) for l in s_ingrs.split()]

    if part2:
        return solve2(ranges)
    return solve1(ranges, ingrs)


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
