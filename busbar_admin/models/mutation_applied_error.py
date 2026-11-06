from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mutation_applied_error_operation import MutationAppliedErrorOperation
from ..models.mutation_applied_error_recovery import MutationAppliedErrorRecovery

if TYPE_CHECKING:
    from ..models.mutation_applied_error_error import MutationAppliedErrorError


T = TypeVar("T", bound="MutationAppliedError")


@_attrs_define(repr=False)
class MutationAppliedError:
    """The key mutation is known committed; a later cache/readback step failed. This is not a rejected/no-effect mutation.
    Reconcile the named resource. Rotation's new secret is not recoverable from this response; never repeat the old
    action to rotate again.

        Attributes:
            error (MutationAppliedErrorError):
            effect (Literal['applied']):
            operation (MutationAppliedErrorOperation):
            resource (str): Non-secret key:<id> identity
            recovery (MutationAppliedErrorRecovery):
            credential_recoverable (Literal[False]):
    """

    error: MutationAppliedErrorError
    effect: Literal["applied"]
    operation: MutationAppliedErrorOperation
    resource: str
    recovery: MutationAppliedErrorRecovery
    credential_recoverable: Literal[False]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error.to_dict()

        effect = self.effect

        operation = self.operation.value

        resource = self.resource

        recovery = self.recovery.value

        credential_recoverable = self.credential_recoverable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "effect": effect,
                "operation": operation,
                "resource": resource,
                "recovery": recovery,
                "credential_recoverable": credential_recoverable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mutation_applied_error_error import MutationAppliedErrorError  # noqa: PLC0415

        d = dict(src_dict)
        error = MutationAppliedErrorError.from_dict(d.pop("error"))

        effect = cast(Literal["applied"], d.pop("effect"))
        if effect != "applied":
            raise ValueError(f"effect must match const 'applied', got '{effect}'")

        operation = MutationAppliedErrorOperation(d.pop("operation"))

        resource = d.pop("resource")

        recovery = MutationAppliedErrorRecovery(d.pop("recovery"))

        credential_recoverable = cast(Literal[False], d.pop("credential_recoverable"))
        if credential_recoverable != False:
            raise ValueError(f"credential_recoverable must match const False, got '{credential_recoverable}'")

        mutation_applied_error = cls(
            error=error,
            effect=effect,
            operation=operation,
            resource=resource,
            recovery=recovery,
            credential_recoverable=credential_recoverable,
        )

        mutation_applied_error.additional_properties = d
        return mutation_applied_error

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
