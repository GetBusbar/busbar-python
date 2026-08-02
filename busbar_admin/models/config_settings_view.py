from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigSettingsView")


@_attrs_define
class ConfigSettingsView:
    """`GET`/`PUT /config/settings` (1.5.0 full-config coverage) — the API-settable single-value config
    overlay (`root` section) and, on a PUT, the apply metadata. `settings` is the CURRENT effective
    root override (the merge of prior overlay + this request). It is overlay-persisted so it survives
    a restart WHEN a config overlay is configured (`BUSBAR_CONFIG_OVERLAY`) — a busbar with none
    applies the change live only, and `note` says so; `PUT` with `"persist": true` makes storage
    mandatory, refusing (`400`) rather than silently applying in memory when no overlay exists.
    `reload_to_apply` names the fields whose new value is DURABLY STORED but not yet LIVE: the
    process-level binds (`listen`/`admin_listen` socket, `tls`/`admin_tls` bind, `admin_insecure`) are
    read once at process start, and the durable `store` backend is reused across a hot reload — none
    can hot-swap, so they take effect on the next RESTART (or a supervisor restart), NEVER on a
    `POST /config/reload` — a reload re-reads disk and rebuilds the `App` but does not rebind sockets,
    rebuild the TLS acceptor, or re-open the store. It is always EMPTY when nothing was durably stored
    (no overlay); `note` names the affected fields instead. Everything else
    (`rate_card`/`per_request_fee`/`security`/`advanced`/`metrics`/`health`/`routing`) is LIVE on the
    swap; `limits` is live EXCEPT four boot-scoped fields (see `reload_to_apply_fields`):
    `upstream_request_timeout_secs`/`pool_max_idle_per_host`/`pool_idle_timeout_secs`, which the
    reused `UpstreamClients` only reads once at boot, and `max_inbound_concurrent`, which is baked
    once into the data router's `GlobalConcurrencyLimitLayer` at process start (a config apply swaps
    only `Arc<App>`, never the router) — two independent freezing mechanisms. `observability` is live
    EXCEPT three boot-scoped fields: `emit_server_timing` (baked into router middleware state at
    boot), `request_log_webhook_url` (seeds a process-global `OnceLock` that no-ops after the first
    `main()` call), and `otlp_url` (feeds a one-shot `tracing_subscriber` init) — none rebuilt by an
    apply.

        Attributes:
            applied (bool): `true` on a PUT that stored + swapped; `false` on a GET (a pure read).
            config_version (int):
            settings (Any): The current effective root-section overlay (only the fields the operator has set; base
                `config.yaml` stands for the rest). An arbitrary JSON object (the `RootSettings` projection).
            note (None | str | Unset): A human note describing the live-vs-reload split (absent on a GET).
            reload_to_apply (list[str] | Unset): Fields that were stored durably but are RESTART-TO-APPLY: a socket rebind,
                a TLS acceptor
                build and a store open all happen once at process start, so a `POST /config/reload` does NOT
                make them live — `POST /restart` (or a supervisor restart) does. Empty when the PUT touched
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
