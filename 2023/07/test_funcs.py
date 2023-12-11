#!/usr/bin/env python3
from main import hand_type

def test_hand_type():
    assert hand_type('AAAAA') == 0
    assert hand_type('AA2AA') == 1
    assert hand_type('23332') == 2
    assert hand_type('TTT98') == 3
    assert hand_type('23432') == 4
    assert hand_type('A23A4') == 5
    assert hand_type('23456') == 6

    assert hand_type('AAAAA', True) == 0
    assert hand_type('T55J5', True) == 1
    assert hand_type('KTJJT', True) == 1
    assert hand_type('QQQJA', True) == 1
