from enum import StrEnum


class ConfigSettingsViewDesiredStatus(StrEnum):
    ABSENT = "absent"
    DISABLED = "disabled"
    LOADED = "loaded"
    NEWER_VERSION = "newer_version"
    UNREADABLE = "unreadable"

    def __str__(self) -> str:
        return str(self.value)
