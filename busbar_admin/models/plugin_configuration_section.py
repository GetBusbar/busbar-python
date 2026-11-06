from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PluginConfigurationSection")


@_attrs_define(repr=False)
class PluginConfigurationSection:
    """
    Attributes:
        name (str):
        declaring (bool):
        consumed (bool):
        required (bool):
        selects (bool):
    """

    name: str
    declaring: bool
    consumed: bool
    required: bool
    selects: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        declaring = self.declaring

        consumed = self.consumed

        required = self.required

        selects = self.selects

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "declaring": declaring,
                "consumed": consumed,
                "required": required,
                "selects": selects,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        declaring = d.pop("declaring")

        consumed = d.pop("consumed")

        required = d.pop("required")

        selects = d.pop("selects")

        plugin_configuration_section = cls(
            name=name,
            declaring=declaring,
            consumed=consumed,
            required=required,
            selects=selects,
        )

        plugin_configuration_section.additional_properties = d
        return plugin_configuration_section

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
