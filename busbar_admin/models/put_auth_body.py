from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="PutAuthBody")


@_attrs_define
class PutAuthBody:
    """The `PUT /api/v1/admin/admin-auth` body: the replacement admin auth chain.

    Attributes:
        admin_auth (list[str]): The ordered admin auth module chain. Empty is the explicit open dev posture.
    """

    admin_auth: list[str]

    def to_dict(self) -> dict[str, Any]:
        admin_auth = self.admin_auth

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "admin_auth": admin_auth,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        admin_auth = cast(list[str], d.pop("admin_auth"))

        put_auth_body = cls(
            admin_auth=admin_auth,
        )

        return put_auth_body
