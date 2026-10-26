# Lab: Understanding Mock Objects

Six worksheet exercises, practiced by changing and rerunning each example.
The saved files contain the final passing versions:

- `test_mock_basics.py`: an arbitrary method call returns another Mock.
- `test_return_value.py`: a fixed integer return value.
- `test_side_effect_exception.py`: the configured RuntimeError is expected with pytest.raises.
- `test_side_effect_list.py`: final comparison using return_value to return the whole list.
- `test_side_effect_function.py`: final comparison using a fixed return value for different inputs.
- `test_comparison.py`: a function-based side_effect converts input to uppercase.

Earlier experiments deliberately produced assertion failures, StopIteration, and
an unhandled RuntimeError. These were learning checkpoints; the final versions
are expected to pass. The written answers are in the separate completed worksheet PDF.

Run from this folder:

```bash
../.venv/bin/python -m pytest -v -s
```

Expected result: **6 passed**. Run this folder separately from exercises_lab6
because both contain a file named test_mock_basics.py.
