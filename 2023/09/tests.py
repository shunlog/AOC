#!/usr/bin/env python3
from main import extrapolate

def test_extrapolate():
    assert extrapolate([0, 0, 0, 0]) == 0
    assert extrapolate([0, 3, 6, 9, 12, 15]) == 18
    assert extrapolate([1, 3, 6, 10, 15, 21]) == 28
    assert extrapolate([10, 13, 16, 21, 30, 45]) == 68
