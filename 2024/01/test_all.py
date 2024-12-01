from main import solve


def file_test(fn, expected, part2=False):
    with open(fn) as f:
        inp = f.read().strip()
    res = solve(inp, part2)

    assert expected == res


def test_t1():
    file_test("test.txt", 11)


def test_t2():
    file_test("test.txt", 31, True)


def test_p1():
    file_test("input.txt", 2904518)


def test_p2():
    file_test("input.txt", 18650129, True)
