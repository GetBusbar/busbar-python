from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CommitUpgradeView")


@_attrs_define(repr=False)
class CommitUpgradeView:
    """`POST /commit-upgrade`'s answer: the committed release and the journal record that seals it.

    Attributes:
        committed (str):
        committed_at (int): The arrival second.
        hash_ (str): The record's chain hash.
        seq (int): The record's position on the node journal.
    """

    committed: str
    committed_at: int
    hash_: str
    seq: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        committed = self.committed

        committed_at = self.committed_at

        hash_ = self.hash_

        seq = self.seq

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "committed": committed,
                "committed_at": committed_at,
                "hash": hash_,
                "seq": seq,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        committed = d.pop("committed")

        committed_at = d.pop("committed_at")

        hash_ = d.pop("hash")

        seq = d.pop("seq")

        commit_upgrade_view = cls(
            committed=committed,
            committed_at=committed_at,
            hash_=hash_,
            seq=seq,
        )

        commit_upgrade_view.additional_properties = d
        return commit_upgrade_view

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
