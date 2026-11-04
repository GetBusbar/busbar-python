from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigApplyView")


@_attrs_define(repr=False)
class ConfigApplyView:
    """`POST /config/apply`: apply-a-full-config result. The change is live but not written to disk.

    Attributes:
        applied (bool):
        config_version (int):
        note (str):
        reload_to_apply (list[str] | Unset): The plane sections this configuration writes whose plane the process did
            not open at boot:
            a plane is opened once, at process start, when its section is configured, so each is stored
            and validated but serves nothing until the next RESTART. Omitted when none.
    """

    applied: bool
    config_version: int
    note: str
    reload_to_apply: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied = self.applied

        config_version = self.config_version

        note = self.note

        reload_to_apply: list[str] | Unset = UNSET
        if not isinstance(self.reload_to_apply, Unset):
            reload_to_apply = self.reload_to_apply

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applied": applied,
                "config_version": config_version,
                "note": note,
            }
        )
        if reload_to_apply is not UNSET:
            field_dict["reload_to_apply"] = reload_to_apply

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        applied = d.pop("applied")

        config_version = d.pop("config_version")

        note = d.pop("note")

        reload_to_apply = cast(list[str], d.pop("reload_to_apply", UNSET))

        config_apply_view = cls(
            applied=applied,
            config_version=config_version,
            note=note,
            reload_to_apply=reload_to_apply,
        )

        config_apply_view.additional_properties = d
        return config_apply_view

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
