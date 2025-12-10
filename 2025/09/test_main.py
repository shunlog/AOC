from main import solve
from icecream import ic


def read_file(fn: str):
    with open(fn) as f:
        return f.read()


def test_ex1_p1():
    ic.enable()
    inp = read_file("example1.txt")
    assert solve(inp) == 50


def test_ex1_p2():
    inp = read_file("example1.txt")
    assert solve(inp, True) == 24


def test_input_p1():
    inp = read_file("input.txt")
    assert solve(inp) == 0


def test_input_p2():
    inp = read_file("input.txt")
    assert solve(inp, True) == 0
