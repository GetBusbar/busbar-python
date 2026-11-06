from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LedgerResidual")


@_attrs_define(repr=False)
class LedgerResidual:
    """The spend residual of one row.

    Attributes:
        accounted (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit integers
            and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        drawn (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit integers and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        amount (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit integers and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
    """

    accounted: str
    drawn: str
    amount: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounted = self.accounted

        drawn = self.drawn

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accounted": accounted,
                "drawn": drawn,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accounted = d.pop("accounted")

        drawn = d.pop("drawn")

        amount = d.pop("amount")

        ledger_residual = cls(
            accounted=accounted,
            drawn=drawn,
            amount=amount,
        )

        ledger_residual.additional_properties = d
        return ledger_residual

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
