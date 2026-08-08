from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConfigVersion")


@_attrs_define
class ConfigVersion:
    """One recorded config version: the metadata the versions LIST shows, plus the full hook-surface
    snapshot rollback restores. Never contains a secret (hook definitions are operator config:
    transports, grants, deadlines).

        Attributes:
            principal (str): The acting principal (audit attribution, same handle as the audit log).
            summary (str): Human summary of the mutation that produced this version (e.g. `hook.register hook:x`).
            ts (int): Unix seconds when the mutation committed.
            version (int): The `App.config_version` this snapshot corresponds to (monotonic per process).
    """

    principal: str
    summary: str
    ts: int
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        principal = self.principal

        summary = self.summary

        ts = self.ts

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "principal": principal,
                "summary": summary,
                "ts": ts,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        principal = d.pop("principal")

        summary = d.pop("summary")

        ts = d.pop("ts")

        version = d.pop("version")

        config_version = cls(
            principal=principal,
            summary=summary,
            ts=ts,
            version=version,
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
