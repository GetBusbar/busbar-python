from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AmendRateHistoryView")


@_attrs_define(repr=False)
class AmendRateHistoryView:
    """`POST /ledger/amend-rate-history`'s answer: the history entry an invoice will cite. It names no
    figure — the corrected rates go into the card, never into the answer.

        Attributes:
            amended_at (int): When the correction was appended, in milliseconds.
            effective_from (int):
            effective_until (int | None):
            history_seq (int): The history sequence number the correction was appended at.
            reason_sha256 (str): The SHA-256 of the reason, as hex.
    """

    amended_at: int
    effective_from: int
    effective_until: int | None
    history_seq: int
    reason_sha256: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amended_at = self.amended_at

        effective_from = self.effective_from

        effective_until: int | None
        effective_until = self.effective_until

        history_seq = self.history_seq

        reason_sha256 = self.reason_sha256

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amended_at": amended_at,
                "effective_from": effective_from,
                "effective_until": effective_until,
                "history_seq": history_seq,
                "reason_sha256": reason_sha256,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amended_at = d.pop("amended_at")

        effective_from = d.pop("effective_from")

        def _parse_effective_until(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        effective_until = _parse_effective_until(d.pop("effective_until"))

        history_seq = d.pop("history_seq")

        reason_sha256 = d.pop("reason_sha256")

        amend_rate_history_view = cls(
            amended_at=amended_at,
            effective_from=effective_from,
            effective_until=effective_until,
            history_seq=history_seq,
            reason_sha256=reason_sha256,
        )

        amend_rate_history_view.additional_properties = d
        return amend_rate_history_view

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
