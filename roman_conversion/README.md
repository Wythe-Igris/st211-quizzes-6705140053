# Roman conversion

Existing Roman numeral exercise, copied from the local `week1_roman` work.
`convert(number)` accepts standard uppercase Roman numerals from 1 to 3999
and raises ValueError for invalid input, including lowercase and whitespace.
This preserves the original solution contract; it is not a new course requirement.

Run from this folder:

```bash
python -m pytest
```

Tests cover symbols, repetition, addition, subtraction, boundaries, invalid
order/format, and non-string inputs. Presentation materials are not included.
