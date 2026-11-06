from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.verdict import Verdict

T = TypeVar("T", bound="ResolveRequest")


@_attrs_define(repr=False)
class ResolveRequest:
    """The immutable operation and recovery version inspected by the operator.

    Attributes:
        operation_id (str): The original operation id as 32 lower-case hexadecimal characters.
        body_fingerprint (str): The retained operation body's SHA-256 fingerprint as 64 lower-case hex characters.
        recovery_version (int): The current recovery version; a stale observation is refused.
        verdict (Verdict): An explicit operator observation of whether the retained operation landed.
        reason (str): The evidence behind the explicit verdict; retained in the durable audit record.
        sender_quiesced (bool): Explicitly attest that every sender for this operation is retired or disarmed.
        backend_quiesced (bool): Explicitly attest that every outstanding backend mutation for this operation settled.
    """

    operation_id: str
    body_fingerprint: str
    recovery_version: int
    verdict: Verdict
    reason: str
    sender_quiesced: bool
    backend_quiesced: bool

    def to_dict(self) -> dict[str, Any]:
        operation_id = self.operation_id

        body_fingerprint = self.body_fingerprint

        recovery_version = self.recovery_version

        verdict = self.verdict.value

        reason = self.reason

        sender_quiesced = self.sender_quiesced

        backend_quiesced = self.backend_quiesced

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "operation_id": operation_id,
                "body_fingerprint": body_fingerprint,
                "recovery_version": recovery_version,
                "verdict": verdict,
                "reason": reason,
                "sender_quiesced": sender_quiesced,
                "backend_quiesced": backend_quiesced,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation_id = d.pop("operation_id")

        body_fingerprint = d.pop("body_fingerprint")

        recovery_version = d.pop("recovery_version")

        verdict = Verdict(d.pop("verdict"))

        reason = d.pop("reason")

        sender_quiesced = d.pop("sender_quiesced")

        backend_quiesced = d.pop("backend_quiesced")

        if d:
            raise ValueError("Unexpected fields for ResolveRequest")
        resolve_request = cls(
            operation_id=operation_id,
            body_fingerprint=body_fingerprint,
            recovery_version=recovery_version,
            verdict=verdict,
            reason=reason,
            sender_quiesced=sender_quiesced,
            backend_quiesced=backend_quiesced,
        )

        return resolve_request
