from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HookReportedStatus")


@_attrs_define
class HookReportedStatus:
    """The REPORTED settings side of `hooks/{name}/status`: what the hook says it is actually running
    (present only when the hook answered `status`).

    KEY NAMES only, and for a sharper reason than the desired side: the reported bag is the hook's
    ECHO of the SECRET-RESOLVED settings busbar pushed it, i.e. the PLAINTEXT of every `SecretRef`,
    and this read is reachable at READ-ONLY admin scope. `null` when the hook answered `status` but
    reported no settings.

        Attributes:
            settings_keys (list[str] | None): Sorted KEY NAMES of the observed settings bag, never its values.
            settings_version (int | None):
    """

    settings_keys: list[str] | None
    settings_version: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        settings_keys: list[str] | None
        if isinstance(self.settings_keys, list):
            settings_keys = self.settings_keys

        else:
            settings_keys = self.settings_keys

        settings_version: int | None
        settings_version = self.settings_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "settings_keys": settings_keys,
                "settings_version": settings_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_settings_keys(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                settings_keys_type_0 = cast(list[str], data)

                return settings_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        settings_keys = _parse_settings_keys(d.pop("settings_keys"))

        def _parse_settings_version(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        settings_version = _parse_settings_version(d.pop("settings_version"))

        hook_reported_status = cls(
            settings_keys=settings_keys,
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
