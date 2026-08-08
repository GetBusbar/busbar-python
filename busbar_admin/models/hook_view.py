from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hook_transport_view import HookTransportView


T = TypeVar("T", bound="HookView")


@_attrs_define
class HookView:
    """A hook definition in the registry read (`GET /api/v1/admin/hooks`, `GET /api/v1/admin/hooks/{name}`): the
    plugin catalog read. Projects the DEFINITION (kind, transport, grants, ordering, stage), never a
    secret, INCLUDING the `settings:` bag, which is projected as KEY NAMES only (see
    [`HookView::settings_keys`]). `global` reports whether the hook fires on EVERY request. There is
    no `global_hooks:` config key to write: 1.5.3 deleted it, and a hook is now DEFINED once in the
    top-level `hooks:` named map (its `module:` naming the `kind: hook` plugin that backs it) and
    ATTACHED by bare name, at the reserved all-pools key `pools.hooks:`, which is what makes it
    global, or at one pool's own `hooks:` list. `groups:` and `phase:` are the config-file selection
    axes (which callers, which pipeline stages). On THIS API the same hook is written with
    `global: true`; the wire and the config file are deliberately different surfaces. Live connection
    status (`health`) is a separate endpoint. Additive-only.

        Attributes:
            at (None | str): TAP observation stage (`"request"`/`"candidate"`/`"routing"`/`"response"`), or `None` for a
                gate.
            global_ (bool): Whether this hook fires on every request (globally wired).
            kind (str): `"tap"` (fire-and-forget) or `"gate"` (fire-and-wait).
            name (str):
            on_error (str): Gate fallback on timeout/error, a CLOSED, unambiguous string union: one of the
                reserved terminals (`"weighted"` | `"reject"` | `"first"` | `"nothing"`) or the NAME of the
                fallback hook the chain continues through. Unambiguous by construction: the terminal words
                are ILLEGAL hook names on every write path (`config::RESERVED_HOOK_NAMES`), so a value in
                the terminal set is always a terminal and anything else is always a hook reference.
            priority (int): Rewrite/reject ordering key (transform-chain order + reject tie-break).
            prompt (str): Prompt access grant: `"no"` | `"ro"` | `"rw"`.
            settings_keys (list[str]): The KEY NAMES of the hook's opaque settings bag, sorted, WITHOUT their values, the
                same
                redacted projection [`NamedDefView::settings_keys`] carries, produced by the same helper.

                This used to be the bag itself, under a doc comment claiming hook settings are "never a
                secret by contract". That claim was retracted for `NamedDefView` and it is no more true here:
                a hook's settings bag is a `SecretRef` carrier by design (`hooks::HookEnv::resolve_hook_settings`
                resolves it before every configure push), and `config::secret::resolve_settings` forwards a
                non-object bag verbatim, so a literal credential is fully supported too. `GET /hooks` and
                `GET /hooks/{name}` serve this at READ-ONLY admin scope. The values are readable only where
                they are writable: the config file and the config overlay.
            timeout_ms (int): Gate decision deadline in milliseconds.
            transport (HookTransportView): The transport half of a `HookView`. As of 1.5.0 a hook is EITHER a compiled-in
                kind (no
                transport at all) or a signed `kind: hook` dlopen'd plugin (`target` = the plugin NAME, not a
                socket path or URL); the retired 1.4.x socket/webhook sidecar transports are gone.
            user (str): Caller-identity access grant: `"no"` | `"ro"`.
    """

    at: None | str
    global_: bool
    kind: str
    name: str
    on_error: str
    priority: int
    prompt: str
    settings_keys: list[str]
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

        settings_keys = self.settings_keys

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
                "settings_keys": settings_keys,
                "timeout_ms": timeout_ms,
                "transport": transport,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hook_transport_view import HookTransportView

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

        settings_keys = cast(list[str], d.pop("settings_keys"))

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
            settings_keys=settings_keys,
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
