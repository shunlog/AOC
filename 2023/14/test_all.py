#!/usr/bin/env python3
from main import *

def test_roll():
    initial = [list(s) for s in '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
'''.splitlines()]

    final = [list(s) for s in '''OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
'''.splitlines()]

    roll(initial, UP)

    assert final == initial


def test_load():
    m = '''OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
'''.splitlines()

    assert 136 == load(m)


def test_four_rolls():
    m = [list(s) for s in '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
'''.splitlines()]

    expected = [list(s) for s in '''.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....'''.splitlines()]

    roll(m, UP)
    roll(m, LEFT)
    roll(m, DOWN)
    roll(m, RIGHT)

    assert expected == m
