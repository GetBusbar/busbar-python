from enum import StrEnum


class ConfigInputHookKind(StrEnum):
    GATE = "gate"
    TAP = "tap"

    def __str__(self) -> str:
        return str(self.value)
