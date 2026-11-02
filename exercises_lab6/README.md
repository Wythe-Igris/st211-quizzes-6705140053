# Lab 06: Mocking and Test Doubles

Practice with mocking, dependency injection, return values, patching, and call verification.

| File | Purpose |
|---|---|
| `weather.py` | Random temperature and weather classification |
| `test_problem.py` | Deliberately weak test: only checks the allowed description words |
| `test_solution_preview.py` | Controls temperatures with `patch` for precise hot/freezing checks |
| `test_mock_basics.py` | Configured return values, arbitrary calls, and stored attributes |
| `payment.py` | PaymentGateway and OrderProcessor with an injected dependency and amount validation |
| `test_payment.py` | Inject a mock payment gateway |
| `test_user_service.py` | `return_value` example |
| `test_return_values.py` | Sequence of return values with `side_effect` |
| `notifications.py` | Email notification example for patching |
| `test_notifications.py` | Patch the email function |
| `date_utils.py` | Report name using the year |
| `test_date_utils.py` | Patch decorator example |
| `test_weather_decorator.py` | Weather patch decorator examples |
| `test_verify_calls.py` | Verify mock calls |
| `test_weather.py` | Additional existing monkeypatch checks for the random range and eight temperature cases |

`test_problem.py` shows a weak test. `test_solution_preview.py` uses mocking to test specific temperatures.

From this folder, using the existing repository environment:

```bash
../.venv/bin/python -m pytest -v
```

To compare the weak test with controlled tests, run:

```bash
../.venv/bin/python -m pytest test_problem.py -v
../.venv/bin/python -m pytest test_solution_preview.py -v
```

Expected: one weak test passes; two controlled tests pass.
