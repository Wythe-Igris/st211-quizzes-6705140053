import pytest

import weather


def test_get_temperature_uses_expected_range(monkeypatch):
    calls = []

    def fake_randint(lower, upper):
        calls.append((lower, upper))
        return lower

    monkeypatch.setattr(weather.random, "randint", fake_randint)

    assert weather.get_temperature() == -10
    assert calls == [(-10, 40)]


@pytest.mark.parametrize(
    ("temperature", "expected"),
    [
        (-10, "Freezing"),
        (-1, "Freezing"),
        (0, "Cold"),
        (14, "Cold"),
        (15, "Pleasant"),
        (24, "Pleasant"),
        (25, "Hot"),
        (40, "Hot"),
    ],
)
def test_describe_weather_for_temperature(monkeypatch, temperature, expected):
    monkeypatch.setattr(weather, "get_temperature", lambda: temperature)

    assert weather.describe_weather() == expected
