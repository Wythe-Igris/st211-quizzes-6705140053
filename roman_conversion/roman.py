"""Convert standard uppercase Roman numerals from 1 to 3999."""

import re


def convert(number: str) -> int:
    """Return the integer value; reject invalid input with ValueError."""
    if not isinstance(number, str) or not number:
        raise ValueError("Expected a Roman numeral string from I to MMMCMXCIX")

    # Thousands, hundreds, tens, then ones, in standard Roman notation.
    pattern = r"M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})"
    if re.fullmatch(pattern, number) is None:
        raise ValueError("Expected a Roman numeral string from I to MMMCMXCIX")

    values = {"I": 1, "V": 5, "X": 10, "L": 50,
              "C": 100, "D": 500, "M": 1000}
    total = 0

    for index in range(len(number)):
        current = values[number[index]]
        # Subtract when the next symbol is larger; otherwise add.
        if index + 1 < len(number) and current < values[number[index + 1]]:
            total -= current
        else:
            total += current

    return total
