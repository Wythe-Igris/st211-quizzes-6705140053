# Exercises lab 1: Testing fundamentals

Basic assertions, calculator tests, Arrange–Act–Assert, print output, and exception checks.

Run from this folder:

```bash
python -m pytest --ignore=test_raise_error.py
python -m pytest test_raise_error.py
```

The second command deliberately gives one pass and one failure: the expected error message differs from the calculator message.
