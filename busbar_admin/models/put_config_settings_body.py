from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutConfigSettingsBody")


@_attrs_define
class PutConfigSettingsBody:
    """The settings sections to replace, keyed by section name. Durable by default (1.5.3): a mutable config always stores
    the change in its overlay (survives restart), and a locked config (`config.locked: true`) refuses ANY change with
    `400`. There is no "apply in memory only" outcome. The optional top-level boolean `persist` is accepted for back-
    compat and boolean-validated (a non-boolean is a 400 naming the field), but its value has NO effect: persistence is
    unconditional on a mutable config and refusal is unconditional on a locked one. Every other top-level key must be a
    known settings section; an unknown key is a 400. The accepted shape is the config file's own, documented in the
    configuration reference; it is not restated here because several of its types parse a wire shape that does not match
    their field layout.

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
