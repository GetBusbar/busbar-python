from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="A2ATrustView")


@_attrs_define(repr=False)
class A2ATrustView:
    """THE TRUST VIEW of one registered agent — what both verbs answer with.

    The sibling of `busbar_mcp::mcp::admin_view::McpTrustView` and shaped like it on purpose: an
    operator console rendering both planes should be rendering one component. It is NOT the same
    type, because the two planes' capability vocabularies differ (a `tools:` entry has an approved
    digest per tool; an `agents:` entry has a skill set on a card) and merging them would mean one
    of the planes filling in fields that mean nothing to it.

        Attributes:
            added (list[str]): Offered now, never ruled on.
            changed (list[str]): Approved, but offered at a DIFFERENT digest. THIS IS THE RUG-PULL ROW.
            failure (None | str): Why the contact failed, when it did.
            fingerprint (None | str): THE CANONICAL CARD FINGERPRINT AN OPERATOR IS BEING ASKED TO APPROVE. Surfaced
                explicitly
                rather than left for a caller to dig out, because this is the one string that goes in front
                of the human and `approve` refuses anything else.
            name (str):
            observed_skills (int): How many skills the observation carried.
            pin_changed (bool): The presented identity is not the locked one. Its own axis: adopting a new identity is a
                different act from adopting new content.
            pin_mechanism (str): The operator's word for the authenticity root, as the OBSERVED pin names it. Never
                interpreted by the machine.
            removed (list[str]): Approved, and no longer offered.
            state (str): `pending`, `approved`, `quarantined`, `suspended` or `error`. DERIVED on every read from the
                standing approval and the sighting, so there is no stored state to go stale.
    """

    added: list[str]
    changed: list[str]
    failure: None | str
    fingerprint: None | str
    name: str
    observed_skills: int
    pin_changed: bool
    pin_mechanism: str
    removed: list[str]
    state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        added = self.added

        changed = self.changed

        failure: None | str
        failure = self.failure

        fingerprint: None | str
        fingerprint = self.fingerprint

        name = self.name

        observed_skills = self.observed_skills

        pin_changed = self.pin_changed

        pin_mechanism = self.pin_mechanism

        removed = self.removed

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "added": added,
                "changed": changed,
                "failure": failure,
                "fingerprint": fingerprint,
                "name": name,
                "observed_skills": observed_skills,
                "pin_changed": pin_changed,
                "pin_mechanism": pin_mechanism,
                "removed": removed,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        added = cast(list[str], d.pop("added"))

        changed = cast(list[str], d.pop("changed"))

        def _parse_failure(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        failure = _parse_failure(d.pop("failure"))

        def _parse_fingerprint(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        fingerprint = _parse_fingerprint(d.pop("fingerprint"))

        name = d.pop("name")

        observed_skills = d.pop("observed_skills")

        pin_changed = d.pop("pin_changed")

        pin_mechanism = d.pop("pin_mechanism")

        removed = cast(list[str], d.pop("removed"))

        state = d.pop("state")

        a2a_trust_view = cls(
            added=added,
            changed=changed,
            failure=failure,
            fingerprint=fingerprint,
            name=name,
            observed_skills=observed_skills,
            pin_changed=pin_changed,
            pin_mechanism=pin_mechanism,
            removed=removed,
            state=state,
        )

        a2a_trust_view.additional_properties = d
        return a2a_trust_view

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
