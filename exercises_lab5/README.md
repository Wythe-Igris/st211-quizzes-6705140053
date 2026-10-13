# Lab 05: Parameterized testing


- `mathutils.py`, `test_param.py`, `test_factorial.py`: even/odd inputs and factorial input/expected-result pairs.
- `test_multi.py`: stacked decorators produce all 3 × 2 = 6 combinations.
- `discount.py`, `test_discount.py`: five discount scenarios.
- `test_default_ids.py`: default IDs for dictionary parameters.
- `test_param_ids.py`: readable IDs using `pytest.param`.
- `test_param_marks.py`: per-case expected failure. The lecture deliberately expects 20 for 5 squared, whose actual result is 25.

From this folder, with pytest installed:

```bash
python -m pytest -v -s
```

Expected result: **34 passed, 1 xfailed**. The expected failure is the lecture demonstration, not an unfinished exercise.
