import regex
from validator_regex.strategies.ValidationStrategy import ValidationStrategy

class BRLCurrencyValidation(ValidationStrategy):
    pattern = regex.compile(
        r"^R\$\s?\d{1,3}(\.\d{3})*(,\d{2})?$"
    )

    def validate(self, text: str) -> bool:
        return bool(self.pattern.match(text))