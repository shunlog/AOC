Put the inputs in `input.txt` and `example1.txt`
```sh
# solves input.txt
$ ./main.py

# solves example1.txt for part 1, turns on logging
$ ./main.py -v -1 example1.txt

# run the tests
$ pytest

# run the tests for example input, part 2
$ pytest -k "p2 and ex"
```

To test individual functions inside `main.py`:
```python
def test_foo():
    ic.enable()
    assert foo(1) == 2
```
```sh
$ pytest main.py
```