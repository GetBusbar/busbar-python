from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PluginView")


@_attrs_define
class PluginView:
    """One plugin in the plugin catalog (`GET /api/v1/admin/plugins?type=`). A plugin is either
    COMPILED-IN (baked into the binary, feature-gated — provably removable via `--no-default-features`)
    or EXTERNAL (registered at runtime over socket/webhook). `active` is `Some(true/false)` where
    activation is tracked (auth modules: in the chain?; external hooks: configured = true) and `None`
    where it is a per-pool concern not summarized here (compiled-in ranking policies). Additive-only.

        Attributes:
            active (bool | None): Whether the plugin is currently active, where tracked; `None` when activation is not
                summarized
                at this level.
            loader (str): `"compiled-in"` or `"external"`.
            name (str):
            target (None | str): For an external plugin, its transport target (socket path / webhook URL). `None` for
                compiled-in.
            type_ (str): `"auth"` or `"hooks"` — the plugin TYPE (each a distinct engine contract).
    """

    active: bool | None
    loader: str
    name: str
    target: None | str
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active: bool | None
        active = self.active

        loader = self.loader

        name = self.name

        target: None | str
        target = self.target

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "loader": loader,
                "name": name,
                "target": target,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_active(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        active = _parse_active(d.pop("active"))

        loader = d.pop("loader")

        name = d.pop("name")

        def _parse_target(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target = _parse_target(d.pop("target"))

        type_ = d.pop("type")

        plugin_view = cls(
            active=active,
            loader=loader,
            name=name,
            target=target,
            type_=type_,
        )

        plugin_view.additional_properties = d
        return plugin_view

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
