from enum import StrEnum


class ConfigInputLimitType6Admission(StrEnum):
    ESTIMATE = "estimate"
    EXACT = "exact"

    def __str__(self) -> str:
        return str(self.value)
