from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HookDesiredStatus")


@_attrs_define
class HookDesiredStatus:
    """The DESIRED settings side of `hooks/{name}/status`: busbar's registry copy of the hook's settings
    (KEY NAMES only, see [`super::HookView::settings_keys`]) and their version.

        Attributes:
            settings_keys (list[str]): Sorted KEY NAMES of the desired settings bag, never its values.
            settings_version (int):
    """

    settings_keys: list[str]
    settings_version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        settings_keys = self.settings_keys

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
        settings_keys = cast(list[str], d.pop("settings_keys"))

        settings_version = d.pop("settings_version")

        hook_desired_status = cls(
            settings_keys=settings_keys,
            settings_version=settings_version,
        )

        hook_desired_status.additional_properties = d
        return hook_desired_status

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
