from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_configuration import PluginConfiguration


T = TypeVar("T", bound="PluginSchemaView")


@_attrs_define(repr=False)
class PluginSchemaView:
    """`GET /plugins/{name}/schema`: the generalized, all-kinds sibling of [`HookSchemaView`].
    Carries `trust`/`source`/`schema_error` on top of
    `{name, schema}` so busbar-ui never has to infer trust state or the describe/manifest
    precedence rule from context; the server always picks exactly one source and reports which.

        Attributes:
            name (str):
            schema (Any): The plugin settings JSON Schema. The canonical Statement takes precedence over the
                legacy manifest field. Null means neither was supplied, or a legacy schema failed parsing
                (with `schema_error`); malformed Statement schemas are refused at admission.
            schema_error (None | str): Set only when the manifest's `settings_schema` was present but failed to parse as
                JSON;
                `null` for a manifest that genuinely never set the field. Never collapsed into a bare
                `schema: null`: a present-but-corrupt schema is a real
                authoring/packaging bug, not "this plugin simply has none."
            trust (str): `"trusted" | "unverified" | "rejected"`: the same vocabulary the plugin catalog already
                uses (never `"verified"`).
            source (str): `"describe"` when a currently-loaded `kind: hook` answered its live `describe` wire
                message; `"statement"` for a linked plugin; `"manifest"` for a dropped-in plugin
                (its signed Statement schema, or the legacy manifest fallback); "installed_archive" for
                an explicit archive lookup bound to the returned archive_sha256. source=linked_statement
                requests read the startup cache and return "statement" here. Lets
                busbar-ui explain "why does this form look different from what I expected" without
                implementing the describe/manifest precedence rule itself.
            configuration (None | PluginConfiguration | Unset): Ownership metadata; lifecycle settings schemas do not
                replace authored input grammar.
            version (None | str | Unset): The plugin's semantic version from its manifest. Present on `POST
                /plugins/inspect` (which
                previews an on-disk candidate's manifest) and installed_archive schema reads; absent on
                legacy loaded-registry schema reads. Declared here so a codegen'd client keeps the field the inspect
                handler always sends, rather than silently dropping it.
            file (None | str | Unset): Present for explicit installed_archive lookup; a bare archive filename.
            archive_sha256 (None | str | Unset): Digest of the same complete archive bytes inspected for this schema.
            schema_state (None | str | Unset): installed_archive lookup: present, absent, or invalid legacy schema.
            kind (None | str | Unset): The plugin's `kind` (`hook` | `secret` | …) from its manifest. Both `GET
                /plugins/{file}/schema`
                and `POST /plugins/inspect` emit it (`null` only when the plugin cannot be resolved to a
                manifest). Declared so codegen'd clients keep it.
            restart_required_default (bool | None | Unset): The kind-derived restart-scoping default
                (`busbar_plugin_sign::kind_restart_default`), so
                busbar-ui need not hardcode the kind→default table. Emitted by both schema endpoints (`null`
                only when the plugin has no resolvable manifest/kind). Declared so codegen'd clients keep it.
    """

    name: str
    schema: Any
    schema_error: None | str
    trust: str
    source: str
    configuration: None | PluginConfiguration | Unset = UNSET
    version: None | str | Unset = UNSET
    file: None | str | Unset = UNSET
    archive_sha256: None | str | Unset = UNSET
    schema_state: None | str | Unset = UNSET
    kind: None | str | Unset = UNSET
    restart_required_default: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.plugin_configuration import PluginConfiguration  # noqa: PLC0415

        name = self.name

        schema = self.schema

        schema_error: None | str
        schema_error = self.schema_error

        trust = self.trust

        source = self.source

        configuration: dict[str, Any] | None | Unset
        if isinstance(self.configuration, Unset):
            configuration = UNSET
        elif isinstance(self.configuration, PluginConfiguration):
            configuration = self.configuration.to_dict()
        else:
            configuration = self.configuration

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        file: None | str | Unset
        if isinstance(self.file, Unset):
            file = UNSET
        else:
            file = self.file

        archive_sha256: None | str | Unset
        if isinstance(self.archive_sha256, Unset):
            archive_sha256 = UNSET
        else:
            archive_sha256 = self.archive_sha256

        schema_state: None | str | Unset
        if isinstance(self.schema_state, Unset):
            schema_state = UNSET
        else:
            schema_state = self.schema_state

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "schema": schema,
                "schema_error": schema_error,
                "trust": trust,
                "source": source,
            }
        )
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if version is not UNSET:
            field_dict["version"] = version
        if file is not UNSET:
            field_dict["file"] = file
        if archive_sha256 is not UNSET:
            field_dict["archive_sha256"] = archive_sha256
        if schema_state is not UNSET:
            field_dict["schema_state"] = schema_state
        if kind is not UNSET:
            field_dict["kind"] = kind
        if restart_required_default is not UNSET:
            field_dict["restart_required_default"] = restart_required_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_configuration import PluginConfiguration  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        schema = d.pop("schema")

        def _parse_schema_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        schema_error = _parse_schema_error(d.pop("schema_error"))

        trust = d.pop("trust")

        source = d.pop("source")

        def _parse_configuration(data: object) -> None | PluginConfiguration | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                configuration_type_0 = PluginConfiguration.from_dict(data)

                return configuration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for configuration")

        configuration = _parse_configuration(d.pop("configuration", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file = _parse_file(d.pop("file", UNSET))

        def _parse_archive_sha256(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        archive_sha256 = _parse_archive_sha256(d.pop("archive_sha256", UNSET))

        def _parse_schema_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema_state = _parse_schema_state(d.pop("schema_state", UNSET))

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

        plugin_schema_view = cls(
            name=name,
            schema=schema,
            schema_error=schema_error,
            trust=trust,
            source=source,
            configuration=configuration,
            version=version,
            file=file,
            archive_sha256=archive_sha256,
            schema_state=schema_state,
            kind=kind,
            restart_required_default=restart_required_default,
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
