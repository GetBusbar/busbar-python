from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigReloadView")


@_attrs_define(repr=False)
class ConfigReloadView:
    """`POST /config/reload`: reload-from-disk result.

    Attributes:
        reloaded (bool):
        config_version (int):
        reload_to_apply (list[str] | Unset): The plane sections this configuration writes whose plane the process did
            not open at boot:
            a plane is opened once, at process start, when its section is configured, so each is stored
            and validated but serves nothing until the next RESTART. Omitted when none.
        note (None | str | Unset): A human note naming the plane sections awaiting restart (omitted with them).
    """

    reloaded: bool
    config_version: int
    reload_to_apply: list[str] | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reloaded = self.reloaded

        config_version = self.config_version

        reload_to_apply: list[str] | Unset = UNSET
        if not isinstance(self.reload_to_apply, Unset):
            reload_to_apply = self.reload_to_apply

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reloaded": reloaded,
                "config_version": config_version,
            }
        )
        if reload_to_apply is not UNSET:
            field_dict["reload_to_apply"] = reload_to_apply
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reloaded = d.pop("reloaded")

        config_version = d.pop("config_version")

        reload_to_apply = cast(list[str], d.pop("reload_to_apply", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        config_reload_view = cls(
            reloaded=reloaded,
            config_version=config_version,
            reload_to_apply=reload_to_apply,
            note=note,
        )

        config_reload_view.additional_properties = d
        return config_reload_view

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
