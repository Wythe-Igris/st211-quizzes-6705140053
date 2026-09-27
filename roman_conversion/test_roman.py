import pytest

from roman import convert


def test_single_symbols():
    assert convert("I") == 1
    assert convert("V") == 5
    assert convert("X") == 10
    assert convert("L") == 50
    assert convert("C") == 100
    assert convert("D") == 500
    assert convert("M") == 1000


def test_repeated_symbols():
    assert convert("II") == 2
    assert convert("III") == 3
    assert convert("XX") == 20
    assert convert("CCC") == 300
    assert convert("MMM") == 3000


def test_additive_combinations():
    assert convert("VI") == 6
    assert convert("XVI") == 16
    assert convert("MD") == 1500
    assert convert("MDCLXVI") == 1666


def test_subtractive_pairs():
    assert convert("IV") == 4
    assert convert("IX") == 9
    assert convert("XL") == 40
    assert convert("XC") == 90
    assert convert("CD") == 400
    assert convert("CM") == 900


def test_mixed_addition_and_subtraction():
    # Arrange: choose an input and its independently known answer.
    number = "XIX"
    expected = 19
    # Act: run the function being tested.
    result = convert(number)
    # Assert: compare the actual result with the expected result.
    assert result == expected
    assert convert("MCMXCIV") == 1994
    assert convert("XLIX") == 49


def test_valid_boundaries():
    assert convert("I") == 1
    assert convert("MMMCMXCIX") == 3999


def test_invalid_order_from_slides():
    with pytest.raises(ValueError):
        convert("VX")
    with pytest.raises(ValueError):
        convert("XXC")


def test_invalid_subtraction():
    for number in ["IL", "IC", "XM", "IIV", "IXIX", "IIX", "XDD", "CMCC", "MCMC", "MMMMCMXCIX"]:
        with pytest.raises(ValueError):
            convert(number)


def test_invalid_repetition():
    for number in ["IIII", "VV", "XXXX", "LL", "CCCC", "DD", "MMMM"]:
        with pytest.raises(ValueError):
            convert(number)


def test_empty_unknown_lowercase_and_whitespace():
    for number in ["", "ABC", "123", "iv", " IV", "IV ", "X I"]:
        with pytest.raises(ValueError):
            convert(number)


def test_non_string_input():
    for number in [None, 4, True, ["I"]]:
        with pytest.raises(ValueError):
            convert(number)
