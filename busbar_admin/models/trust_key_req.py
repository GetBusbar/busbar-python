from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrustKeyReq")


@_attrs_define(repr=False)
class TrustKeyReq:
    """`POST /trust/approve` and `/trust/revoke`: the trust key decided.

    Attributes:
        key (str): `<instance>/<counterparty>[/<item>]`, as `GET /trust` lists it.
        expected_digest (str | Unset): Optional compare-and-set guard against this key's current `seen` digest, for both
            approve
            and revoke. Supply the exact digest reviewed from `GET /trust`, not `approved`. A changed
            or absent sighting returns 409 without changing the decision. Omission keeps key-only
            behavior; an explicitly supplied null, empty string or non-string is invalid.
    """

    key: str
    expected_digest: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        expected_digest = self.expected_digest

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
            }
        )
        if expected_digest is not UNSET:
            field_dict["expected_digest"] = expected_digest

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        expected_digest = d.pop("expected_digest", UNSET)

        trust_key_req = cls(
            key=key,
            expected_digest=expected_digest,
        )

        trust_key_req.additional_properties = d
        return trust_key_req

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
