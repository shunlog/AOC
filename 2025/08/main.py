#!/usr/bin/env python3
import sys
from icecream import ic
from dataclasses import dataclass
import math
import itertools
from collections import Counter

ic.disable()

@dataclass(frozen=True)
class Coord3D:
    x: int
    y: int
    z: int

def coord_dist(c1: Coord3D, c2: Coord3D) -> float:
    return math.sqrt((c1.x-c2.x)**2
                     + (c1.y-c2.y)**2
                     + (c1.z-c2.z)**2)


def connect(circuits, c1, c2):
    if not (circuits.get(c1) or circuits.get(c2)):
        # both empty
        circ = {c1, c2}
        circuits[c1] = circ
        circuits[c2] = circ
    elif circuits.get(c1) and circuits.get(c2):
        # both grouped
        if circuits.get(c1) is circuits.get(c2):
            # already in same circuit
            return
        circ1 = circuits[c1]
        circ1 |= circuits[c2]
        for c2_neighbor in circuits[c2]:
            circuits[c2_neighbor] = circ1
    else:
        c_alone = c1 if circuits.get(c2) else c2
        c_conn = c2 if circuits.get(c2) else c1
        circ = circuits[c_conn]
        circ.add(c_alone)
        circuits[c_alone] = circ


def solve1(sorted_dists):
    circuits:dict[Coord3D, set[Coord3D]] = {}
        
    for (c1, c2), _dist in sorted_dists[:1000]:
        connect(circuits, c1, c2)

    unique_circuits = Counter(id(c) for c in circuits.values())

    top3 = [elem[1] for elem in unique_circuits.most_common(3)]
    return math.prod(top3)


def solve2(coords, sorted_dists):
    circuits:dict[Coord3D, set[Coord3D]] = {}
    
    for i, ((c1, c2), _dist) in enumerate(sorted_dists):
        connect(circuits, c1, c2)
        any_conn = next(iter(circuits.values()))
        if any_conn and len(any_conn) == len(coords):
            break
    ic("Stopped after", i, "connections")
    ic(c1, c2)

    return c1.x * c2.x


def solve(inp, part2=False):
    inp = inp.strip()

    coords = [Coord3D(*(int(n) for n in l.split(',')))
              for l in inp.split()]

    dists: dict[tuple, float] = {}
    for combi in itertools.combinations(coords, 2):
        dists[combi] = coord_dist(*combi)
    sorted_dists = sorted(dists.items(), key=lambda x: x[1])
    
    if part2:
        return solve2(coords, sorted_dists)
    else:
        return solve1(sorted_dists)


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

