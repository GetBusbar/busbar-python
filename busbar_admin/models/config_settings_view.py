from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.config_settings_view_desired_status import ConfigSettingsViewDesiredStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_settings_view_configuration import ConfigSettingsViewConfiguration


T = TypeVar("T", bound="ConfigSettingsView")


@_attrs_define(repr=False)
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
    only `Arc<App>`, never the router): two independent freezing mechanisms.
    The optional `limits.datagram_line_memory_bytes` setting is off by default. Setting it to
    a positive integer enables a retained-capacity limit for new datagram LINE pairings; null
    disables it. Existing connections retain their chosen limit. Exhaustion closes the affected
    connection. The limit counts retained requested capacity across both directions, queued output
    ownership and metadata, not process RSS or allocator overhead.
    There is NO
    `observability` section here, and no `metrics` one either: 1.5.3 DELETED both from the config
    grammar, and `RootSettings` (what this endpoint projects) carries neither field: a PUT naming
    `observability` is a loud `400` (`deny_unknown_fields`), never a silent no-op. All telemetry
    egress uses the named `export:` map. Export definitions and explicit supported field projections
    are authored through the named exporter routes or source-fenced configuration document edits.
    Module-carried streams, produced fields and required pinned fields are published in the export
    form schema; lifecycle and restart requirements remain explicit in mutation responses.
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
            reload_to_apply (list[str] | Unset): Fields that were stored durably but are RESTART-TO-APPLY: a socket rebind,
                a TLS acceptor
                build and a store open all happen once at process start, so a `POST /config/reload` does NOT
                make them live; `POST /restart` (or a supervisor restart) does. Empty when the PUT touched
                only live-swappable fields (or on a GET). The field NAME is frozen wire; only this description
                changed.
            note (None | str | Unset): A human note describing the live-vs-reload split (absent on a GET).
            configuration (ConfigSettingsViewConfiguration | Unset): Sanitized values captured from the installed config
                generation, bound to the response ETag; configured does not mean physically active.
            settings_source (str | Unset): desired_root_overlay on GET; settings never represents the full applied
                configuration.
            desired_revision (None | str | Unset): SHA256 content revision of the exact verified desired Store document;
                independent of the process-local config_version.
            desired_status (ConfigSettingsViewDesiredStatus | Unset):
    """

    applied: bool
    config_version: int
    settings: Any
    reload_to_apply: list[str] | Unset = UNSET
    note: None | str | Unset = UNSET
    configuration: ConfigSettingsViewConfiguration | Unset = UNSET
    settings_source: str | Unset = UNSET
    desired_revision: None | str | Unset = UNSET
    desired_status: ConfigSettingsViewDesiredStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied = self.applied

        config_version = self.config_version

        settings = self.settings

        reload_to_apply: list[str] | Unset = UNSET
        if not isinstance(self.reload_to_apply, Unset):
            reload_to_apply = self.reload_to_apply

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        settings_source = self.settings_source

        desired_revision: None | str | Unset
        if isinstance(self.desired_revision, Unset):
            desired_revision = UNSET
        else:
            desired_revision = self.desired_revision

        desired_status: str | Unset = UNSET
        if not isinstance(self.desired_status, Unset):
            desired_status = self.desired_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applied": applied,
                "config_version": config_version,
                "settings": settings,
            }
        )
        if reload_to_apply is not UNSET:
            field_dict["reload_to_apply"] = reload_to_apply
        if note is not UNSET:
            field_dict["note"] = note
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if settings_source is not UNSET:
            field_dict["settings_source"] = settings_source
        if desired_revision is not UNSET:
            field_dict["desired_revision"] = desired_revision
        if desired_status is not UNSET:
            field_dict["desired_status"] = desired_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_settings_view_configuration import ConfigSettingsViewConfiguration  # noqa: PLC0415

        d = dict(src_dict)
        applied = d.pop("applied")

        config_version = d.pop("config_version")

        settings = d.pop("settings")

        reload_to_apply = cast(list[str], d.pop("reload_to_apply", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        _configuration = d.pop("configuration", UNSET)
        configuration: ConfigSettingsViewConfiguration | Unset
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = ConfigSettingsViewConfiguration.from_dict(_configuration)

        settings_source = d.pop("settings_source", UNSET)

        def _parse_desired_revision(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        desired_revision = _parse_desired_revision(d.pop("desired_revision", UNSET))

        _desired_status = d.pop("desired_status", UNSET)
        desired_status: ConfigSettingsViewDesiredStatus | Unset
        if isinstance(_desired_status, Unset):
            desired_status = UNSET
        else:
            desired_status = ConfigSettingsViewDesiredStatus(_desired_status)

        config_settings_view = cls(
            applied=applied,
            config_version=config_version,
            settings=settings,
            reload_to_apply=reload_to_apply,
            note=note,
            configuration=configuration,
            settings_source=settings_source,
            desired_revision=desired_revision,
            desired_status=desired_status,
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
