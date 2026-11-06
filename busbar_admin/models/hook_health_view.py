from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hook_transport_view import HookTransportView


T = TypeVar("T", bound="HookHealthView")


@_attrs_define(repr=False)
class HookHealthView:
    """The live health of one hook's transport (`GET /api/v1/admin/hooks/{name}/health`). Checks
    whether the hook resolves to a LOADED `kind: hook` plugin in the process's plugin registry;
    this is a plugin-LOAD status check, not a network reachability probe: it never opens a
    connection, and it cannot tell you whether a `kind: hook` plugin's own configured external
    endpoint (e.g. `busbar-webrequest-hook`'s `settings.url`) is actually reachable, only that the
    plugin itself is loaded. Never fires the hook. Additive-only.

        Attributes:
            name (str):
            transport (HookTransportView): The transport half of a `HookView`. As of 1.5.0 a hook is EITHER a compiled-in
                kind (no
                transport at all) or a signed `kind: hook` dlopen'd plugin (`target` = the plugin NAME, not a
                socket path or URL); the retired 1.4.x socket/webhook sidecar transports are gone.
            reachable (bool | None): `Some(true)` = resolves to a loaded `kind: hook` plugin; `Some(false)` = it does not
                (wrong kind, or not installed/loaded), always `Some`, never `None`, as of 1.5.0's
                in-process plugin model.
            detail (None | str): A short human note on the resolution (why `false`, or the resolved plugin's kind). Never a
                secret.
    """

    name: str
    transport: HookTransportView
    reachable: bool | None
    detail: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        transport = self.transport.to_dict()

        reachable: bool | None
        reachable = self.reachable

        detail: None | str
        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "transport": transport,
                "reachable": reachable,
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hook_transport_view import HookTransportView  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        transport = HookTransportView.from_dict(d.pop("transport"))

        def _parse_reachable(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        reachable = _parse_reachable(d.pop("reachable"))

        def _parse_detail(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        detail = _parse_detail(d.pop("detail"))

        hook_health_view = cls(
            name=name,
            transport=transport,
            reachable=reachable,
            detail=detail,
        )

        hook_health_view.additional_properties = d
        return hook_health_view

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
