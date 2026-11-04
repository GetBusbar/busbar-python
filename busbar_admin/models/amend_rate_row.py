from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AmendRateRow")


@_attrs_define(repr=False)
class AmendRateRow:
    """One corrected rate.

    Attributes:
        class_ (str): The billable class.
        lane (str): The lane the rate is written against.
        micro_per_unit (float): The rate, in micro-units per unit. Finite and non-negative.
    """

    class_: str
    lane: str
    micro_per_unit: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        class_ = self.class_

        lane = self.lane

        micro_per_unit = self.micro_per_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "class": class_,
                "lane": lane,
                "micro_per_unit": micro_per_unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        class_ = d.pop("class")

        lane = d.pop("lane")

        micro_per_unit = d.pop("micro_per_unit")

        amend_rate_row = cls(
            class_=class_,
            lane=lane,
            micro_per_unit=micro_per_unit,
        )

        amend_rate_row.additional_properties = d
        return amend_rate_row

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
