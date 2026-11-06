from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.adjustment_action_in_flight_error_error import AdjustmentActionInFlightErrorError


T = TypeVar("T", bound="AdjustmentActionInFlightError")


@_attrs_define(repr=False)
class AdjustmentActionInFlightError:
    """
    Attributes:
        error (AdjustmentActionInFlightErrorError):
        operation_id (str):
        effect (Literal['unknown']):
        recovery (Literal['reconcile_ledger_recovery']):
    """

    error: AdjustmentActionInFlightErrorError
    operation_id: str
    effect: Literal["unknown"]
    recovery: Literal["reconcile_ledger_recovery"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error.to_dict()

        operation_id = self.operation_id

        effect = self.effect

        recovery = self.recovery

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "operation_id": operation_id,
                "effect": effect,
                "recovery": recovery,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adjustment_action_in_flight_error_error import AdjustmentActionInFlightErrorError  # noqa: PLC0415

        d = dict(src_dict)
        error = AdjustmentActionInFlightErrorError.from_dict(d.pop("error"))

        operation_id = d.pop("operation_id")

        effect = cast(Literal["unknown"], d.pop("effect"))
        if effect != "unknown":
            raise ValueError(f"effect must match const 'unknown', got '{effect}'")

        recovery = cast(Literal["reconcile_ledger_recovery"], d.pop("recovery"))
        if recovery != "reconcile_ledger_recovery":
            raise ValueError(f"recovery must match const 'reconcile_ledger_recovery', got '{recovery}'")

        adjustment_action_in_flight_error = cls(
            error=error,
            operation_id=operation_id,
            effect=effect,
            recovery=recovery,
        )

        adjustment_action_in_flight_error.additional_properties = d
        return adjustment_action_in_flight_error

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
