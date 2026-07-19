from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hook_desired_status_settings import HookDesiredStatusSettings


T = TypeVar("T", bound="HookDesiredStatus")


@_attrs_define
class HookDesiredStatus:
    """The DESIRED settings side of `hooks/{name}/status`: busbar's registry copy of the hook's settings
    and their version.

        Attributes:
            settings (HookDesiredStatusSettings):
            settings_version (int):
    """

    settings: HookDesiredStatusSettings
    settings_version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        settings = self.settings.to_dict()

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
        from ..models.hook_desired_status_settings import HookDesiredStatusSettings

        d = dict(src_dict)
        settings = HookDesiredStatusSettings.from_dict(d.pop("settings"))

        settings_version = d.pop("settings_version")

        hook_desired_status = cls(
            settings=settings,
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
