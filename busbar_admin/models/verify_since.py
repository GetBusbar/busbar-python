from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VerifySince")


@_attrs_define(repr=False)
class VerifySince:
    """The checkpoint `verify` measured against.

    Attributes:
        checkpoint_seq (int):
        node (int):
        wall (int): When it was sealed, in whole seconds.
    """

    checkpoint_seq: int
    node: int
    wall: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checkpoint_seq = self.checkpoint_seq

        node = self.node

        wall = self.wall

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checkpoint_seq": checkpoint_seq,
                "node": node,
                "wall": wall,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        checkpoint_seq = d.pop("checkpoint_seq")

        node = d.pop("node")

        wall = d.pop("wall")

        verify_since = cls(
            checkpoint_seq=checkpoint_seq,
            node=node,
            wall=wall,
        )

        verify_since.additional_properties = d
        return verify_since

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
