from enum import StrEnum


class ConfigInputLimitType6OnExhaust(StrEnum):
    BLOCK = "block"
    DOWNGRADE = "downgrade"

    def __str__(self) -> str:
        return str(self.value)
