#!/usr/bin/env python3
import sys
from icecream import ic
from collections import defaultdict
import functools


def solve1(graph):
    parents = defaultdict(lambda: list())
    for src, dests in graph.items():
        for dest in dests:
            parents[dest].append(src)

    @functools.lru_cache
    def paths(s: str, start: str) -> int:
        if s == start:
            return 1
        return sum(paths(parent, start) for parent in parents[s])

    return paths("out", "you")


def solve2(graph):
    import copy
    from frozendict import frozendict

    parents = defaultdict(lambda: list())
    for src, dests in graph.items():
        for dest in dests:
            parents[dest].append(src)
    parents["svr"] = []
    parents = {k: tuple(ls) for k, ls in parents.items()}

    def remove_node(graph, node: str):
        new = copy.deepcopy(graph)
        del new[node]
        new = {k: tuple(el for el in ls if el != node)
               for k, ls in new.items()}
        return new

    parents_without_dac = frozendict(remove_node(parents, "dac"))
    parents_without_fft = frozendict(remove_node(parents, "fft"))
    parents = frozendict(parents)

    ic(parents_without_dac)

    @functools.lru_cache
    def paths(node: str, start: str, parents) -> int:
        if node == start:
            return 1
        return sum(paths(parent, start, parents) for parent in parents[node])

    paths_fft_dac = (ic(paths("fft", "svr", parents_without_dac))
                     * paths("dac", "fft", parents)
                     * paths("out", "dac", parents_without_fft))
    paths_dac_fft = (paths("dac", "svr", parents_without_fft)
                     * paths("fft", "dac", parents)
                     * paths("out", "fft", parents_without_dac))
    return ic(paths_fft_dac) + ic(paths_dac_fft)


def solve(inp, part2=False, debug=False):
    if debug:
        ic.enable()
    else:
        ic.disable()

    graph: dict[str, list[str]] = {}
    for l in inp.strip().split('\n'):
        parts = l.split()
        src, dests = parts[0][:-1], parts[1:]
        graph[src] = dests

    if part2:
        return solve2(graph)
    return solve1(graph)


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

    debug = '-v' in sys.argv

    if '-2' not in sys.argv:
        print(solve(inp, False, debug))
    if '-1' not in sys.argv:
        print(solve(inp, True, debug))
