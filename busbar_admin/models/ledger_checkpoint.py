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
            backup_watermark (int):
            body_hash (str): A 32-byte digest as 64 lower-case hex characters.
            body_hash_verifies (bool): This node's own answer to whether the sealed body re-hashes to `body_hash`.
            checkpoint_seq (int):
            heads (list[LedgerChainHead]):
            node (int):
            signed (bool): Whether a signature is present. The signature's bytes are never served.
            store_seq_high_water (int):
            totals (list[LedgerTotalsCell]):
            wall (int): When it was sealed, in whole seconds.
    """

    backup_watermark: int
    body_hash: str
    body_hash_verifies: bool
    checkpoint_seq: int
    heads: list[LedgerChainHead]
    node: int
    signed: bool
    store_seq_high_water: int
    totals: list[LedgerTotalsCell]
    wall: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_watermark = self.backup_watermark

        body_hash = self.body_hash

        body_hash_verifies = self.body_hash_verifies

        checkpoint_seq = self.checkpoint_seq

        heads = []
        for heads_item_data in self.heads:
            heads_item = heads_item_data.to_dict()
            heads.append(heads_item)

        node = self.node

        signed = self.signed

        store_seq_high_water = self.store_seq_high_water

        totals = []
        for totals_item_data in self.totals:
            totals_item = totals_item_data.to_dict()
            totals.append(totals_item)

        wall = self.wall

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backup_watermark": backup_watermark,
                "body_hash": body_hash,
                "body_hash_verifies": body_hash_verifies,
                "checkpoint_seq": checkpoint_seq,
                "heads": heads,
                "node": node,
                "signed": signed,
                "store_seq_high_water": store_seq_high_water,
                "totals": totals,
                "wall": wall,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ledger_chain_head import LedgerChainHead  # noqa: PLC0415
        from ..models.ledger_totals_cell import LedgerTotalsCell  # noqa: PLC0415

        d = dict(src_dict)
        backup_watermark = d.pop("backup_watermark")

        body_hash = d.pop("body_hash")

        body_hash_verifies = d.pop("body_hash_verifies")

        checkpoint_seq = d.pop("checkpoint_seq")

        heads = []
        _heads = d.pop("heads")
        for heads_item_data in _heads:
            heads_item = LedgerChainHead.from_dict(heads_item_data)

            heads.append(heads_item)

        node = d.pop("node")

        signed = d.pop("signed")

        store_seq_high_water = d.pop("store_seq_high_water")

        totals = []
        _totals = d.pop("totals")
        for totals_item_data in _totals:
            totals_item = LedgerTotalsCell.from_dict(totals_item_data)

            totals.append(totals_item)

        wall = d.pop("wall")

        ledger_checkpoint = cls(
            backup_watermark=backup_watermark,
            body_hash=body_hash,
            body_hash_verifies=body_hash_verifies,
            checkpoint_seq=checkpoint_seq,
            heads=heads,
            node=node,
            signed=signed,
            store_seq_high_water=store_seq_high_water,
            totals=totals,
            wall=wall,
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
