#!/bin/env python3

from icecream import ic

def format_input(inp):
    inp = inp.splitlines()
    return inp

def sol(inp, part2=False):
    tr = list(zip(*inp))
    ic(tr)
    from collections import Counter
    cl = ic([Counter(l) for l in tr])
    mc = ic([c.most_common(1)[0][0] for c in cl])
    g = ic(''.join(mc))
    e = ic(g.translate(g.maketrans({'1': '0', '0': '1'})))
    gn = int(g, 2)
    en = int(e, 2)
    return gn * en

def test(part2=False):
    import glob
    tst = []
    for file in glob.glob("test*.txt"):
        tst.append(file)
    ic(tst)

    inp = open("test.txt", 'r').read()
    inp = ic(format_input(inp))
    exp = 198
    res = sol(inp)
    print("Part 1: ", end='')
    from termcolor import colored
    if exp != res:
        print(colored(res, 'red'))
        print('Expected:', exp)
    else:
        print(colored(res, 'green'), ', just as expected!')

def main(*argv):
    if 'test' in argv[0]:
        print("Using test case input.")
        test()
        return
    ic.disable()
    inp = open("input.txt", 'r').read()
    inp = ic(format_input(inp))
    if '1' in argv[0]:
        print("Part 1:", sol(inp))
    elif '2' in argv[0]:
        print("Part 2:", sol(inp, True))
    else:
        print("Part 1:", sol(inp))
        print("Part 2:", sol(inp, True))

if __name__ == "__main__":
    import sys
    main(sys.argv)

