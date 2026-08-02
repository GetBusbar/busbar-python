from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutConfigSettingsBody")


@_attrs_define
class PutConfigSettingsBody:
    """The settings sections to replace, keyed by section name. The optional top-level boolean `persist` asserts the change
    MUST be stored in the config overlay: with `persist: true` a busbar that has no overlay refuses with `400
    invalid_request` instead of applying the change in memory only. Omitted or `false` means the change is applied and
    stored where storage is available, and applied in memory only where it is not (the response `note` says which);
    `false` never suppresses storage. Every other top-level key must be a known settings section — an unknown key is a
    400. The accepted shape is the config file's own, documented in the configuration reference; it is not restated here
    because several of its types parse a wire shape that does not match their field layout.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        put_config_settings_body = cls()

        put_config_settings_body.additional_properties = d
        return put_config_settings_body

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
