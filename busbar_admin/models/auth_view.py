from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuthView")


@_attrs_define
class AuthView:
    """The ingress auth chain read (`GET /api/v1/admin/auth`): the ordered module names that authenticate
    callers + the upstream-credential mode. Never a secret — module names and the mode are config
    identifiers, not credentials. An empty `chain` is the open front door (admits every request).

        Attributes:
            chain (list[str]): Ordered auth-chain module names (`[]` = open front door).
            open_ (bool): Whether the front door is open (empty chain admits unconditionally).
            upstream_credentials (str): `"own"` (busbar signs egress with its configured key) or `"passthrough"` (forward
                the caller's
                credential upstream).
    """

    chain: list[str]
    open_: bool
    upstream_credentials: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chain = self.chain

        open_ = self.open_

        upstream_credentials = self.upstream_credentials

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chain": chain,
                "open": open_,
                "upstream_credentials": upstream_credentials,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chain = cast(list[str], d.pop("chain"))

        open_ = d.pop("open")

        upstream_credentials = d.pop("upstream_credentials")

        auth_view = cls(
            chain=chain,
            open_=open_,
            upstream_credentials=upstream_credentials,
        )

        auth_view.additional_properties = d
        return auth_view

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
