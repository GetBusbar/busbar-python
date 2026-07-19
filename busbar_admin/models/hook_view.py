from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hook_transport_view import HookTransportView
    from ..models.hook_view_settings import HookViewSettings


T = TypeVar("T", bound="HookView")


@_attrs_define
class HookView:
    """A hook definition in the registry read (`GET /api/v1/admin/hooks`, `GET /api/v1/admin/hooks/{name}`) — the
    plugin catalog read. Projects the DEFINITION (kind, transport, grants, ordering, stage), never a
    secret. `global` reports whether the hook fires on every request (named in `global_hooks:` or
    declared `global: true`). Live connection status (`health`) is a separate endpoint. Additive-only.

        Attributes:
            at (None | str): TAP observation stage (`"request"`/`"route"`/`"attempt"`/`"completion"`), or `None` for a gate.
            global_ (bool): Whether this hook fires on every request (globally wired).
            kind (str): `"tap"` (fire-and-forget) or `"gate"` (fire-and-wait).
            name (str):
            on_error (str): Gate fallback on timeout/error — a CLOSED, unambiguous string union (audit #8): one of the
                reserved terminals (`"weighted"` | `"reject"` | `"first"` | `"nothing"`) or the NAME of the
                fallback hook the chain continues through. Unambiguous by construction: the terminal words
                are ILLEGAL hook names on every write path (`config::RESERVED_HOOK_NAMES`), so a value in
                the terminal set is always a terminal and anything else is always a hook reference.
            priority (int): Rewrite/reject ordering key (transform-chain order + reject tie-break).
            prompt (str): Prompt access grant: `"no"` | `"ro"` | `"rw"`.
            settings (HookViewSettings): The hook's opaque settings map (operator/API-owned; pushed via the configure wire).
                Never
                interpreted by busbar; never a secret by contract (hook settings are operator config).
            timeout_ms (int): Gate decision deadline in milliseconds.
            transport (HookTransportView): The transport half of a `HookView`: which wire the hook speaks and its target
                (socket path or
                webhook URL — operator config, not a secret). Exactly one of `socket`/`webhook` is set.
            user (str): Caller-identity access grant: `"no"` | `"ro"`.
    """

    at: None | str
    global_: bool
    kind: str
    name: str
    on_error: str
    priority: int
    prompt: str
    settings: HookViewSettings
    timeout_ms: int
    transport: HookTransportView
    user: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at: None | str
        at = self.at

        global_ = self.global_

        kind = self.kind

        name = self.name

        on_error = self.on_error

        priority = self.priority

        prompt = self.prompt

        settings = self.settings.to_dict()

        timeout_ms = self.timeout_ms

        transport = self.transport.to_dict()

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "at": at,
                "global": global_,
                "kind": kind,
                "name": name,
                "on_error": on_error,
                "priority": priority,
                "prompt": prompt,
                "settings": settings,
                "timeout_ms": timeout_ms,
                "transport": transport,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hook_transport_view import HookTransportView
        from ..models.hook_view_settings import HookViewSettings

        d = dict(src_dict)

        def _parse_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        at = _parse_at(d.pop("at"))

        global_ = d.pop("global")

        kind = d.pop("kind")

        name = d.pop("name")

        on_error = d.pop("on_error")

        priority = d.pop("priority")

        prompt = d.pop("prompt")

        settings = HookViewSettings.from_dict(d.pop("settings"))

        timeout_ms = d.pop("timeout_ms")

        transport = HookTransportView.from_dict(d.pop("transport"))

        user = d.pop("user")

        hook_view = cls(
            at=at,
            global_=global_,
            kind=kind,
            name=name,
            on_error=on_error,
            priority=priority,
            prompt=prompt,
            settings=settings,
            timeout_ms=timeout_ms,
            transport=transport,
            user=user,
        )

        hook_view.additional_properties = d
        return hook_view

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
