# Automated Software Testing — 192-211

**Student:** Theikdi Nyan  
**Student ID:** 6705140053  
**University:** Siam University  
**Semester:** 1/2026

## About this repository

This repository contains my classroom exercises and Roman numeral assignment for Automated Software Testing. I use Python and pytest to practice writing test cases, understand failure output, and organize tests as the course progresses.

## Exercises

The `exercises_lab1`–`exercises_lab6` folders follow Lab 01–06. Each folder corresponds to a lab; one lab may span more than one classroom session.

| Folder | Lab / exercise | What it covers |
|---|---|---|
| [exercises_lab1](exercises_lab1/) | Lab 01: Testing fundamentals | Basic assertions, calculator tests, Arrange–Act–Assert (AAA), print output, and checking exceptions and error messages |
| [exercises_lab2](exercises_lab2/) | Lab 02: Effective test cases | Bank-account tests, shared state versus independent tests, descriptive names, grade boundaries, and positive/negative email and age validation |
| [exercises_lab3](exercises_lab3/) | Lab 03: Assertions and organization | Collection and floating-point assertions, shopping-cart test classes, custom markers, skipping, expected failures, and `pytest.ini` |
| [exercises_lab4](exercises_lab4/) | Lab 04: Fixtures | A fresh bank-account fixture for deposit and withdrawal tests |
| [exercises_lab5](exercises_lab5/) | Lab 05: Parameterized testing | Input lists, tuples, stacked parameters, IDs, per-case xfail, parameterized fixtures, and JSON/CSV test data |
| [exercises_lab6](exercises_lab6/) | Lab 06: Mocking | Mock basics, payment dependency injection, return values, patching, decorators, and call verification |
| [Lab_Mock_Objects](Lab_Mock_Objects/) | Mock objects worksheet | Six exercises covering basic mocks, return_value, and side_effect with exceptions, lists, and functions |
| [roman_conversion](roman_conversion/) | Roman numeral assignment | Uppercase Roman numerals from 1–3999, with tests for conversion rules, boundaries, and invalid inputs |

Each folder has a short README with its purpose and run instructions.

## Setup

You need Python 3 and pytest. From the repository root, create and activate a virtual environment:

```bash
python3 -m venv .venv
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Then install pytest in the activated environment:

```bash
python -m pip install pytest
```

If you already have an environment with pytest installed, activate that environment instead.

## Running the exercises

Run each group from inside its folder so its local imports and configuration are used. The commands below start from the repository root and return there after each group.

```bash
# Lab 1: basic tests, calculator, AAA, and print output
cd exercises_lab1
python -m pytest --ignore=test_raise_error.py
cd ..

# Lab 2: effective test cases
cd exercises_lab2
python -m pytest
cd ..

# Lab 3: assertions, organization, and configuration
cd exercises_lab3
python -m pytest --ignore=test_strict.py
cd ..

# Lab 4: fixtures
cd exercises_lab4
python -m pytest
cd ..

# Lab 5: selected parameterization exercises
cd exercises_lab5
python -m pytest -v -s
cd ..

# Lab 6: mocking
cd exercises_lab6
python -m pytest -v
cd ..

# Mock objects worksheet (run separately from Lab 6)
cd Lab_Mock_Objects
python -m pytest -v -s
cd ..

# Roman numeral conversion
cd roman_conversion
python -m pytest
cd ..
```

### Intentional failures and special results

Some examples are designed to show how pytest reports problems.

- **Lab 1 — error-message mismatch:** Run `python -m pytest test_raise_error.py` inside `exercises_lab1`. One test passes and one deliberately fails because the expected error message differs from the actual message.
- **Lab 2 — dependent tests:** `test_dependent.py` shares one account between tests. The withdrawal test depends on the deposit test running first. `test_independent.py` shows the version with a fresh account in each test.
- **Lab 3 — strict markers:** Run `python -m pytest test_strict.py` inside `exercises_lab3`. Collection deliberately stops with an error because the test uses an unregistered marker.
- **Lab 3 — skip and xfail:** The examples include a skipped test, an expected failure (`XFAIL`), and a test that passes despite being marked as expected to fail (`XPASS`). Conditional skips depend on the Python version and whether `/etc/hosts` exists.

## What I practiced

- Separating test setup, the action, and the assertion using AAA.
- Choosing boundary values and invalid inputs instead of checking only typical cases.
- Checking exceptions and reading failure messages to understand what went wrong.
- Comparing shared-state tests with independent tests and fixture-based setup.
- Grouping tests with classes and markers, and controlling test runs with pytest configuration.

