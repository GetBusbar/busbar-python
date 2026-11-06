from enum import StrEnum


class ConfigInputHookDefinitionUserType0(StrEnum):
    NO = "no"
    RO = "ro"

    def __str__(self) -> str:
        return str(self.value)
