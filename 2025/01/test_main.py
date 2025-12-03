from main import solve


def read_file(fn: str):
    with open(fn) as f:
        return f.read()

def test_ex1_p1():
    inp = read_file("example1.txt")
    assert solve(inp) == 3

def test_ex1_p2():
    inp = read_file("example1.txt")
    assert solve(inp, True) == 6


def test_input_p1():
    inp = read_file("input.txt")
    assert solve(inp) == 1139


def test_input_p2():
    inp = read_file("input.txt")
    assert solve(inp, True) == 6684
