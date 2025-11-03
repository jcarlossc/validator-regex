import pytest
from validator_regex.RegexValidator import RegexValidator

def test_cpfvalidation_valid():
    assert RegexValidator.is_cpf("123.123.123-44")

def test_cpfvalidation_invalid():
    assert not RegexValidator.is_cpf("12345678912")