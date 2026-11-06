from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ledger_chain_head import LedgerChainHead
    from ..models.ledger_totals_cell import LedgerTotalsCell


T = TypeVar("T", bound="LedgerCheckpoint")


@_attrs_define(repr=False)
class LedgerCheckpoint:
    """One sealed checkpoint. `body_hash` is what an auditor re-derives independently;
    `body_hash_verifies` is this node's own answer to the same question. A signature's presence is
    reported and its bytes are not.

        Attributes:
            checkpoint_seq (int):
            node (int):
            wall (int): When it was sealed, in whole seconds.
            backup_watermark (int):
            store_seq_high_water (int):
            body_hash (str): A 32-byte digest as 64 lower-case hex characters.
            body_hash_verifies (bool): This node's own answer to whether the sealed body re-hashes to `body_hash`.
            signed (bool): Whether a signature is present. The signature's bytes are never served.
            heads (list[LedgerChainHead]):
            totals (list[LedgerTotalsCell]):
    """

    checkpoint_seq: int
    node: int
    wall: int
    backup_watermark: int
    store_seq_high_water: int
    body_hash: str
    body_hash_verifies: bool
    signed: bool
    heads: list[LedgerChainHead]
    totals: list[LedgerTotalsCell]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checkpoint_seq = self.checkpoint_seq

        node = self.node

        wall = self.wall

        backup_watermark = self.backup_watermark

        store_seq_high_water = self.store_seq_high_water

        body_hash = self.body_hash

        body_hash_verifies = self.body_hash_verifies

        signed = self.signed

        heads = []
        for heads_item_data in self.heads:
            heads_item = heads_item_data.to_dict()
            heads.append(heads_item)

        totals = []
        for totals_item_data in self.totals:
            totals_item = totals_item_data.to_dict()
            totals.append(totals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checkpoint_seq": checkpoint_seq,
                "node": node,
                "wall": wall,
                "backup_watermark": backup_watermark,
                "store_seq_high_water": store_seq_high_water,
                "body_hash": body_hash,
                "body_hash_verifies": body_hash_verifies,
                "signed": signed,
                "heads": heads,
                "totals": totals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ledger_chain_head import LedgerChainHead  # noqa: PLC0415
        from ..models.ledger_totals_cell import LedgerTotalsCell  # noqa: PLC0415

        d = dict(src_dict)
        checkpoint_seq = d.pop("checkpoint_seq")

        node = d.pop("node")

        wall = d.pop("wall")

        backup_watermark = d.pop("backup_watermark")

        store_seq_high_water = d.pop("store_seq_high_water")

        body_hash = d.pop("body_hash")

        body_hash_verifies = d.pop("body_hash_verifies")

        signed = d.pop("signed")

        heads = []
        _heads = d.pop("heads")
        for heads_item_data in _heads:
            heads_item = LedgerChainHead.from_dict(heads_item_data)

            heads.append(heads_item)

        totals = []
        _totals = d.pop("totals")
        for totals_item_data in _totals:
            totals_item = LedgerTotalsCell.from_dict(totals_item_data)

            totals.append(totals_item)

        ledger_checkpoint = cls(
            checkpoint_seq=checkpoint_seq,
            node=node,
            wall=wall,
            backup_watermark=backup_watermark,
            store_seq_high_water=store_seq_high_water,
            body_hash=body_hash,
            body_hash_verifies=body_hash_verifies,
            signed=signed,
            heads=heads,
            totals=totals,
        )

        ledger_checkpoint.additional_properties = d
        return ledger_checkpoint

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
