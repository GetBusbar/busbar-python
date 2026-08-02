from enum import Enum


class DeleteOverlaySectionSection(str, Enum):
    GROUPS = "groups"
    HOOKS = "hooks"
    PLUGIN_VERSIONS = "plugin_versions"
    ROOT = "root"

    def __str__(self) -> str:
        return str(self.value)
