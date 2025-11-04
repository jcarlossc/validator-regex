import pytest
from validator_regex.RegexValidator import RegexValidator


def test_cnpjvalidation_valid():
    assert RegexValidator.is_cnpj("12.569.987/0211-95")


def test_cnpjvalidation_invalid():
    assert not RegexValidator.is_cnpj("12345678912345")
    assert not RegexValidator.is_cnpj("12.3456.789.1234")
