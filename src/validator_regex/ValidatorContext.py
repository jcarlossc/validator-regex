from strategies.ValidationStrategy import ValidationStrategy

class ValidatorContext:
    def __init__(self, strategy: ValidationStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: ValidationStrategy) -> None:
        self._strategy = strategy

    def validate(self, text: str) -> bool:
        return self._strategy.validate(text)

