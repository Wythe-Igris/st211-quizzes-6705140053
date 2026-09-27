# Exercises day 3: Assertions and organization

Collection and float assertions, shopping-cart test classes, markers, skips, expected failures, and pytest configuration. Combines the earlier Week 4 and Week 5 Lab 03 work; validation exercises now live in day 2.

Run from this folder:

```bash
python -m pytest --ignore=test_strict.py
python -m pytest test_strict.py
```

The first command includes intentional SKIPPED, XFAIL, and XPASS results. The second deliberately produces a collection error for an unregistered marker.
