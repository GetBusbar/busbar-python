from enum import StrEnum


class ConfigInputHookOnEmptyType0(StrEnum):
    FIRST = "first"
    REJECT = "reject"
    WEIGHTED = "weighted"

    def __str__(self) -> str:
        return str(self.value)
