from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditChainSignedHead")


@_attrs_define(repr=False)
class AuditChainSignedHead:
    """One signed head of the audit record chain.

    Attributes:
        seq (int): The chain position this head seals.
        hash_ (str): The chain digest at that position.
        signature (None | str): The head's signature, or null for an unsigned chain.
        key_id (None | str): Which key signed it, or null for an unsigned chain.
        wall (int): When the head was sealed, in whole seconds.
    """

    seq: int
    hash_: str
    signature: None | str
    key_id: None | str
    wall: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        seq = self.seq

        hash_ = self.hash_

        signature: None | str
        signature = self.signature

        key_id: None | str
        key_id = self.key_id

        wall = self.wall

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "seq": seq,
                "hash": hash_,
                "signature": signature,
                "key_id": key_id,
                "wall": wall,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        seq = d.pop("seq")

        hash_ = d.pop("hash")

        def _parse_signature(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        signature = _parse_signature(d.pop("signature"))

        def _parse_key_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        key_id = _parse_key_id(d.pop("key_id"))

        wall = d.pop("wall")

        audit_chain_signed_head = cls(
            seq=seq,
            hash_=hash_,
            signature=signature,
            key_id=key_id,
            wall=wall,
        )

        audit_chain_signed_head.additional_properties = d
        return audit_chain_signed_head

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
