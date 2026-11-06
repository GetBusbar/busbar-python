from enum import StrEnum


class GetPluginsFileSchemaSource(StrEnum):
    INSTALLED_ARCHIVE = "installed_archive"
    LINKED_STATEMENT = "linked_statement"

    def __str__(self) -> str:
        return str(self.value)
