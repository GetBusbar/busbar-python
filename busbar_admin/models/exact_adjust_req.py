from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.exact_adjust_req_delta import ExactAdjustReqDelta


T = TypeVar("T", bound="ExactAdjustReq")


@_attrs_define(repr=False)
class ExactAdjustReq:
    """Exact-Count adjustment profile selected only by one valid Idempotency-Key header. Key and exact body bytes identify
    one durable action. Runtime validates count range/scale, entry/epoch, key, pool and nonnegative resulting counts.
    Without the header only the legacy signed-integer request applies.

        Attributes:
            key (str): The key whose counts are corrected.
            lane (str): The lane (model) the counts were earned on.
            entry (str): The rate-card history entry key the counts were priced with, as 40 hexadecimal digits.
            card_epoch_ms (int): The corrected unit's card epoch: its arrival instant, unix milliseconds. The correction
                lands in the budget windows, the card entry and the metering day holding it, never in those
                current when it is made, and `entry` must be the entry in force at it.
            delta (ExactAdjustReqDelta):
            reason (str): Nonblank UTF-8 reason, at most 4096 bytes; only its hash is retained in the safe action receipt.
            pool (str): The pool the corrected unit was dispatched through. Required, and it must name a pool this
                node has configured: a pool-scoped group budget for that pool takes the correction as well
                as the group-wide budgets do.
    """

    key: str
    lane: str
    entry: str
    card_epoch_ms: int
    delta: ExactAdjustReqDelta
    reason: str
    pool: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        lane = self.lane

        entry = self.entry

        card_epoch_ms = self.card_epoch_ms

        delta = self.delta.to_dict()

        reason = self.reason

        pool = self.pool

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "lane": lane,
                "entry": entry,
                "card_epoch_ms": card_epoch_ms,
                "delta": delta,
                "reason": reason,
                "pool": pool,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exact_adjust_req_delta import ExactAdjustReqDelta  # noqa: PLC0415

        d = dict(src_dict)
        key = d.pop("key")

        lane = d.pop("lane")

        entry = d.pop("entry")

        card_epoch_ms = d.pop("card_epoch_ms")

        delta = ExactAdjustReqDelta.from_dict(d.pop("delta"))

        reason = d.pop("reason")

        pool = d.pop("pool")

        exact_adjust_req = cls(
            key=key,
            lane=lane,
            entry=entry,
            card_epoch_ms=card_epoch_ms,
            delta=delta,
            reason=reason,
            pool=pool,
        )

        exact_adjust_req.additional_properties = d
        return exact_adjust_req

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
