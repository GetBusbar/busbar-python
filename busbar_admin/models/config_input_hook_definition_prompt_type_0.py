from enum import StrEnum


class ConfigInputHookDefinitionPromptType0(StrEnum):
    NO = "no"
    RO = "ro"
    RW = "rw"

    def __str__(self) -> str:
        return str(self.value)
