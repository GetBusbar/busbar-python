from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BuildInfo")


@_attrs_define
class BuildInfo:
    """The compiled-in feature proof (`InfoView.build`).

    Attributes:
        auth_modules (list[str]): Auth modules baked into this binary (e.g. `["tokens"]`; empty under `--no-default-
            features`).
        hook_plugins (list[str]): Hook plugins baked into this binary (e.g. `["ranking"]`).
        weighted_floor (bool): The inline SWRR floor: ALWAYS `true` (compiled in unconditionally, non-removable).
    """

    auth_modules: list[str]
    hook_plugins: list[str]
    weighted_floor: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_modules = self.auth_modules

        hook_plugins = self.hook_plugins

        weighted_floor = self.weighted_floor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auth_modules": auth_modules,
                "hook_plugins": hook_plugins,
                "weighted_floor": weighted_floor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_modules = cast(list[str], d.pop("auth_modules"))

        hook_plugins = cast(list[str], d.pop("hook_plugins"))

        weighted_floor = d.pop("weighted_floor")

        build_info = cls(
            auth_modules=auth_modules,
            hook_plugins=hook_plugins,
            weighted_floor=weighted_floor,
        )

        build_info.additional_properties = d
        return build_info

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
