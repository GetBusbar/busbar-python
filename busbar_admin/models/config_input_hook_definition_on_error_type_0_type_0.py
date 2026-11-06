from enum import StrEnum


class ConfigInputHookDefinitionOnErrorType0Type0(StrEnum):
    FIRST = "first"
    NOTHING = "nothing"
    REJECT = "reject"
    WEIGHTED = "weighted"

    def __str__(self) -> str:
        return str(self.value)
