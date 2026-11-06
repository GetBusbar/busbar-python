from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ledger_discrepancy import LedgerDiscrepancy
    from ..models.ledger_refused_balance import LedgerRefusedBalance


T = TypeVar("T", bound="LedgerReconciliation")


@_attrs_define(repr=False)
class LedgerReconciliation:
    """`GET /ledger/reconciliation`: whether the ledger's postings reconcile with the previous
    release's rows, and every row on which they do not.

        Attributes:
            holds (bool): True when every row reconciles. `discrepancies` and `refused` are then empty.
            discrepancies (list[LedgerDiscrepancy]):
            refused (list[LedgerRefusedBalance]): Every balance whose counts a present rate card refused to price: its row
                is withheld from
                both sides of the identity, which was not measured over it. Empty is the good answer.
    """

    holds: bool
    discrepancies: list[LedgerDiscrepancy]
    refused: list[LedgerRefusedBalance]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        holds = self.holds

        discrepancies = []
        for discrepancies_item_data in self.discrepancies:
            discrepancies_item = discrepancies_item_data.to_dict()
            discrepancies.append(discrepancies_item)

        refused = []
        for refused_item_data in self.refused:
            refused_item = refused_item_data.to_dict()
            refused.append(refused_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "holds": holds,
                "discrepancies": discrepancies,
                "refused": refused,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ledger_discrepancy import LedgerDiscrepancy  # noqa: PLC0415
        from ..models.ledger_refused_balance import LedgerRefusedBalance  # noqa: PLC0415

        d = dict(src_dict)
        holds = d.pop("holds")

        discrepancies = []
        _discrepancies = d.pop("discrepancies")
        for discrepancies_item_data in _discrepancies:
            discrepancies_item = LedgerDiscrepancy.from_dict(discrepancies_item_data)

            discrepancies.append(discrepancies_item)

        refused = []
        _refused = d.pop("refused")
        for refused_item_data in _refused:
            refused_item = LedgerRefusedBalance.from_dict(refused_item_data)

            refused.append(refused_item)

        ledger_reconciliation = cls(
            holds=holds,
            discrepancies=discrepancies,
            refused=refused,
        )

        ledger_reconciliation.additional_properties = d
        return ledger_reconciliation

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
