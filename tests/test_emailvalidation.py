import pytest
from validator_regex.RegexValidator import RegexValidator


def test_email_valid():
    assert RegexValidator.is_email("carlos@gmail.com")
    assert RegexValidator.is_email("carlos.costa1977@gmail.com")
    assert RegexValidator.is_email("carlos_costa1977@gmail.com")


def test_email_invalid():
    assert not RegexValidator.is_email("carlose@@gmail.com")
    assert not RegexValidator.is_email("carlos@.com")
    assert not RegexValidator.is_email("carlos.com")
