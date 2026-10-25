# Lab 05: Parameterized testing


- `mathutils.py`, `test_param.py`, `test_factorial.py`: even/odd inputs and factorial input/expected-result pairs.
- `test_multi.py`: stacked decorators produce all 3 × 2 = 6 combinations.
- `discount.py`, `test_discount.py`: five discount scenarios.
- `test_default_ids.py`: default IDs for dictionary parameters.
- `test_param_ids.py`: readable IDs using `pytest.param`.
- `test_param_marks.py`: per-case expected failure. The lecture deliberately expects 20 for 5 squared, whose actual result is 25.
- `test_param_fixture.py`: parameterized fixture with three database names (lecture p. 30).
- `test_browsers.py`: two tests across three browser names, with setup and teardown (p. 33). This demonstrates fixtures using strings; it does not launch real browsers.
- `test_cases.json`: four uppercase input/expected pairs for the external-data example (p. 38).
- `test_data_driven.py`: loads the JSON cases at collection time and parameterizes the uppercase test (p. 39). Run from this folder so the relative JSON path resolves.
- `logins.csv`: four login-data cases, including missing passwords and usernames (p. 40).
- `validate.py`, `test_csv_driven.py`: check for nonempty username/password values using CSV cases loaded with `csv.DictReader` (p. 41). Run from this folder so the relative CSV path resolves.

From this folder, with pytest installed:

```bash
python -m pytest -v -s
```

Expected result: **51 passed, 1 xfailed**. The expected failure is the lecture demonstration, not an unfinished exercise.
