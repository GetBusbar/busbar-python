from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Dropped")


@_attrs_define(repr=False)
class Dropped:
    """
    Attributes:
        invalid_duration (str): Unsigned 64-bit integer as an exact decimal string.
        integer_overflow (str): Unsigned 64-bit integer as an exact decimal string.
        series_capacity (str): Unsigned 64-bit integer as an exact decimal string.
        boot_nonce_unavailable (str): Unsigned 64-bit integer as an exact decimal string.
        histogram_capacity (str): Unsigned 64-bit integer as an exact decimal string.
        unregistered_labels (str): Unsigned 64-bit integer as an exact decimal string.
    """

    invalid_duration: str
    integer_overflow: str
    series_capacity: str
    boot_nonce_unavailable: str
    histogram_capacity: str
    unregistered_labels: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invalid_duration = self.invalid_duration

        integer_overflow = self.integer_overflow

        series_capacity = self.series_capacity

        boot_nonce_unavailable = self.boot_nonce_unavailable

        histogram_capacity = self.histogram_capacity

        unregistered_labels = self.unregistered_labels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invalid_duration": invalid_duration,
                "integer_overflow": integer_overflow,
                "series_capacity": series_capacity,
                "boot_nonce_unavailable": boot_nonce_unavailable,
                "histogram_capacity": histogram_capacity,
                "unregistered_labels": unregistered_labels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        invalid_duration = d.pop("invalid_duration")

        integer_overflow = d.pop("integer_overflow")

        series_capacity = d.pop("series_capacity")

        boot_nonce_unavailable = d.pop("boot_nonce_unavailable")

        histogram_capacity = d.pop("histogram_capacity")

        unregistered_labels = d.pop("unregistered_labels")

        dropped = cls(
            invalid_duration=invalid_duration,
            integer_overflow=integer_overflow,
            series_capacity=series_capacity,
            boot_nonce_unavailable=boot_nonce_unavailable,
            histogram_capacity=histogram_capacity,
            unregistered_labels=unregistered_labels,
        )

        dropped.additional_properties = d
        return dropped

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
