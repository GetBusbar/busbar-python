from enum import StrEnum


class ConfigInputHookUser(StrEnum):
    NO = "no"
    RO = "ro"

    def __str__(self) -> str:
        return str(self.value)
