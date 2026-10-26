# Lab 06: Mocking and Test Doubles

Lecture exercises covered through page 24 (`payment.py`).

| File | Purpose | Lecture page |
|---|---|---|
| `weather.py` | Random temperature and weather classification | 12 |
| `test_problem.py` | Deliberately weak test: only checks the allowed description words | 13 |
| `test_solution_preview.py` | Controls temperatures with `patch` for precise hot/freezing checks | 15–16 |
| `test_mock_basics.py` | Configured return values, arbitrary calls, and stored attributes | 19–23 |
| `payment.py` | PaymentGateway and OrderProcessor with an injected dependency and amount validation | 24 |
| `test_weather.py` | Additional existing monkeypatch checks for the random range and eight temperature cases | Earlier practice |

The two patch tests previously in `test_problem.py` are preserved in
`test_solution_preview.py`, matching the lecture filenames. The weak test is
intentionally kept for comparison: passing it does not prove the weather boundaries.

From this folder, using the existing repository environment:

```bash
../.venv/bin/python -m pytest -v
```

Expected result: **15 passed**. The payment test on page 27 is beyond the current
page-24 stopping point.

For the Step 1 checkpoint (p. 16), run these separately and keep their output:

```bash
../.venv/bin/python -m pytest test_problem.py -v
../.venv/bin/python -m pytest test_solution_preview.py -v
```

Expected: one weak test passes; two controlled tests pass.
