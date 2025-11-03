import regex
from validator_regex.strategies.ValidationStrategy import ValidationStrategy

class TimeValidation(ValidationStrategy):
    pattern = regex.compile(
        r"^(?:[01]\d|2[0-3]):[0-5]\d(:[0-5]\d)?$"
    )

    def validate(self, text: str) -> bool:
        return bool(self.pattern.match(text))