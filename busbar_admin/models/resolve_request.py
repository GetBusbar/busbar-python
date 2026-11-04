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
        backend_quiesced (bool): Explicitly attest that every outstanding backend mutation for this operation settled.
        body_fingerprint (str): The retained operation body's SHA-256 fingerprint as 64 lower-case hex characters.
        operation_id (str): The original operation id as 32 lower-case hexadecimal characters.
        reason (str): The evidence behind the explicit verdict; retained in the durable audit record.
        recovery_version (int): The current recovery version; a stale observation is refused.
        sender_quiesced (bool): Explicitly attest that every sender for this operation is retired or disarmed.
        verdict (Verdict): An explicit operator observation of whether the retained operation landed.
    """

    backend_quiesced: bool
    body_fingerprint: str
    operation_id: str
    reason: str
    recovery_version: int
    sender_quiesced: bool
    verdict: Verdict

    def to_dict(self) -> dict[str, Any]:
        backend_quiesced = self.backend_quiesced

        body_fingerprint = self.body_fingerprint

        operation_id = self.operation_id

        reason = self.reason

        recovery_version = self.recovery_version

        sender_quiesced = self.sender_quiesced

        verdict = self.verdict.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "backend_quiesced": backend_quiesced,
                "body_fingerprint": body_fingerprint,
                "operation_id": operation_id,
                "reason": reason,
                "recovery_version": recovery_version,
                "sender_quiesced": sender_quiesced,
                "verdict": verdict,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backend_quiesced = d.pop("backend_quiesced")

        body_fingerprint = d.pop("body_fingerprint")

        operation_id = d.pop("operation_id")

        reason = d.pop("reason")

        recovery_version = d.pop("recovery_version")

        sender_quiesced = d.pop("sender_quiesced")

        verdict = Verdict(d.pop("verdict"))

        if d:
            raise ValueError("Unexpected fields for ResolveRequest")
        resolve_request = cls(
            backend_quiesced=backend_quiesced,
            body_fingerprint=body_fingerprint,
            operation_id=operation_id,
            reason=reason,
            recovery_version=recovery_version,
            sender_quiesced=sender_quiesced,
            verdict=verdict,
        )

        return resolve_request
