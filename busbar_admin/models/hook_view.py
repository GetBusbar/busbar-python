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
            at (None | str): The LEGACY single-valued tap stage (`"request"`/`"candidate"`/`"routing"`/`"response"`), or
                `null`. Kept for back-compat and NOT the field to read: `null` here does NOT mean "a gate"
                and does not mean "unscoped". Every hook written in the current top-level `hooks:` grammar
                has `at: null` by construction (`config::hook_cfg_from_def` never sets it, and
                `--migrate-config` rewrites a legacy `at:` into `phase:`), so this field is `null` for
                essentially every hook a running deployment has. Read `fires_at`.
                1.6.0 owner rule: a 1.5.5 client reading this view must see this field byte-for-byte, so it
                is RESTORED alongside `phase`/`fires_at`.
            fires_at (list[str]): The RESOLVED stage set: the stages this hook ACTUALLY fires at, in pipeline order, never
                empty. This is the field that answers "when does this hook run", and it is computed by
                `config::HookCfg::resolved_stages` through the same `fires_at_stage` predicate the firing
                path uses, so it cannot disagree with runtime behavior. It reflects the frozen precedence
                (a non-empty `phase:` wins, else the legacy single `at:`, else the four core stages) without
                asking the reader to re-derive it from the two spellings above.
            global_ (bool): Whether this hook fires on every request (globally wired).
            groups (list[str]): The `groups:` CALLER SCOPE exactly as configured: the caller groups this hook fires for,
                empty meaning ALL callers (unscoped). The other half of "when does this hook run", and the
                same writable-but-unreadable gap `phase` had.
            kind (str): `"tap"` (fire-and-forget) or `"gate"` (fire-and-wait).
            name (str):
            on_error (str): Gate fallback on timeout/error, a CLOSED, unambiguous string union: one of the
                reserved terminals (`"weighted"` | `"reject"` | `"first"` | `"nothing"`) or the NAME of the
                fallback hook the chain continues through. Unambiguous by construction: the terminal words
                are ILLEGAL hook names on every write path (`config::RESERVED_HOOK_NAMES`), so a value in
                the terminal set is always a terminal and anything else is always a hook reference.
            phase (list[str]): The `phase:` STAGE LIST exactly as configured, empty when unset. The literal config echo,
                for an operator diffing what they wrote against what busbar parsed. It is NOT the effective
                answer on its own: empty means "fall back", and what it falls back TO is `at:` if set and the
                four core stages otherwise. For the effective answer read `fires_at`.
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
    fires_at: list[str]
    global_: bool
    groups: list[str]
    kind: str
    name: str
    on_error: str
    phase: list[str]
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

        fires_at = self.fires_at

        global_ = self.global_

        groups = self.groups

        kind = self.kind

        name = self.name

        on_error = self.on_error

        phase = self.phase

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
                "fires_at": fires_at,
                "global": global_,
                "groups": groups,
                "kind": kind,
                "name": name,
                "on_error": on_error,
                "phase": phase,
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
        from ..models.hook_transport_view import HookTransportView  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        at = _parse_at(d.pop("at"))

        fires_at = cast(list[str], d.pop("fires_at"))

        global_ = d.pop("global")

        groups = cast(list[str], d.pop("groups"))

        kind = d.pop("kind")

        name = d.pop("name")

        on_error = d.pop("on_error")

        phase = cast(list[str], d.pop("phase"))

        priority = d.pop("priority")

        prompt = d.pop("prompt")

        settings_keys = cast(list[str], d.pop("settings_keys"))

        timeout_ms = d.pop("timeout_ms")

        transport = HookTransportView.from_dict(d.pop("transport"))

        user = d.pop("user")

        hook_view = cls(
            at=at,
            fires_at=fires_at,
            global_=global_,
            groups=groups,
            kind=kind,
            name=name,
            on_error=on_error,
            phase=phase,
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
