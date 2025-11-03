import pytest
from validator_regex.RegexValidator import RegexValidator

def test_timevalidation_valid():
    assert RegexValidator.is_time("23:45")
    assert RegexValidator.is_time("00:00")
    assert RegexValidator.is_time("23:00:01")

def test_timevalidation_invalid():
    assert not RegexValidator.is_time("24:00")
    assert not RegexValidator.is_time("23:60")
    assert not RegexValidator.is_time("77:77:77")