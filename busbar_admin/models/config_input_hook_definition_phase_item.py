from enum import StrEnum


class ConfigInputHookDefinitionPhaseItem(StrEnum):
    CANDIDATE = "candidate"
    REQUEST = "request"
    RESPONSE = "response"
    ROUTING = "routing"

    def __str__(self) -> str:
        return str(self.value)
