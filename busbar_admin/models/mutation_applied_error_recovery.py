from enum import StrEnum


class MutationAppliedErrorRecovery(StrEnum):
    REREAD_RESOURCE = "reread_resource"
    ROTATE_WITH_NEW_ACTION = "rotate_with_new_action"

    def __str__(self) -> str:
        return str(self.value)
