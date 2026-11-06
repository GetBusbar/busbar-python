from enum import StrEnum


class ConfigInputHookDefinitionKindType0(StrEnum):
    GATE = "gate"
    TAP = "tap"

    def __str__(self) -> str:
        return str(self.value)
