from main import solve


def file_test(fn: str, expected: int, part2: bool = False):
    '''
    Assert that solve() is correct on input from file.
    - fn: filename which contains the test case
    - expected: expected result number
    '''
    with open(fn) as f:
        inp = f.read()
    res = solve(inp, part2)
    assert expected == res


def test_ex1_p1():
    file_test("example1.txt", 480)


def test_ex1_p2():
    file_test("example1.txt", 875318608908, True)


def test_input_p1():
    file_test("input.txt", 26599)


def test_input_p2():
    file_test("input.txt", 106228669504887, True)
