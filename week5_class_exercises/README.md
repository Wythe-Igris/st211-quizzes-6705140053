# Week 5 Class Exercises

These exercises continue Lab 03: Assertions and Test Organization, covering steps 3–5.

- `test_markers.py`: label tests with smoke, slow, and regression markers.
- `test_skips.py`: skip tests unconditionally or based on the Python version.
- `test_xfail.py`: demonstrate expected failures and unexpected passes.
- `test_conditional.py`: skip a test when `/etc/hosts` is missing.
- `pytest.ini`: configure test discovery, output, and registered markers.
- `test_strict.py`: demonstrate an error caused by an unregistered marker.

Run from this folder:

```bash
pytest --ignore=test_strict.py
```

Run `pytest test_strict.py` separately to see the intentional marker error.
