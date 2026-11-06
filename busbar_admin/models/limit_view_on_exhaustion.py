from enum import StrEnum


class LimitViewOnExhaustion(StrEnum):
    CUT_STREAM = "cut-stream"
    FINISH_UNIT = "finish-unit"

    def __str__(self) -> str:
        return str(self.value)
