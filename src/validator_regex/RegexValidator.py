from ValidatorContext import ValidatorContext

from strategies.EmailValidation import EmailValidation

class RegexValidator:
    @staticmethod
    def is_email(text: str) -> bool:
        return ValidatorContext(EmailValidation()).validate(text)