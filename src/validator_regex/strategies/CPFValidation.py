import regex
from validator_regex.strategies.ValidationStrategy import ValidationStrategy

class CPFValidation(ValidationStrategy):
    pattern = regex.compile(
        r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    )

    def validate(self, text: str) -> bool:
        return bool(self.pattern.match(text))