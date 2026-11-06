from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LedgerChainHead")


@_attrs_define(repr=False)
class LedgerChainHead:
    """One node's journal head, as a checkpoint sealed it.

    Attributes:
        node (int):
        node_seq (int):
        hash_ (str): A 32-byte digest as 64 lower-case hex characters.
    """

    node: int
    node_seq: int
    hash_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node = self.node

        node_seq = self.node_seq

        hash_ = self.hash_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node": node,
                "node_seq": node_seq,
                "hash": hash_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        node = d.pop("node")

        node_seq = d.pop("node_seq")

        hash_ = d.pop("hash")

        ledger_chain_head = cls(
            node=node,
            node_seq=node_seq,
            hash_=hash_,
        )

        ledger_chain_head.additional_properties = d
        return ledger_chain_head

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
