from enum import StrEnum


class Phase(StrEnum):
    LLMPRODUCERDRIVE = "LlmProducerDrive"
    MOUNTEDRESPONSEREADY = "MountedResponseReady"

    def __str__(self) -> str:
        return str(self.value)
