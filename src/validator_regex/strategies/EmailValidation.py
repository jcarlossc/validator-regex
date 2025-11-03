import regex
from strategies.ValidationStrategy import ValidationStrategy

class EmailValidation(ValidationStrategy):
    pattern = regex.compile(
        r"^(?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+"
        r"(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*"
        r"|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21"
        r"\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b"
        r"\x0c\x0e-\x7f])*\")@"
        r"(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*"
        r"[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}"
        r"|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?"
        r"[0-9][0-9]?)\.){3}"
        r"(?:25[0-5]|2[0-4][0-9]|[01]?"
        r"[0-9][0-9]?|[a-zA-Z0-9-]*"
        r"[a-zA-Z0-9]:"
        r"(?:[\x01-\x08\x0b\x0c\x0e-\x1f"
        r"\x21-\x5a\x53-\x7f]"
        r"|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)])$"
    )

    def validate(self, text: str) -> bool:
        return bool(self.pattern.match(text))