from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginSchemaView")


@_attrs_define
class PluginSchemaView:
    """`GET /plugins/{name}/schema`: the generalized, all-kinds sibling of [`HookSchemaView`].
    Carries `trust`/`source`/`schema_error` on top of
    `{name, schema}` so busbar-ui never has to infer trust state or the describe/manifest
    precedence rule from context; the server always picks exactly one source and reports which.

        Attributes:
            name (str):
            schema (Any): The plugin's settings JSON Schema verbatim, or `null`, either because the manifest never
                set `settings_schema`, or (distinctly, see `schema_error`) because it did but the value
                failed to parse.
            schema_error (None | str): Set only when the manifest's `settings_schema` was present but failed to parse as
                JSON;
                `null` for a manifest that genuinely never set the field. Never collapsed into a bare
                `schema: null`: a present-but-corrupt schema is a real
                authoring/packaging bug, not "this plugin simply has none."
            source (str): `"describe"` when a currently-loaded `kind: hook` answered its live `describe` wire
                message (the existing describe-proxy behavior, unchanged); `"manifest"` otherwise. Lets
                busbar-ui explain "why does this form look different from what I expected" without
                implementing the describe/manifest precedence rule itself.
            trust (str): `"trusted" | "unverified" | "rejected"`: the same vocabulary the plugin catalog already
                uses (never `"verified"`).
            kind (None | str | Unset): The plugin's `kind` (`hook` | `secret` | …) from its manifest. Both `GET
                /plugins/{file}/schema`
                and `POST /plugins/inspect` emit it (`null` only when the plugin cannot be resolved to a
                manifest). Declared so codegen'd clients keep it.
            restart_required_default (bool | None | Unset): The kind-derived restart-scoping default
                (`busbar_plugin_sign::kind_restart_default`), so
                busbar-ui need not hardcode the kind→default table. Emitted by both schema endpoints (`null`
                only when the plugin has no resolvable manifest/kind). Declared so codegen'd clients keep it.
            version (None | str | Unset): The plugin's semantic version from its manifest. Present on `POST
                /plugins/inspect` (which
                previews an on-disk candidate's manifest); `null`/absent on `GET /plugins/{file}/schema`, which
                does not surface the version. Declared here so a codegen'd client keeps the field the inspect
                handler always sends, rather than silently dropping it.
    """

    name: str
    schema: Any
    schema_error: None | str
    source: str
    trust: str
    kind: None | str | Unset = UNSET
    restart_required_default: bool | None | Unset = UNSET
    version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        schema = self.schema

        schema_error: None | str
        schema_error = self.schema_error

        source = self.source

        trust = self.trust

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        restart_required_default: bool | None | Unset
        if isinstance(self.restart_required_default, Unset):
            restart_required_default = UNSET
        else:
            restart_required_default = self.restart_required_default

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "schema": schema,
                "schema_error": schema_error,
                "source": source,
                "trust": trust,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if restart_required_default is not UNSET:
            field_dict["restart_required_default"] = restart_required_default
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        schema = d.pop("schema")

        def _parse_schema_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        schema_error = _parse_schema_error(d.pop("schema_error"))

        source = d.pop("source")

        trust = d.pop("trust")

        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_restart_required_default(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        restart_required_default = _parse_restart_required_default(d.pop("restart_required_default", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        plugin_schema_view = cls(
            name=name,
            schema=schema,
            schema_error=schema_error,
            source=source,
            trust=trust,
            kind=kind,
            restart_required_default=restart_required_default,
            version=version,
        )

        plugin_schema_view.additional_properties = d
        return plugin_schema_view

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
