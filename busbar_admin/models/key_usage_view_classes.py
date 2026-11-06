from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.class_usage import ClassUsage


T = TypeVar("T", bound="KeyUsageViewClasses")


@_attrs_define(repr=False)
class KeyUsageViewClasses:
    """Every ledgered class outside the reserved token split, keyed by class name ([`ClassUsage`]).
    Includes open classes from every provider and plane. Absent when the row carries none.

    """

    additional_properties: dict[str, ClassUsage] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.class_usage import ClassUsage  # noqa: PLC0415

        d = dict(src_dict)
        key_usage_view_classes = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ClassUsage.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        key_usage_view_classes.additional_properties = additional_properties
        return key_usage_view_classes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ClassUsage:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ClassUsage) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
