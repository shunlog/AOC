#!/bin/env python3

from icecream import ic

from solve import solve

def run_tests(part2=False):
    import glob
    tst = list(glob.glob("test*"))
    ic(tst)

    # inp = open("test.txt", 'r').read()
    # inp = ic(format_input(inp))
    # exp = 198
    # res = sol(inp)
    # print("Part 1: ", end='')
    # from termcolor import colored
    # if exp != res:
    #     print(colored(res, 'red'))
    #     print('Expected:', exp)
    # else:
    #     print(colored(res, 'green'), ', just as expected!')

def main(*argv):
    if 'test' in argv[0]:
        if '1' in argv[0]:
            run_tests()
        elif '2' in argv[0]:
            run_tests(True)
        return
    ic.disable()
    inp = open("input.txt", 'r').read()
    inp = ic(format_input(inp))
    if '1' in argv[0]:
        print("Part 1:", sol(inp))
    elif '2' in argv[0]:
        print("Part 2:", sol(inp, True))

if __name__ == "__main__":
    import sys
    main(sys.argv)
