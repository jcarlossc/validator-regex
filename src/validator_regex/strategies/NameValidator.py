import regex
from validator_regex.strategies.ValidationStrategy import ValidationStrategy

class NameValidation(ValidationStrategy):
    pattern = regex.compile(
        r"^(?:(?:[A-ZÀ-Ý][a-zà-ÿ]+)(?:['\- ][A-ZÀ-Ýa-zà-ÿ]+)*)$"
    )

    def validate(self, text: str) -> bool:
        return bool(self.pattern.match(text))