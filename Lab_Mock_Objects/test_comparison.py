from unittest.mock import Mock


def fetch(value):
    return value.upper()


def test_comparison():
    mock = Mock()

    mock.fetch.side_effect = fetch

    result = mock.fetch("hello")
    print(result)

    assert result == "HELLO"