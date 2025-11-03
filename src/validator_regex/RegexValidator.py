from validator_regex.ValidatorContext import ValidatorContext
from validator_regex.strategies.EmailValidation import EmailValidation

class RegexValidator:
    @staticmethod
    def is_email(text: str) -> bool:
        return ValidatorContext(EmailValidation()).validate(text)