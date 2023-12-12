#!/usr/bin/env python3
from main import possib
import pytest

@pytest.mark.parametrize(
    "s, nums, expected",
    [
        ("???.###", [1,1,3], 1),
        (".??..??...?##.", [1,1,3], 4),
        ("?#?#?#?#?#?#?#?", [1,3,1,6], 1),
        ("????.#...#...", [4,1,1], 1),
        ("????.######..#####.", [1,6,5], 4),
        ("?###????????", [3,2,1], 10)
    ]
)
def test_possib(s, nums, expected):
    assert possib(s, tuple(nums)) == expected

@pytest.mark.parametrize(
    "s, nums, expected",
    [
        ("???.###", [1,1,3], 1),
        (".??..??...?##.", [1,1,3], 16384),
        ("?#?#?#?#?#?#?#?", [1,3,1,6], 1),
        ("????.#...#...", [4,1,1], 16),
        ("????.######..#####.", [1,6,5], 2500),
        ("?###????????", [3,2,1], 506250)
    ]
)
def test_possib2(s, nums, expected):
    s += "?"
    s = s*5
    s = s[:-1]
    nums = nums*5

    assert possib(s, tuple(nums)) == expected
