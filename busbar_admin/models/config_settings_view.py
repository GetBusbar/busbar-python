from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigSettingsView")


@_attrs_define
class ConfigSettingsView:
    """`GET`/`PUT /config/settings` (1.5.0 full-config coverage): the API-settable single-value config
    overlay (`root` section) and, on a PUT, the apply metadata. `settings` is the CURRENT effective
    root override (the merge of prior overlay + this request). It is overlay-persisted so it survives
    a restart. 1.5.3: a MUTABLE config always has a writable `config.overlay` backend (the boot
    invariant), so a successful PUT is ALWAYS durable; a LOCKED config (`config.locked: true`) refuses
    the PUT (`400`) instead of applying it in memory only; the silent-loss outcome is gone.
    `reload_to_apply` names the fields whose new value is DURABLY STORED but not yet LIVE: the
    process-level binds (`listen`/`admin_listen` socket, `tls`/`admin_tls` bind, and the
    `admin_require_mtls` boot-guard) are read once at process start, and the durable `store` backend
    is reused across a hot reload; none can hot-swap, so they take effect on the next RESTART (or a
    supervisor restart), NEVER on a
    `POST /config/reload`: a reload re-reads disk and rebuilds the `App` but does not rebind sockets,
    rebuild the TLS acceptor, or re-open the store. It is always EMPTY when nothing was durably stored
    (no overlay); `note` names the affected fields instead. Everything else
    (`rate_card`/`per_request_fee`/`security`/`health`/`routing`) is LIVE on the swap;
    `limits` is live EXCEPT four boot-scoped fields (see `reload_to_apply_fields`):
    `upstream_request_timeout_secs`/`pool_max_idle_per_host`/`pool_idle_timeout_secs`, which the
    reused `UpstreamClients` only reads once at boot, and `max_inbound_concurrent`, which is baked
    once into the data router's `GlobalConcurrencyLimitLayer` at process start (a config apply swaps
    only `Arc<App>`, never the router): two independent freezing mechanisms. There is NO
    `observability` section here, and no `metrics` one either: 1.5.3 DELETED both from the config
    grammar, and `RootSettings` (what this endpoint projects) carries neither field: a PUT naming
    `observability` is a loud `400` (`deny_unknown_fields`), never a silent no-op. All telemetry
    egress is now `export:`, a NAMED MAP of exporter instances that this endpoint does not reach at
    all: it is edited in `config.yaml` and made live by a plugin reload, not by `PUT /config/settings`.
    Each `export:` entry is keyed by an operator-chosen instance name and carries a `module:` naming
    the exporter plus a `settings:` bag that module validates, and MAY carry a `streams:`
    subscription list. The built-in modules are `prometheus` (carries the `metrics` stream), `otlp`
    (`traces`), and `request-log-webhook` + `request-log-file` (`logs`); subscribing an instance to a
    stream its module does not carry is rejected rather than silently delivering nothing. An entry
    MAY also carry a `fields:` projection, but do NOT plan on it in 1.5.3: it is parsed and enforced
    yet unreachable with every built-in module, because each stream they carry has a pinned field
    that has no producer yet, so any `fields:` on them is rejected. Omit it and receive the stream's
    produced default set.
    `advanced` is live EXCEPT `response_headers`: `response_headers.server_timing` is
    baked into router middleware state at boot (same "config apply swaps `Arc<App>`, never the
    router" freezing as `max_inbound_concurrent`) and `response_headers.route_policy` seeds a
    process-global `OnceLock`; neither is rebuilt by an apply.

        Attributes:
            applied (bool): `true` on a PUT that stored + swapped; `false` on a GET (a pure read).
            config_version (int):
            settings (Any): The current effective root-section overlay (only the fields the operator has set; base
                `config.yaml` stands for the rest). An arbitrary JSON object (the `RootSettings` projection),
                REDACTED by `service::redact_settings_bags`: every opaque `settings:` bag inside it (today
                `store.settings`, whose `url` is a credential in busbar's own docs) appears as
                `settings_keys`: sorted key names, no values. Same on the GET and on the PUT echo.

                This field NAME is frozen wire and is the response ENVELOPE member, not a plugin settings
                bag; the redaction applies to the bags nested INSIDE it.
            note (None | str | Unset): A human note describing the live-vs-reload split (absent on a GET).
            reload_to_apply (list[str] | Unset): Fields that were stored durably but are RESTART-TO-APPLY: a socket rebind,
                a TLS acceptor
                build and a store open all happen once at process start, so a `POST /config/reload` does NOT
                make them live; `POST /restart` (or a supervisor restart) does. Empty when the PUT touched
                only live-swappable fields (or on a GET). The field NAME is frozen wire; only this description
                changed.
    """

    applied: bool
    config_version: int
    settings: Any
    note: None | str | Unset = UNSET
    reload_to_apply: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied = self.applied

        config_version = self.config_version

        settings = self.settings

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        reload_to_apply: list[str] | Unset = UNSET
        if not isinstance(self.reload_to_apply, Unset):
            reload_to_apply = self.reload_to_apply

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applied": applied,
                "config_version": config_version,
                "settings": settings,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note
        if reload_to_apply is not UNSET:
            field_dict["reload_to_apply"] = reload_to_apply

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        applied = d.pop("applied")

        config_version = d.pop("config_version")

        settings = d.pop("settings")

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        reload_to_apply = cast(list[str], d.pop("reload_to_apply", UNSET))

        config_settings_view = cls(
            applied=applied,
            config_version=config_version,
            settings=settings,
            note=note,
            reload_to_apply=reload_to_apply,
        )

        config_settings_view.additional_properties = d
        return config_settings_view

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
