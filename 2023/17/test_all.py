#!/usr/bin/env python3
from main import solve
import pytest
from icecream import ic

@pytest.mark.parametrize("fn", [
    ("test1"), ("test2"), ("input")
])
class TestSolutgion:
    def test_part1(self, fn):
        ic.disable()
        with open(f"{fn}.in") as f:
            inp = f.read().strip()
        with open(f"{fn}.1.out") as f:
            out1 = int(f.read().strip())

        assert solve(inp) == out1

    def test_part2(self, fn):
        ic.disable()
        with open(f"{fn}.in") as f:
            inp = f.read().strip()
        with open(f"{fn}.2.out") as f:
            out2 = int(f.read().strip())

        assert solve(inp, True) == out2

