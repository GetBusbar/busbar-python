from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.configured_settings_view_settings_public import ConfiguredSettingsViewSettingsPublic


T = TypeVar("T", bound="ConfiguredSettingsView")


@_attrs_define(repr=False)
class ConfiguredSettingsView:
    """
    Attributes:
        config_version (int):
        source (str):
        state (str):
        settings_public (ConfiguredSettingsViewSettingsPublic):
    """

    config_version: int
    source: str
    state: str
    settings_public: ConfiguredSettingsViewSettingsPublic
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config_version = self.config_version

        source = self.source

        state = self.state

        settings_public = self.settings_public.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config_version": config_version,
                "source": source,
                "state": state,
                "settings_public": settings_public,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configured_settings_view_settings_public import ConfiguredSettingsViewSettingsPublic  # noqa: PLC0415

        d = dict(src_dict)
        config_version = d.pop("config_version")

        source = d.pop("source")

        state = d.pop("state")

        settings_public = ConfiguredSettingsViewSettingsPublic.from_dict(d.pop("settings_public"))

        configured_settings_view = cls(
            config_version=config_version,
            source=source,
            state=state,
            settings_public=settings_public,
        )

        configured_settings_view.additional_properties = d
        return configured_settings_view

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
