from enum import StrEnum


class Verdict(StrEnum):
    LANDED = "landed"
    NOT_LANDED = "not_landed"

    def __str__(self) -> str:
        return str(self.value)
