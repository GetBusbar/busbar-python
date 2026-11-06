from enum import StrEnum


class ConfigInputLimitType2Per(StrEnum):
    DAY = "day"
    HOUR = "hour"
    MINUTE = "minute"
    MONTH = "month"
    TOTAL = "total"

    def __str__(self) -> str:
        return str(self.value)
