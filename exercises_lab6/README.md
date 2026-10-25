# Lab 06: Mocking

- `weather.py`: generates a temperature and classifies it as Freezing, Cold, Pleasant, or Hot.
- `test_problem.py`: uses `unittest.mock.patch` to control temperatures in two tests.
- `test_weather.py`: uses pytest's `monkeypatch` to check the random range and eight temperature boundary cases.

From this folder, with pytest installed:

```bash
python -m pytest -v
```

Expected result: **11 passed**. The tests replace randomness with controlled values.


