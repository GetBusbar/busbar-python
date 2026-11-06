from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LedgerRefusedBalance")


@_attrs_define(repr=False)
class LedgerRefusedBalance:
    """A balance with no figure: a unit's counts on it that the rate card in force refused to price
    (a present card silent about the lane or a class). The row the balance folds into — the same
    `bucket` and `day` — is withheld from the view that names this.

        Attributes:
            bucket (str): The balance's bucket.
            dimension (str): The balance's dimension.
            scope (str): The balance's scope.
            day (int): The balance's window, as the unix second it opens at: the `day` of the withheld row.
            lane (str): The lane that served the unit whose counts refused.
            refusal (str): Why the pricing refused, in its own words.
    """

    bucket: str
    dimension: str
    scope: str
    day: int
    lane: str
    refusal: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        dimension = self.dimension

        scope = self.scope

        day = self.day

        lane = self.lane

        refusal = self.refusal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket": bucket,
                "dimension": dimension,
                "scope": scope,
                "day": day,
                "lane": lane,
                "refusal": refusal,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket = d.pop("bucket")

        dimension = d.pop("dimension")

        scope = d.pop("scope")

        day = d.pop("day")

        lane = d.pop("lane")

        refusal = d.pop("refusal")

        ledger_refused_balance = cls(
            bucket=bucket,
            dimension=dimension,
            scope=scope,
            day=day,
            lane=lane,
            refusal=refusal,
        )

        ledger_refused_balance.additional_properties = d
        return ledger_refused_balance

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
