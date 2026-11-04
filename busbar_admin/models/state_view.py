from enum import StrEnum


class StateView(StrEnum):
    APPLIED = "applied"
    CONDITION_CONFLICT = "condition_conflict"
    INTENT = "intent"
    LANDED_UNKNOWN = "landed_unknown"
    SETTLED = "settled"
    VERDICT_LANDED = "verdict_landed"
    VERDICT_NOT_LANDED = "verdict_not_landed"

    def __str__(self) -> str:
        return str(self.value)
