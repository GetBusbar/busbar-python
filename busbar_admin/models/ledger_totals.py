from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ledger_refused_balance import LedgerRefusedBalance
    from ..models.ledger_totals_row import LedgerTotalsRow


T = TypeVar("T", bound="LedgerTotals")


@_attrs_define(repr=False)
class LedgerTotals:
    """`GET /ledger/totals`: what the ledger's lines come to, per bucket, day, lane and provider.

    Attributes:
        rows (list[LedgerTotalsRow]): The rows, in bucket, day, lane and provider order. A row a `refused` entry names
            is absent.
        refused (list[LedgerRefusedBalance]): Every balance whose counts a present rate card refused to price: its row
            has no figure, so
            it is withheld from `rows` rather than served as the priced remainder. Empty is the good
            answer.
    """

    rows: list[LedgerTotalsRow]
    refused: list[LedgerRefusedBalance]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        refused = []
        for refused_item_data in self.refused:
            refused_item = refused_item_data.to_dict()
            refused.append(refused_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rows": rows,
                "refused": refused,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ledger_refused_balance import LedgerRefusedBalance  # noqa: PLC0415
        from ..models.ledger_totals_row import LedgerTotalsRow  # noqa: PLC0415

        d = dict(src_dict)
        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = LedgerTotalsRow.from_dict(rows_item_data)

            rows.append(rows_item)

        refused = []
        _refused = d.pop("refused")
        for refused_item_data in _refused:
            refused_item = LedgerRefusedBalance.from_dict(refused_item_data)

            refused.append(refused_item)

        ledger_totals = cls(
            rows=rows,
            refused=refused,
        )

        ledger_totals.additional_properties = d
        return ledger_totals

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
