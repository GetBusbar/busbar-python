from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.config_version_detail_view_hooks import ConfigVersionDetailViewHooks


T = TypeVar("T", bound="ConfigVersionDetailView")


@_attrs_define
class ConfigVersionDetailView:
    """`GET /config/versions/{v}` — one retained config version WITH its full hook-surface snapshot
    (projected through the wire `HookView`, keyed by hook name) and the global wiring at that version.

        Attributes:
            global_hooks (list[str]):
            hooks (ConfigVersionDetailViewHooks):
            principal (str):
            summary (str):
            ts (int):
            version (int):
    """

    global_hooks: list[str]
    hooks: ConfigVersionDetailViewHooks
    principal: str
    summary: str
    ts: int
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        global_hooks = self.global_hooks

        hooks = self.hooks.to_dict()

        principal = self.principal

        summary = self.summary

        ts = self.ts

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "global_hooks": global_hooks,
                "hooks": hooks,
                "principal": principal,
                "summary": summary,
                "ts": ts,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_version_detail_view_hooks import ConfigVersionDetailViewHooks

        d = dict(src_dict)
        global_hooks = cast(list[str], d.pop("global_hooks"))

        hooks = ConfigVersionDetailViewHooks.from_dict(d.pop("hooks"))

        principal = d.pop("principal")

        summary = d.pop("summary")

        ts = d.pop("ts")

        version = d.pop("version")

        config_version_detail_view = cls(
            global_hooks=global_hooks,
            hooks=hooks,
            principal=principal,
            summary=summary,
            ts=ts,
            version=version,
        )

        config_version_detail_view.additional_properties = d
        return config_version_detail_view

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
