from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.configured_settings_view import ConfiguredSettingsView


T = TypeVar("T", bound="MutatedDefView")


@_attrs_define(repr=False)
class MutatedDefView:
    """THE MUTATION RESPONSE for an upsert/settings write: the stored definition, PLUS the
    restart-required signal for boot-bound routes, planes and export instances or projections.

    `#[serde(flatten)]` keeps the definition's own fields exactly where they have always been, so the
    signal is purely ADDITIVE. Configuration values, when available, are explicitly identified as
    belonging to the installed config generation, not an acknowledgement from a running plugin.
    This is the `export:` named map's sibling of
    `PUT /config/settings`'s `reload_to_apply`/`note` pair (`handlers::reload_to_apply_fields`), which
    reports the same class of boot-frozen change for the single-value settings surface.

        Attributes:
            name (str): The instance NAME: the map key, and the token every reference site uses.
            settings_keys (list[str]): The KEY NAMES of the module's opaque settings bag, sorted, WITHOUT their values, the
                redacted projection of `settings:`. Operator/API-owned and never interpreted here, but also
                never a place a VALUE can leak from: a settings value may be a credential (see the type doc),
                and this surface is reachable at READ-ONLY admin scope. An empty bag ⇒ an empty list. The
                values are readable only where they are writable: the config file and the config overlay.
            module (str | Unset): The `module:` backing this plugin instance (a built-in name or signed-plugin name/alias).
                Omitted for definitions that do not instantiate a module, such as remote agents, and for
                an unparseable stored definition that has no string-valued module to project.
            max_admin_scope (None | str | Unset): `identity-providers` ONLY: the per-provider ADMIN CEILING (`read-only` |
                `full`). There is no
                `none` token: `Scope::parse_ceiling` rejects it, because a ceiling
                caps what a grant can reach and cannot express the absence of one.
                `None` ⇒ the definition names no ceiling, so the most restrictive default applies. Omitted
                entirely for a section that carries no ceiling.
            token_configured (bool | None | Unset): `identity-providers` ONLY: whether a `token:` secret REFERENCE is
                configured (the built-in
                `admin-tokens` operator credential). The reference itself is never projected.
            browser_login_configured (bool | None | Unset): `identity-providers` ONLY: whether a `browser_login:` block is
                configured, the presence that
                puts a button on the hosted login page.
            pin_mechanism (None | str | Unset): `agents` ONLY: which authenticity root this registration is pinned to
                (`jws_issuer_key` |
                `cert_spki` | `mtls` | `unpinned`). Projected because an operator scanning a registration
                list needs to SEE which entries have no root; a mechanism that could only be discovered by
                reading the config file is a mechanism nobody audits.
            fingerprint_pinned (bool | None | Unset): `agents` ONLY: whether an approved card FINGERPRINT is pinned yet. A
                registration with a
                root but no fingerprint is the normal state of a fresh entry awaiting approval, and it is
                the state an operator most needs to be able to see.
            reverify_ttl (None | str | Unset): `agents` ONLY: the re-verification cadence this registration carries, as
                written. The
                backend `url:` is deliberately NOT projected here: it is the real remote endpoint and is
                never client-visible.
            unparseable (None | str | Unset): Set ONLY on an entry that is STORED in the config overlay but could NOT be
                parsed into this
                section's typed config by this binary (a downgrade whose struct lost a field, a hand-edited
                overlay); the value is the parse error. Such an entry is dropped at every rebuild, so it is
                NOT live: `module`/`settings_keys` are the raw stored document's best-effort projection, not
                a resolved definition. Present so the drop is DISCOVERABLE here rather than only in a boot
                log line. Absent (and omitted from the body) for every live definition.
            reload_to_apply (list[str] | Unset): The plugin-route PATHS this mutation declared that the process cannot serve
                until it restarts,
                because the axum router registers each path once, at boot, and a config apply swaps only
                `Arc<App>`; then the plane SECTIONS it first wrote whose plane the process did not open at
                boot (a plane is opened once, at process start, when its section is configured); and export
                instances whose membership, module or projection differs from the boot-opened sink.
                Empty and omitted when this mutation leaves no boot-bound change.
            note (None | str | Unset): The operator-facing sentence for [`Self::reload_to_apply`]; omitted with it.
            configuration (ConfiguredSettingsView | None | Unset): Safe settings from the same installed configuration
                generation as the response ETag.
                This is configured intent, not proof that an asynchronous plugin refresh completed.
    """

    name: str
    settings_keys: list[str]
    module: str | Unset = UNSET
    max_admin_scope: None | str | Unset = UNSET
    token_configured: bool | None | Unset = UNSET
    browser_login_configured: bool | None | Unset = UNSET
    pin_mechanism: None | str | Unset = UNSET
    fingerprint_pinned: bool | None | Unset = UNSET
    reverify_ttl: None | str | Unset = UNSET
    unparseable: None | str | Unset = UNSET
    reload_to_apply: list[str] | Unset = UNSET
    note: None | str | Unset = UNSET
    configuration: ConfiguredSettingsView | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.configured_settings_view import ConfiguredSettingsView  # noqa: PLC0415

        name = self.name

        settings_keys = self.settings_keys

        module = self.module

        max_admin_scope: None | str | Unset
        if isinstance(self.max_admin_scope, Unset):
            max_admin_scope = UNSET
        else:
            max_admin_scope = self.max_admin_scope

        token_configured: bool | None | Unset
        if isinstance(self.token_configured, Unset):
            token_configured = UNSET
        else:
            token_configured = self.token_configured

        browser_login_configured: bool | None | Unset
        if isinstance(self.browser_login_configured, Unset):
            browser_login_configured = UNSET
        else:
            browser_login_configured = self.browser_login_configured

        pin_mechanism: None | str | Unset
        if isinstance(self.pin_mechanism, Unset):
            pin_mechanism = UNSET
        else:
            pin_mechanism = self.pin_mechanism

        fingerprint_pinned: bool | None | Unset
        if isinstance(self.fingerprint_pinned, Unset):
            fingerprint_pinned = UNSET
        else:
            fingerprint_pinned = self.fingerprint_pinned

        reverify_ttl: None | str | Unset
        if isinstance(self.reverify_ttl, Unset):
            reverify_ttl = UNSET
        else:
            reverify_ttl = self.reverify_ttl

        unparseable: None | str | Unset
        if isinstance(self.unparseable, Unset):
            unparseable = UNSET
        else:
            unparseable = self.unparseable

        reload_to_apply: list[str] | Unset = UNSET
        if not isinstance(self.reload_to_apply, Unset):
            reload_to_apply = self.reload_to_apply

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        configuration: dict[str, Any] | None | Unset
        if isinstance(self.configuration, Unset):
            configuration = UNSET
        elif isinstance(self.configuration, ConfiguredSettingsView):
            configuration = self.configuration.to_dict()
        else:
            configuration = self.configuration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "settings_keys": settings_keys,
            }
        )
        if module is not UNSET:
            field_dict["module"] = module
        if max_admin_scope is not UNSET:
            field_dict["max_admin_scope"] = max_admin_scope
        if token_configured is not UNSET:
            field_dict["token_configured"] = token_configured
        if browser_login_configured is not UNSET:
            field_dict["browser_login_configured"] = browser_login_configured
        if pin_mechanism is not UNSET:
            field_dict["pin_mechanism"] = pin_mechanism
        if fingerprint_pinned is not UNSET:
            field_dict["fingerprint_pinned"] = fingerprint_pinned
        if reverify_ttl is not UNSET:
            field_dict["reverify_ttl"] = reverify_ttl
        if unparseable is not UNSET:
            field_dict["unparseable"] = unparseable
        if reload_to_apply is not UNSET:
            field_dict["reload_to_apply"] = reload_to_apply
        if note is not UNSET:
            field_dict["note"] = note
        if configuration is not UNSET:
            field_dict["configuration"] = configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configured_settings_view import ConfiguredSettingsView  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        settings_keys = cast(list[str], d.pop("settings_keys"))

        module = d.pop("module", UNSET)

        def _parse_max_admin_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_admin_scope = _parse_max_admin_scope(d.pop("max_admin_scope", UNSET))

        def _parse_token_configured(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        token_configured = _parse_token_configured(d.pop("token_configured", UNSET))

        def _parse_browser_login_configured(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        browser_login_configured = _parse_browser_login_configured(d.pop("browser_login_configured", UNSET))

        def _parse_pin_mechanism(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pin_mechanism = _parse_pin_mechanism(d.pop("pin_mechanism", UNSET))

        def _parse_fingerprint_pinned(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        fingerprint_pinned = _parse_fingerprint_pinned(d.pop("fingerprint_pinned", UNSET))

        def _parse_reverify_ttl(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reverify_ttl = _parse_reverify_ttl(d.pop("reverify_ttl", UNSET))

        def _parse_unparseable(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unparseable = _parse_unparseable(d.pop("unparseable", UNSET))

        reload_to_apply = cast(list[str], d.pop("reload_to_apply", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        def _parse_configuration(data: object) -> ConfiguredSettingsView | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                configuration_type_0 = ConfiguredSettingsView.from_dict(data)

                return configuration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for configuration")

        configuration = _parse_configuration(d.pop("configuration", UNSET))

        mutated_def_view = cls(
            name=name,
            settings_keys=settings_keys,
            module=module,
            max_admin_scope=max_admin_scope,
            token_configured=token_configured,
            browser_login_configured=browser_login_configured,
            pin_mechanism=pin_mechanism,
            fingerprint_pinned=fingerprint_pinned,
            reverify_ttl=reverify_ttl,
            unparseable=unparseable,
            reload_to_apply=reload_to_apply,
            note=note,
            configuration=configuration,
        )

        mutated_def_view.additional_properties = d
        return mutated_def_view

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
