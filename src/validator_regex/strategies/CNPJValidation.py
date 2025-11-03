import regex
from validator_regex.strategies.ValidationStrategy import ValidationStrategy

class CNPJValidation(ValidationStrategy):
    pattern = regex.compile(
        r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$"
    )

    def validate(self, text: str) -> bool:
        return bool(self.pattern.match(text))