from validator_regex.ValidatorContext import ValidatorContext
from validator_regex.strategies.EmailValidation import EmailValidation
from validator_regex.strategies.BRLCurrencyValidation import BRLCurrencyValidation
from validator_regex.strategies.NameValidation import NameValidation
from validator_regex.strategies.CPFValidation import CPFValidation
from validator_regex.strategies.CNPJValidation import CNPJValidation
from validator_regex.strategies.TimeValidation import TimeValidation

class RegexValidator:
    @staticmethod
    def is_email(text: str) -> bool:
        return ValidatorContext(EmailValidation()).validate(text)
    
    @staticmethod
    def is_brl(text: str) -> bool:
        return ValidatorContext(BRLCurrencyValidation()).validate(text)
    
    @staticmethod
    def is_name(text: str) -> bool:
        return ValidatorContext(NameValidation()).validate(text)
    
    @staticmethod
    def is_cpf(text: str) -> bool:
        return ValidatorContext(CPFValidation()).validate(text)
    
    @staticmethod
    def is_cnpj(text: str) -> bool:
        return ValidatorContext(CNPJValidation()).validate(text)
    
    @staticmethod
    def is_time(text: str) -> bool:
        return ValidatorContext(TimeValidation()).validate(text)