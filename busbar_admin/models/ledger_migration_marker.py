from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LedgerMigrationMarker")


@_attrs_define(repr=False)
class LedgerMigrationMarker:
    """The marker the first boot after the upgrade sealed.

    Attributes:
        balances (int): How many balances the opening carries.
        body_hash (str): A 32-byte digest as 64 lower-case hex characters.
        cells_read (int): How many of the previous release's cells were read to arrive at them.
        checkpoint_seq (int): The checkpoint the migration sealed.
        node (int): Which node sealed it.
        rate_card_version (int): Which card version the opening entries were priced under.
        sealed_at (int): When, in whole seconds.
    """

    balances: int
    body_hash: str
    cells_read: int
    checkpoint_seq: int
    node: int
    rate_card_version: int
    sealed_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balances = self.balances

        body_hash = self.body_hash

        cells_read = self.cells_read

        checkpoint_seq = self.checkpoint_seq

        node = self.node

        rate_card_version = self.rate_card_version

        sealed_at = self.sealed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "balances": balances,
                "body_hash": body_hash,
                "cells_read": cells_read,
                "checkpoint_seq": checkpoint_seq,
                "node": node,
                "rate_card_version": rate_card_version,
                "sealed_at": sealed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        balances = d.pop("balances")

        body_hash = d.pop("body_hash")

        cells_read = d.pop("cells_read")

        checkpoint_seq = d.pop("checkpoint_seq")

        node = d.pop("node")

        rate_card_version = d.pop("rate_card_version")

        sealed_at = d.pop("sealed_at")

        ledger_migration_marker = cls(
            balances=balances,
            body_hash=body_hash,
            cells_read=cells_read,
            checkpoint_seq=checkpoint_seq,
            node=node,
            rate_card_version=rate_card_version,
            sealed_at=sealed_at,
        )

        ledger_migration_marker.additional_properties = d
        return ledger_migration_marker

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
