import pytest
from validator_regex.RegexValidator import RegexValidator


def test_namevalidation_valid():
    assert RegexValidator.is_name("Carlos da Costa")
    assert RegexValidator.is_name("José Carlos")


def test_namevalidation_invalid():
    assert not RegexValidator.is_name("Carlos123")
    assert not RegexValidator.is_name("carlos")
