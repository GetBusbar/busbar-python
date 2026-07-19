from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdminAuthView")


@_attrs_define
class AdminAuthView:
    """The admin-plane auth read (`GET /api/v1/admin/admin-auth`) — which modules guard the ADMIN surface
    (distinct from the ingress `auth` chain). `modules` is the live `admin_auth` chain (the SAME
    resource `PUT /api/v1/admin/admin-auth` writes), so a read-after-write is coherent. An empty chain is
    the open (anonymous, full-authority) dev posture — `configured: false`. Never a secret.

        Attributes:
            configured (bool): Whether an admin credential chain is configured. `false` = the empty chain = open dev
                posture.
            modules (list[str]): The active admin-plane guard module names — the `admin_auth` chain verbatim (e.g.
                `["admin-tokens"]`), reported in order. Empty when the admin plane is open.
    """

    configured: bool
    modules: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configured = self.configured

        modules = self.modules

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configured": configured,
                "modules": modules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        configured = d.pop("configured")

        modules = cast(list[str], d.pop("modules"))

        admin_auth_view = cls(
            configured=configured,
            modules=modules,
        )

        admin_auth_view.additional_properties = d
        return admin_auth_view

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
