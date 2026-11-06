from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ClassUsage")


@_attrs_define(repr=False)
class ClassUsage:
    """One plane-declared class's consumption on a usage row: its raw count and its cost.

    NEW IN 1.6.0 (1.5.5's usage rows carried the token split alone, and 1.5.5 served no plane that
    declares a class of its own): ledgered by the FLIP-A2A ruling. `cost` is in the same MICRO-units
    as [`UsageBreakdown::spend_micros`], priced by the same card in force at the row's instant, and is
    part of that row's `spend_micros`, never added to it a second time.

        Attributes:
            count (float): The raw count the plane's ledger lines recorded under the class.
            cost (int): What the card in force priced that count at, in micro-units.
    """

    count: float
    cost: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        cost = self.cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "cost": cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        cost = d.pop("cost")

        class_usage = cls(
            count=count,
            cost=cost,
        )

        class_usage.additional_properties = d
        return class_usage

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
