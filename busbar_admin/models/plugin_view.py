from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginView")


@_attrs_define
class PluginView:
    """One plugin in the plugin catalog (`GET /api/v1/admin/plugins?type=`). A plugin is either
    COMPILED-IN (baked into the binary, feature-gated — provably removable via `--no-default-features`)
    or a signed DYNAMIC-LIBRARY plugin (a loadable `.so`/`.dll`/`.dylib`, dlopen'd over the signed
    plugin ABI — this covers `auth`, `hooks`, and `store` plugin kinds alike as of 1.5.0; the
    retired 1.4.x socket/webhook "external" transport is gone). `active` is `Some(true/false)`
    where activation is tracked (auth modules: in the chain?; hook plugins: configured = true;
    dynamic store: the configured `store.module`) and `None` where it is a per-pool concern not
    summarized here (compiled-in ranking policies). Additive-only.

        Attributes:
            active (bool | None): Whether the plugin is currently active, where tracked; `None` when activation is not
                summarized
                at this level.
            has_schema (bool): `true` iff `GET /plugins/{file}/schema` would resolve this row's `file` to a manifest that
                declares `settings_schema` at all — i.e. iff `schema_url` below is non-null — so a plugin
                catalog can render which rows are configurable in one list call instead of a fetch per row
                (E-003). Mirrors `schema_url.is_some()`; kept as its own boolean rather than requiring the
                caller to null-check `schema_url` for the same fact. `false` for compiled-in/external rows
                (no manifest to carry a schema) and for a dynamic-library row whose manifest never set
                `settings_schema`. Additive.
            loader (str): `"compiled-in"` or `"plugin"` (a dlopen'd dynamic-library plugin — auth, hook, and store
                kinds alike as of 1.5.0's signed plugin ABI).
            name (str):
            target (None | str): For a dynamic-library plugin, its NAME (not a socket path or URL — the retired 1.4.x
                transport target). `None` for compiled-in.
            type_ (str): `"auth"`, `"hooks"`, or `"store"` — the plugin TYPE (each a distinct engine contract).
            error (None | str | Unset): Why a dynamic-library plugin did not validate (`valid: false`) — a short, secret-
                free reason.
            file (None | str | Unset): The artifact FILENAME in `plugins.dir` — the `{file}` path segment `DELETE
                /plugins/{file}` and `GET /plugins/{file}/schema` key off (E-003: a list row previously
                carried no field a client could feed straight back into either sibling endpoint; `target`
                is documented as the manifest NAME, not necessarily the on-disk filename, and is not a
                reliable substitute). `None` for compiled-in/external rows, which have no backing artifact
                to name. Additive; existing consumers reading only the pre-1.5.1 fields are unaffected.
            interface_version (int | None | Unset): The store C-ABI (`interface_version`) the manifest declares (dynamic-
                library plugins with a
                manifest). Operator-facing name for the "ABI" the engine speaks.
            publisher (None | str | Unset): The manifest's declared publisher (dynamic-library plugins with a manifest).
            schema_error (None | str | Unset): A manifest that SET `settings_schema` but whose value fails to parse
                (question #3's round-4
                correction, carried onto the list row too) — distinct from a manifest that never set the
                field at all (`schema_url: null`, this field also `None`). `schema_url` stays non-null in
                this case; the operator sees the row is degraded from the list alone, before ever following
                the URL.
            schema_url (None | str | Unset): Server-resolved path to this plugin's `GET /plugins/{name}/schema` endpoint
                (questions
                #10/#11 of plugin-settings-schema-SPEC.md) — ALWAYS a relative path under the admin origin
                (the client MUST reject an absolute/cross-origin value rather than fetch it; this endpoint
                only ever emits the admin-prefixed relative form, never anything else). Non-null whenever the
                manifest declared a `settings_schema` AT ALL, even if it's unparseable (following it then
                surfaces `schema_error` — question #11, round-8 correction: a present-but-corrupt schema is a
                worse, distinct condition from "no schema declared", never folded into the same `null`).
                `null` for a compiled-in/external row (no manifest to carry a schema at all) and for any
                dynamic-library row whose manifest never set `settings_schema`.
            trust (None | str | Unset): The server-side trust verdict for a dynamic-library plugin, re-evaluated against the
                running
                `plugins.trust` posture: `"trusted"` (signed by an allowlisted publisher), `"unverified"`
                (loaded but not verified — the posture permits it), or `"rejected"` (the `halt` posture would
                refuse it). `None` for compiled-in/external.
            valid (bool | None | Unset): For a dynamic-library plugin: whether the library validated as a busbar store
                plugin the engine
                can load (ABI handshake). `None` for compiled-in/external.
            version (None | str | Unset): The plugin's semantic version, from its signed sidecar manifest (dynamic-library
                plugins only).
                `None` for compiled-in/external, or a dynamic plugin with no/invalid manifest.
    """

    active: bool | None
    has_schema: bool
    loader: str
    name: str
    target: None | str
    type_: str
    error: None | str | Unset = UNSET
    file: None | str | Unset = UNSET
    interface_version: int | None | Unset = UNSET
    publisher: None | str | Unset = UNSET
    schema_error: None | str | Unset = UNSET
    schema_url: None | str | Unset = UNSET
    trust: None | str | Unset = UNSET
    valid: bool | None | Unset = UNSET
    version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active: bool | None
        active = self.active

        has_schema = self.has_schema

        loader = self.loader

        name = self.name

        target: None | str
        target = self.target

        type_ = self.type_

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        file: None | str | Unset
        if isinstance(self.file, Unset):
            file = UNSET
        else:
            file = self.file

        interface_version: int | None | Unset
        if isinstance(self.interface_version, Unset):
            interface_version = UNSET
        else:
            interface_version = self.interface_version

        publisher: None | str | Unset
        if isinstance(self.publisher, Unset):
            publisher = UNSET
        else:
            publisher = self.publisher

        schema_error: None | str | Unset
        if isinstance(self.schema_error, Unset):
            schema_error = UNSET
        else:
            schema_error = self.schema_error

        schema_url: None | str | Unset
        if isinstance(self.schema_url, Unset):
            schema_url = UNSET
        else:
            schema_url = self.schema_url

        trust: None | str | Unset
        if isinstance(self.trust, Unset):
            trust = UNSET
        else:
            trust = self.trust

        valid: bool | None | Unset
        if isinstance(self.valid, Unset):
            valid = UNSET
        else:
            valid = self.valid

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "has_schema": has_schema,
                "loader": loader,
                "name": name,
                "target": target,
                "type": type_,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if file is not UNSET:
            field_dict["file"] = file
        if interface_version is not UNSET:
            field_dict["interface_version"] = interface_version
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if schema_error is not UNSET:
            field_dict["schema_error"] = schema_error
        if schema_url is not UNSET:
            field_dict["schema_url"] = schema_url
        if trust is not UNSET:
            field_dict["trust"] = trust
        if valid is not UNSET:
            field_dict["valid"] = valid
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_active(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        active = _parse_active(d.pop("active"))

        has_schema = d.pop("has_schema")

        loader = d.pop("loader")

        name = d.pop("name")

        def _parse_target(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target = _parse_target(d.pop("target"))

        type_ = d.pop("type")

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file = _parse_file(d.pop("file", UNSET))

        def _parse_interface_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        interface_version = _parse_interface_version(d.pop("interface_version", UNSET))

        def _parse_publisher(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publisher = _parse_publisher(d.pop("publisher", UNSET))

        def _parse_schema_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema_error = _parse_schema_error(d.pop("schema_error", UNSET))

        def _parse_schema_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema_url = _parse_schema_url(d.pop("schema_url", UNSET))

        def _parse_trust(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trust = _parse_trust(d.pop("trust", UNSET))

        def _parse_valid(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        valid = _parse_valid(d.pop("valid", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        plugin_view = cls(
            active=active,
            has_schema=has_schema,
            loader=loader,
            name=name,
            target=target,
            type_=type_,
            error=error,
            file=file,
            interface_version=interface_version,
            publisher=publisher,
            schema_error=schema_error,
            schema_url=schema_url,
            trust=trust,
            valid=valid,
            version=version,
        )

        plugin_view.additional_properties = d
        return plugin_view

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
