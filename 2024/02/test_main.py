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


def test_test1_part1():
    file_test("test1.txt", 2)


def test_test1_part2():
    file_test("test1.txt", 4, True)


def test_input_part1():
    file_test("input.txt", 230)


def test_input_part2():
    file_test("input.txt", 301, True)
