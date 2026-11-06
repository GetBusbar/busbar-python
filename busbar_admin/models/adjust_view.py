from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adjust_view_delta import AdjustViewDelta


T = TypeVar("T", bound="AdjustView")


@_attrs_define(repr=False)
class AdjustView:
    """`POST /adjust`'s answer: the correction as applied.

    Attributes:
        applied (bool): Always true: a refused correction is a `400`, and nothing of it is applied.
        key (str): The key corrected.
        lane (str): The lane corrected.
        entry (str): The rate-card history entry key, as 40 lowercase hexadecimal digits.
        card_epoch_ms (int): The corrected unit's card epoch, unix milliseconds: where the correction landed.
        pool (str): The pool the correction names.
        delta (AdjustViewDelta): The signed delta applied, per class.
        retry (Literal['nonretryable_without_idempotency_key'] | Unset):
    """

    applied: bool
    key: str
    lane: str
    entry: str
    card_epoch_ms: int
    pool: str
    delta: AdjustViewDelta
    retry: Literal["nonretryable_without_idempotency_key"] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied = self.applied

        key = self.key

        lane = self.lane

        entry = self.entry

        card_epoch_ms = self.card_epoch_ms

        pool = self.pool

        delta = self.delta.to_dict()

        retry = self.retry

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applied": applied,
                "key": key,
                "lane": lane,
                "entry": entry,
                "card_epoch_ms": card_epoch_ms,
                "pool": pool,
                "delta": delta,
            }
        )
        if retry is not UNSET:
            field_dict["retry"] = retry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adjust_view_delta import AdjustViewDelta  # noqa: PLC0415

        d = dict(src_dict)
        applied = d.pop("applied")

        key = d.pop("key")

        lane = d.pop("lane")

        entry = d.pop("entry")

        card_epoch_ms = d.pop("card_epoch_ms")

        pool = d.pop("pool")

        delta = AdjustViewDelta.from_dict(d.pop("delta"))

        retry = cast(Literal["nonretryable_without_idempotency_key"] | Unset, d.pop("retry", UNSET))
        if retry != "nonretryable_without_idempotency_key" and not isinstance(retry, Unset):
            raise ValueError(f"retry must match const 'nonretryable_without_idempotency_key', got '{retry}'")

        adjust_view = cls(
            applied=applied,
            key=key,
            lane=lane,
            entry=entry,
            card_epoch_ms=card_epoch_ms,
            pool=pool,
            delta=delta,
            retry=retry,
        )

        adjust_view.additional_properties = d
        return adjust_view

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
