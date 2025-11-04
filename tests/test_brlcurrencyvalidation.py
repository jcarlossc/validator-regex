import pytest
from validator_regex.RegexValidator import RegexValidator


def test_brlcurrencyvalidation_valid():
    assert RegexValidator.is_brl("R$ 1.564,23")
    assert RegexValidator.is_brl("R$123,45")


def test_brlcurrencyvalidation_invalid():
    assert not RegexValidator.is_brl("1.564,23")
    assert not RegexValidator.is_brl("R$ 123.45")
