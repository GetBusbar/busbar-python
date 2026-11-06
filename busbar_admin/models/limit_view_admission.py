from enum import StrEnum


class LimitViewAdmission(StrEnum):
    ESTIMATE = "estimate"
    EXACT = "exact"

    def __str__(self) -> str:
        return str(self.value)
