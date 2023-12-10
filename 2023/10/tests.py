#!/usr/bin/env python3
from main import *


def test_next_pipe():
    m = '''.....
.S-7-
.|.|.
.L-J.
...|. '''.splitlines()
    S = (1, 1)

    # test entering pipe
    assert find_next_pipe(m, S) in ((1, 2), (2, 1))
    assert find_next_pipe(m, (1, 2), (1, 1)) == (1, 3)
    assert find_next_pipe(m, (2, 1), (1, 1)) == (3, 1)
    assert find_next_pipe(m, (3, 1), (2, 1)) == (3, 2)

    # test not exiting pipe from wrong end
    assert find_next_pipe(m, (3, 1), (2, 1)) == (3, 2)
    assert find_next_pipe(m, (3, 3), (3, 2)) == (2, 3)
