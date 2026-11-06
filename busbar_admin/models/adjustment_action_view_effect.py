from enum import StrEnum


class AdjustmentActionViewEffect(StrEnum):
    APPLIED = "applied"
    NOT_APPLIED = "not_applied"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
