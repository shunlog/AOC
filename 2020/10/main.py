#!/bin/env python3

from icecream import ic
from termcolor import colored
from solve import solve

def run_tests(part2=False):
    import glob
    til = list(glob.glob("test*.in"))
    for ti in til:
        tn = ti.split('.')[0]
        to = f'{tn}.{2 if part2 else 1}.out'
        inp = open(ti, 'r').read().strip()
        sol = solve(inp, part2)
        exp = open(to, 'r').read().strip()
        if str(sol) != exp:
            print(colored(f"Wrong on {tn}!", 'red'))
            print(f"Expected {exp}")
            print(f"Got {sol}")
        else:
            print(colored(f"Correct on {tn}!", 'green'))
            print(f"Got {sol}")

def main(*argv):
    if 'test' in argv[0]:
        run_tests('2' in argv[0])
        return
    ic.disable()
    inp = open("input.txt", 'r').read().strip()
    if '1' in argv[0] or '2' not in argv[0]:
        print("Part 1:", solve(inp))
    if '1' not in argv[0] or '2' in argv[0]:
        print("Part 2:", solve(inp, True))

if __name__ == "__main__":
    import sys
    main(sys.argv)
