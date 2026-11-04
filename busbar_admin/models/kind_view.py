from enum import StrEnum


class KindView(StrEnum):
    CORRECTION = "correction"
    METERING = "metering"
    USAGE = "usage"

    def __str__(self) -> str:
        return str(self.value)
