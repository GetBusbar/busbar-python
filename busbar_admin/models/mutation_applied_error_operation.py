from enum import StrEnum


class MutationAppliedErrorOperation(StrEnum):
    KEY_DELETE = "key.delete"
    KEY_PATCH = "key.patch"
    KEY_ROTATE = "key.rotate"

    def __str__(self) -> str:
        return str(self.value)
