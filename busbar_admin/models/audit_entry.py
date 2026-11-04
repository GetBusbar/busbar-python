from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditEntry")


@_attrs_define(repr=False)
class AuditEntry:
    """One admin audit record. `outcome` is a stable token tooling can branch on. The record is
    HASH-CHAINED for tamper-EVIDENCE: `hash` is the SHA-256 of bytes fixed by this record's own
    `scheme` (the recipe is on `hash`), and `prev_hash` is the preceding entry's `hash`. Recomputing
    the chain detects any altered/reordered/deleted entry (detection, not prevention; a compromised
    host can still rewrite the whole chain; prevention is shipping the log off-box to a SIEM).

        Attributes:
            action (str): The action, `noun.verb` (e.g. `hook.register`, `hook.delete`).
            hash_ (str): The tamper-evidence digest: lowercase hex SHA-256 over the bytes this record's `scheme` names.
                Integers are written in decimal ASCII and strings as their UTF-8 bytes unless stated.

                Scheme 1: `prev_hash|seq|ts|action|resource|outcome|principal`, the fields joined by `|`
                (1.5.5's formula).

                Scheme 2: `prev_hash|seq` as in scheme 1, then one zero byte (0x00), then `ts`, `action`,
                `resource`, `outcome` and `principal`, each as its byte length (8 bytes, big-endian) followed
                by its bytes; `ts` is its 8-byte big-endian value, so its length is 8.
            outcome (str): Stable outcome token: `applied` (mutation committed) | `rejected` (validation/conflict, nothing
                changed).
            prev_hash (str): The preceding entry's `hash` (empty for the first entry of the process, or the oldest retained
                entry whose predecessor was pruned).
            principal (str): WHO: the authenticated principal id that attempted the mutation (`admin` for the operator
                token; a virtual-key id or an external module's principal id otherwise; `anonymous` for the
                explicit open admin posture). Attribution, never a credential.
            resource (str): The resource acted on (e.g. `hook:compress`). Never a secret.
            scheme (int): WHICH RECIPE `hash` was sealed under: 1 (the 1.5.5 pipe join) or 2 (length-prefixed fields);
                both are stated on `hash`. A record is sealed under 1 when its `action`, `resource` and
                `outcome` carry no `|`, and under 2 otherwise, so its fields always read back exactly. A
                record without this field is scheme 1. A verifier checks each record under its own scheme. Default: 1.
            seq (int): Monotonic sequence number (1-based), unique within a process lifetime.
            ts (int): Unix seconds when the mutation was attempted.
    """

    action: str
    hash_: str
    outcome: str
    prev_hash: str
    principal: str
    resource: str
    seq: int
    ts: int
    scheme: int = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        hash_ = self.hash_

        outcome = self.outcome

        prev_hash = self.prev_hash

        principal = self.principal

        resource = self.resource

        scheme = self.scheme

        seq = self.seq

        ts = self.ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "hash": hash_,
                "outcome": outcome,
                "prev_hash": prev_hash,
                "principal": principal,
                "resource": resource,
                "scheme": scheme,
                "seq": seq,
                "ts": ts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        hash_ = d.pop("hash")

        outcome = d.pop("outcome")

        prev_hash = d.pop("prev_hash")

        principal = d.pop("principal")

        resource = d.pop("resource")

        scheme = d.pop("scheme")

        seq = d.pop("seq")

        ts = d.pop("ts")

        audit_entry = cls(
            action=action,
            hash_=hash_,
            outcome=outcome,
            prev_hash=prev_hash,
            principal=principal,
            resource=resource,
            scheme=scheme,
            seq=seq,
            ts=ts,
        )

        audit_entry.additional_properties = d
        return audit_entry

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
