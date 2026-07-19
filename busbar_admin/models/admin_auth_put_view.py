from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdminAuthPutView")


@_attrs_define
class AdminAuthPutView:
    """`PUT /admin-auth` — the resource post-state (`{configured, modules}`, the same shape
    `GET /admin-auth` returns) plus apply metadata, so a client uses the PUT response as post-state.

        Attributes:
            applied (bool):
            config_version (int):
            configured (bool):
            modules (list[str]):
            note (str):
    """

    applied: bool
    config_version: int
    configured: bool
    modules: list[str]
    note: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied = self.applied

        config_version = self.config_version

        configured = self.configured

        modules = self.modules

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applied": applied,
                "config_version": config_version,
                "configured": configured,
                "modules": modules,
                "note": note,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        applied = d.pop("applied")

        config_version = d.pop("config_version")

        configured = d.pop("configured")

        modules = cast(list[str], d.pop("modules"))

        note = d.pop("note")

        admin_auth_put_view = cls(
            applied=applied,
            config_version=config_version,
            configured=configured,
            modules=modules,
            note=note,
        )

        admin_auth_put_view.additional_properties = d
        return admin_auth_put_view

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
