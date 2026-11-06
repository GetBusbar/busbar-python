from enum import StrEnum


class PatchGroupsNameBodyClearItem(StrEnum):
    CHILD_DEFAULT = "child_default"
    PARENT = "parent"

    def __str__(self) -> str:
        return str(self.value)
