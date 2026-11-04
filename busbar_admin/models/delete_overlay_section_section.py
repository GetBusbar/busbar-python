from enum import StrEnum


class DeleteOverlaySectionSection(StrEnum):
    AGENTS = "agents"
    EXPORT = "export"
    GROUPS = "groups"
    HOOKS = "hooks"
    IDENTITY_PROVIDERS = "identity-providers"
    PLUGIN_VERSIONS = "plugin_versions"
    ROOT = "root"
    TOOLS = "tools"

    def __str__(self) -> str:
        return str(self.value)
