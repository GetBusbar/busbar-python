from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.adjustment_action_view_effect import AdjustmentActionViewEffect
from ..models.adjustment_action_view_recovery import AdjustmentActionViewRecovery

T = TypeVar("T", bound="AdjustmentActionView")


@_attrs_define(repr=False)
class AdjustmentActionView:
    """Durable caller-action receipt. A known rejection can have a non-2xx status with this body; unknown is HTTP 409.
    Effect and recovery are authoritative, not the HTTP status alone. applied is true exactly when effect=applied.
    Unknown effects require ledger recovery and never authorize a second delta. This projection intentionally does not
    echo raw counts or reason.

        Attributes:
            operation_id (str):
            operation (Literal['adjust']):
            actor (str):
            target (str): Corrected key id
            fingerprint (str): SHA256 of exact request bytes
            reason_hash (str): SHA256 of the reason bytes; no public reason text
            effect (AdjustmentActionViewEffect):
            applied (bool):
            retry (Literal['same_action_only']):
            recovery (AdjustmentActionViewRecovery):
            count_scale (Literal[6]):
    """

    operation_id: str
    operation: Literal["adjust"]
    actor: str
    target: str
    fingerprint: str
    reason_hash: str
    effect: AdjustmentActionViewEffect
    applied: bool
    retry: Literal["same_action_only"]
    recovery: AdjustmentActionViewRecovery
    count_scale: Literal[6]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation_id = self.operation_id

        operation = self.operation

        actor = self.actor

        target = self.target

        fingerprint = self.fingerprint

        reason_hash = self.reason_hash

        effect = self.effect.value

        applied = self.applied

        retry = self.retry

        recovery = self.recovery.value

        count_scale = self.count_scale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation_id": operation_id,
                "operation": operation,
                "actor": actor,
                "target": target,
                "fingerprint": fingerprint,
                "reason_hash": reason_hash,
                "effect": effect,
                "applied": applied,
                "retry": retry,
                "recovery": recovery,
                "count_scale": count_scale,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation_id = d.pop("operation_id")

        operation = cast(Literal["adjust"], d.pop("operation"))
        if operation != "adjust":
            raise ValueError(f"operation must match const 'adjust', got '{operation}'")

        actor = d.pop("actor")

        target = d.pop("target")

        fingerprint = d.pop("fingerprint")

        reason_hash = d.pop("reason_hash")

        effect = AdjustmentActionViewEffect(d.pop("effect"))

        applied = d.pop("applied")

        retry = cast(Literal["same_action_only"], d.pop("retry"))
        if retry != "same_action_only":
            raise ValueError(f"retry must match const 'same_action_only', got '{retry}'")

        recovery = AdjustmentActionViewRecovery(d.pop("recovery"))

        count_scale = cast(Literal[6], d.pop("count_scale"))
        if count_scale != 6:
            raise ValueError(f"count_scale must match const 6, got '{count_scale}'")

        adjustment_action_view = cls(
            operation_id=operation_id,
            operation=operation,
            actor=actor,
            target=target,
            fingerprint=fingerprint,
            reason_hash=reason_hash,
            effect=effect,
            applied=applied,
            retry=retry,
            recovery=recovery,
            count_scale=count_scale,
        )

        adjustment_action_view.additional_properties = d
        return adjustment_action_view

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
