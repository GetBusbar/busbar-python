from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hook_reported_status_settings_type_0 import HookReportedStatusSettingsType0


T = TypeVar("T", bound="HookReportedStatus")


@_attrs_define
class HookReportedStatus:
    """The REPORTED settings side of `hooks/{name}/status`: what the hook says it is actually running
    (present only when the hook answered `status`).

        Attributes:
            settings (HookReportedStatusSettingsType0 | None):
            settings_version (int | None):
    """

    settings: HookReportedStatusSettingsType0 | None
    settings_version: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hook_reported_status_settings_type_0 import HookReportedStatusSettingsType0

        settings: dict[str, Any] | None
        if isinstance(self.settings, HookReportedStatusSettingsType0):
            settings = self.settings.to_dict()
        else:
            settings = self.settings

        settings_version: int | None
        settings_version = self.settings_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "settings": settings,
                "settings_version": settings_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hook_reported_status_settings_type_0 import HookReportedStatusSettingsType0

        d = dict(src_dict)

        def _parse_settings(data: object) -> HookReportedStatusSettingsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_0 = HookReportedStatusSettingsType0.from_dict(data)

                return settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HookReportedStatusSettingsType0 | None, data)

        settings = _parse_settings(d.pop("settings"))

        def _parse_settings_version(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        settings_version = _parse_settings_version(d.pop("settings_version"))

        hook_reported_status = cls(
            settings=settings,
            settings_version=settings_version,
        )

        hook_reported_status.additional_properties = d
        return hook_reported_status

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
