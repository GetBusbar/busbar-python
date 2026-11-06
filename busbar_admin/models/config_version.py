from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConfigVersion")


@_attrs_define(repr=False)
class ConfigVersion:
    """One recorded config version: the metadata the versions LIST shows, plus the full hook-surface
    snapshot rollback restores. Never contains a secret (hook definitions are operator config:
    transports, grants, deadlines).

        Attributes:
            version (int): The `App.config_version` this snapshot corresponds to (monotonic per process).
            ts (int): Unix seconds when the mutation committed.
            principal (str): The acting principal (audit attribution, same handle as the audit log).
            summary (str): Human summary of the mutation that produced this version (e.g. `hook.register hook:x`).
    """

    version: int
    ts: int
    principal: str
    summary: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        ts = self.ts

        principal = self.principal

        summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "ts": ts,
                "principal": principal,
                "summary": summary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("version")

        ts = d.pop("ts")

        principal = d.pop("principal")

        summary = d.pop("summary")

        config_version = cls(
            version=version,
            ts=ts,
            principal=principal,
            summary=summary,
        )

        config_version.additional_properties = d
        return config_version

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
