from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NamedDefView")


@_attrs_define
class NamedDefView:
    """ONE definition of ONE 1.5.3 named-DEFINITION map: the read shape of the GENERIC named-map CRUD
    (`GET /api/v1/admin/identity-providers[/{name}]`, `GET /api/v1/admin/export[/{name}]`, and
    `tools:`/`agents:` when they land).

    Deliberately ONE view for every section rather than one per kind: the sections share the frozen
    `{module, settings}` spine and differ only by optional kind-specific fields, which are
    `skip_serializing_if`-omitted for a section that has none. So `/export` serves exactly
    `{name, module, settings_keys}` while `/identity-providers` additionally carries its ceiling,
    and a new section adds fields here (additive) instead of a parallel view + a parallel handler.

    SECRETS ARE NEVER PROJECTED, by construction, and that claim covers the `settings:` bag too,
    which is why this view carries `settings_keys` and NOT the bag itself. A `token:` is a SECRET
    REFERENCE collapsed to a boolean, and the module's opaque settings are a bag an operator
    legitimately puts a credential VALUE in (an OIDC `client_secret`, a webhook `auth_header` value),
    so projecting it verbatim would hand every READ-ONLY admin credential the deployment's secrets
    through `GET /identity-providers/{name}` / `GET /export/{name}`. Projecting the KEY NAMES keeps
    the introspection the read surface exists for ("what is configured here?") with no field a value
    could ride out on: the same discipline `token_configured` already applies to the reference.

        Attributes:
            module (str): The `module:` backing this instance (a built-in name or a signed-plugin name/alias).
            name (str): The instance NAME: the map key, and the token every reference site uses.
            settings_keys (list[str]): The KEY NAMES of the module's opaque settings bag, sorted, WITHOUT their values, the
                redacted projection of `settings:`. Operator/API-owned and never interpreted here, but also
                never a place a VALUE can leak from: a settings value may be a credential (see the type doc),
                and this surface is reachable at READ-ONLY admin scope. An empty bag ⇒ an empty list. The
                values are readable only where they are writable: the config file and the config overlay.
            browser_login_configured (bool | None | Unset): `identity-providers` ONLY: whether a `browser_login:` block is
                configured, the presence that
                puts a button on the hosted login page.
            max_admin_scope (None | str | Unset): `identity-providers` ONLY: the per-provider ADMIN CEILING (`none` | `read-
                only` | `full`).
                `None` ⇒ the definition names none, so the most restrictive default applies. Omitted entirely
                for a section that carries no ceiling.
            token_configured (bool | None | Unset): `identity-providers` ONLY: whether a `token:` secret REFERENCE is
                configured (the built-in
                `admin-tokens` operator credential). The reference itself is never projected.
            unparseable (None | str | Unset): Set ONLY on an entry that is STORED in the config overlay but could NOT be
                parsed into this
                section's typed config by this binary (a downgrade whose struct lost a field, a hand-edited
                overlay); the value is the parse error. Such an entry is dropped at every rebuild, so it is
                NOT live: `module`/`settings_keys` are the raw stored document's best-effort projection, not
                a resolved definition. Present so the drop is DISCOVERABLE here rather than only in a boot
                log line. Absent (and omitted from the body) for every live definition.
    """

    module: str
    name: str
    settings_keys: list[str]
    browser_login_configured: bool | None | Unset = UNSET
    max_admin_scope: None | str | Unset = UNSET
    token_configured: bool | None | Unset = UNSET
    unparseable: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        module = self.module

        name = self.name

        settings_keys = self.settings_keys

        browser_login_configured: bool | None | Unset
        if isinstance(self.browser_login_configured, Unset):
            browser_login_configured = UNSET
        else:
            browser_login_configured = self.browser_login_configured

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

        unparseable: None | str | Unset
        if isinstance(self.unparseable, Unset):
            unparseable = UNSET
        else:
            unparseable = self.unparseable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "module": module,
                "name": name,
                "settings_keys": settings_keys,
            }
        )
        if browser_login_configured is not UNSET:
            field_dict["browser_login_configured"] = browser_login_configured
        if max_admin_scope is not UNSET:
            field_dict["max_admin_scope"] = max_admin_scope
        if token_configured is not UNSET:
            field_dict["token_configured"] = token_configured
        if unparseable is not UNSET:
            field_dict["unparseable"] = unparseable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        module = d.pop("module")

        name = d.pop("name")

        settings_keys = cast(list[str], d.pop("settings_keys"))

        def _parse_browser_login_configured(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        browser_login_configured = _parse_browser_login_configured(d.pop("browser_login_configured", UNSET))

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

        def _parse_unparseable(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unparseable = _parse_unparseable(d.pop("unparseable", UNSET))

        named_def_view = cls(
            module=module,
            name=name,
            settings_keys=settings_keys,
            browser_login_configured=browser_login_configured,
            max_admin_scope=max_admin_scope,
            token_configured=token_configured,
            unparseable=unparseable,
        )

        named_def_view.additional_properties = d
        return named_def_view

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
