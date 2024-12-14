# Advent of Code solution

This is a solution for an AOC problem.

The program `main.py` takes the puzzle input from `stdin`.
The `-d` flag turns on debugging.
Passing the argument `1` or `2` only runs the specified part.

For testing, `pytest` is used.

# Instructions

Make sure to put the test inputs in the respective files:

- `input.txt` for the main input
- `test1.txt` for the first example
- `test2.txt` for the second example, etc.

If there are more than one example tests,
make sure to add the respective test cases in `test_main.py`.

For example, to run the solution on the input only for part 1:
```sh
./main.py -d  1 < input.txt
```

To run the test cases only for the example 1, part 1:
```sh
pytest -k 'test1 and part1`
```

To run all tests:
```sh
pytest
```
