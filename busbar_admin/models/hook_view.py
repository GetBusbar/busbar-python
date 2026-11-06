from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hook_transport_view import HookTransportView


T = TypeVar("T", bound="HookView")


@_attrs_define(repr=False)
class HookView:
    """A hook definition in the registry read (`GET /api/v1/admin/hooks`, `GET /api/v1/admin/hooks/{name}`): the
    plugin catalog read. Projects the DEFINITION (kind, transport, grants, ordering, stage), never a
    secret, INCLUDING the `settings:` bag, which is projected as KEY NAMES only (see
    [`HookView::settings_keys`]). `global` reports whether the hook fires on EVERY request. There is
    no `global_hooks:` config key to write: 1.5.3 deleted it, and a hook is now DEFINED once in the
    top-level `hooks:` named map (its `module:` naming the `kind: hook` plugin that backs it) and
    ATTACHED by bare name, at the reserved all-pools key `pools.hooks:`, which is what makes it
    global, or at one pool's own `hooks:` list. On THIS API the same hook is written with
    `global: true`; the wire and the config file are deliberately different surfaces. Live connection
    status (`health`) is a separate endpoint. Additive-only.

    `groups:` and `phase:` are the config-file SELECTION axes (which callers, which pipeline stages),
    and this view used to omit both. That was not a decision to keep them file-only: both are
    WRITABLE over this API (`POST`/`PUT /hooks` deserialize `config::HookCfg` verbatim, which is the
    documented "paste a `hooks:` entry" contract), so omitting them made a field an operator can set
    through the API one they could not read back through it. `groups` and the stage pair
    (`phase` + `fires_at`) close that.

        Attributes:
            name (str):
            kind (str): `"tap"` (fire-and-forget) or `"gate"` (fire-and-wait).
            transport (HookTransportView): The transport half of a `HookView`. As of 1.5.0 a hook is EITHER a compiled-in
                kind (no
                transport at all) or a signed `kind: hook` dlopen'd plugin (`target` = the plugin NAME, not a
                socket path or URL); the retired 1.4.x socket/webhook sidecar transports are gone.
            prompt (str): Prompt access grant: `"no"` | `"ro"` | `"rw"`.
            user (str): Caller-identity access grant: `"no"` | `"ro"`.
            priority (int): Rewrite/reject ordering key (transform-chain order + reject tie-break).
            on_error (str): Gate fallback on timeout/error, a CLOSED, unambiguous string union: one of the
                reserved terminals (`"weighted"` | `"reject"` | `"first"` | `"nothing"`) or the NAME of the
                fallback hook the chain continues through. Unambiguous by construction: the terminal words
                are ILLEGAL hook names on every write path (`config::RESERVED_HOOK_NAMES`), so a value in
                the terminal set is always a terminal and anything else is always a hook reference.
            on_empty (None | str): Configured empty-intersection fallback: `"weighted"` | `"reject"` | `"first"`.
                `null` preserves an omitted override, whose runtime default is fail-closed.
            signals (list[str]): Requested signal catalog names, in configured order.
            timeout_ms (int): Gate decision deadline in milliseconds.
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
            global_ (bool): Whether this hook fires on every request (globally wired).
            default (bool): Whether this hook replaces the default ordering hook for pools with no named base.
            phase (list[str]): The canonical configured stage list. Empty selects the fixed core stages.
            fires_at (list[str]): The effective stage set in pipeline order, computed by the runtime firing predicate.
            groups (list[str]): The `groups:` CALLER SCOPE exactly as configured: the caller groups this hook fires for,
                empty meaning ALL callers (unscoped). The other half of "when does this hook run", and the
                same writable-but-unreadable gap `phase` had.
    """

    name: str
    kind: str
    transport: HookTransportView
    prompt: str
    user: str
    priority: int
    on_error: str
    on_empty: None | str
    signals: list[str]
    timeout_ms: int
    settings_keys: list[str]
    global_: bool
    default: bool
    phase: list[str]
    fires_at: list[str]
    groups: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        kind = self.kind

        transport = self.transport.to_dict()

        prompt = self.prompt

        user = self.user

        priority = self.priority

        on_error = self.on_error

        on_empty: None | str
        on_empty = self.on_empty

        signals = self.signals

        timeout_ms = self.timeout_ms

        settings_keys = self.settings_keys

        global_ = self.global_

        default = self.default

        phase = self.phase

        fires_at = self.fires_at

        groups = self.groups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "kind": kind,
                "transport": transport,
                "prompt": prompt,
                "user": user,
                "priority": priority,
                "on_error": on_error,
                "on_empty": on_empty,
                "signals": signals,
                "timeout_ms": timeout_ms,
                "settings_keys": settings_keys,
                "global": global_,
                "default": default,
                "phase": phase,
                "fires_at": fires_at,
                "groups": groups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hook_transport_view import HookTransportView  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        kind = d.pop("kind")

        transport = HookTransportView.from_dict(d.pop("transport"))

        prompt = d.pop("prompt")

        user = d.pop("user")

        priority = d.pop("priority")

        on_error = d.pop("on_error")

        def _parse_on_empty(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        on_empty = _parse_on_empty(d.pop("on_empty"))

        signals = cast(list[str], d.pop("signals"))

        timeout_ms = d.pop("timeout_ms")

        settings_keys = cast(list[str], d.pop("settings_keys"))

        global_ = d.pop("global")

        default = d.pop("default")

        phase = cast(list[str], d.pop("phase"))

        fires_at = cast(list[str], d.pop("fires_at"))

        groups = cast(list[str], d.pop("groups"))

        hook_view = cls(
            name=name,
            kind=kind,
            transport=transport,
            prompt=prompt,
            user=user,
            priority=priority,
            on_error=on_error,
            on_empty=on_empty,
            signals=signals,
            timeout_ms=timeout_ms,
            settings_keys=settings_keys,
            global_=global_,
            default=default,
            phase=phase,
            fires_at=fires_at,
            groups=groups,
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
