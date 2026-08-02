from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OverlayResetView")


@_attrs_define
class OverlayResetView:
    """`DELETE /overlay/{section}` — per-section overlay reset result: the section reverted, the
    resulting config version, and whether anything changed (`false` = the section had no overlay state,
    an idempotent no-op).

        Attributes:
            changed (bool): `true` when the reset discarded overlay mutations; `false` for an already-empty section.
            config_version (int):
            reset (str): The section that was reset (`groups` | `hooks` | `root` | `plugin_versions`).
    """

    changed: bool
    config_version: int
    reset: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changed = self.changed

        config_version = self.config_version

        reset = self.reset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "changed": changed,
                "config_version": config_version,
                "reset": reset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        changed = d.pop("changed")

        config_version = d.pop("config_version")

        reset = d.pop("reset")

        overlay_reset_view = cls(
            changed=changed,
            config_version=config_version,
            reset=reset,
        )

        overlay_reset_view.additional_properties = d
        return overlay_reset_view

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
