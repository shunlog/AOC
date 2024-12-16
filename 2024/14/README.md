This is a very cool problem, and something you would only find in AOC.
You are not even told what the tree will look like, so you can either guess that there will be adjacent robots in a line,
or you can do more clever methods like standard deviation,
or you can simply brute-force it with our eyes.

Interestingly, for part 2 I couldn't use any of the code from part 1.
I even had to write it in a separate file, so that I could get input from the keyboard.

The ways to solves this were:
1. Look through each possible solution (consider losing your mind after 1k images, when the answer is at ~8k)
2. Only look at images in which there are N adjacent robots (i looked for lines of 5 vertically, and found the solution quite quickly)
3. Simulate until no robots are overlapping (a big gamble imo)
3. Compute the standard deviation
4. (a clever implementation of 2) Generate all the solutions into a txt file and Ctrl+F for an increasing number of XXXXX


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
