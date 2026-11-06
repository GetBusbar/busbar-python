from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConfigDiffHooks")


@_attrs_define(repr=False)
class ConfigDiffHooks:
    """The `hooks` object of a `GET /config/diff`: hook names added / removed / changed between the two
    versions.

        Attributes:
            added (list[str]):
            removed (list[str]):
            changed (list[str]):
    """

    added: list[str]
    removed: list[str]
    changed: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        added = self.added

        removed = self.removed

        changed = self.changed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "added": added,
                "removed": removed,
                "changed": changed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        added = cast(list[str], d.pop("added"))

        removed = cast(list[str], d.pop("removed"))

        changed = cast(list[str], d.pop("changed"))

        config_diff_hooks = cls(
            added=added,
            removed=removed,
            changed=changed,
        )

        config_diff_hooks.additional_properties = d
        return config_diff_hooks

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
