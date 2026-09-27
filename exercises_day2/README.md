# Exercises day 2: Effective test cases

Bank-account AAA, an everything-at-once example, dependent/independent tests, descriptive test names, grade boundaries, and positive/negative validation.

Run from this folder:

```bash
python -m pytest
```

`test_dependent.py` deliberately shares an account. Its withdrawal test relies on the deposit test running first; this is the bad example being demonstrated.
