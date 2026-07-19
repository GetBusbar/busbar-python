from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConfigDiffHooks")


@_attrs_define
class ConfigDiffHooks:
    """The `hooks` object of a `GET /config/diff` — hook names added / removed / changed between the two
    versions.

        Attributes:
            added (list[str]):
            changed (list[str]):
            removed (list[str]):
    """

    added: list[str]
    changed: list[str]
    removed: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        added = self.added

        changed = self.changed

        removed = self.removed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "added": added,
                "changed": changed,
                "removed": removed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        added = cast(list[str], d.pop("added"))

        changed = cast(list[str], d.pop("changed"))

        removed = cast(list[str], d.pop("removed"))

        config_diff_hooks = cls(
            added=added,
            changed=changed,
            removed=removed,
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
