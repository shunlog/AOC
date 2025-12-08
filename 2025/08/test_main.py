from main import solve


def read_file(fn: str):
    with open(fn) as f:
        return f.read()

def test_ex1_p2():
    inp = read_file("example1.txt")
    assert solve(inp, True) == 25272


def test_input_p1():
    inp = read_file("input.txt")
    assert solve(inp) == 330786


def test_input_p2():
    inp = read_file("input.txt")
    assert solve(inp, True) == 3276581616
