from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ledger_checkpoint import LedgerCheckpoint


T = TypeVar("T", bound="LedgerCheckpoints")


@_attrs_define(repr=False)
class LedgerCheckpoints:
    """`GET /ledger/checkpoints`: the sealed checkpoint figures, oldest first.

    Attributes:
        checkpoints (list[LedgerCheckpoint]):
    """

    checkpoints: list[LedgerCheckpoint]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checkpoints = []
        for checkpoints_item_data in self.checkpoints:
            checkpoints_item = checkpoints_item_data.to_dict()
            checkpoints.append(checkpoints_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checkpoints": checkpoints,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ledger_checkpoint import LedgerCheckpoint  # noqa: PLC0415

        d = dict(src_dict)
        checkpoints = []
        _checkpoints = d.pop("checkpoints")
        for checkpoints_item_data in _checkpoints:
            checkpoints_item = LedgerCheckpoint.from_dict(checkpoints_item_data)

            checkpoints.append(checkpoints_item)

        ledger_checkpoints = cls(
            checkpoints=checkpoints,
        )

        ledger_checkpoints.additional_properties = d
        return ledger_checkpoints

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
