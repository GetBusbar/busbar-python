from enum import StrEnum


class AdjustmentActionViewRecovery(StrEnum):
    RECEIPT = "receipt"
    RECONCILE_LEDGER_RECOVERY = "reconcile_ledger_recovery"

    def __str__(self) -> str:
        return str(self.value)
