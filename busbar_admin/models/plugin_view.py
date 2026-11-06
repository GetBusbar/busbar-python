from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_configuration import PluginConfiguration


T = TypeVar("T", bound="PluginView")


@_attrs_define(repr=False)
class PluginView:
    """One plugin in the plugin catalog (`GET /api/v1/admin/plugins?type=`). A plugin is either
    COMPILED-IN (baked into the binary, feature-gated, provably removable via `--no-default-features`)
    or a signed DYNAMIC-LIBRARY plugin (a loadable `.so`/`.dll`/`.dylib`, dlopen'd over the signed
    plugin ABI; this covers `auth`, `hooks`, and `store` plugin kinds alike as of 1.5.0; the
    retired 1.4.x socket/webhook "external" transport is gone). `active` is `Some(true/false)`
    where activation is tracked (auth modules: in the chain?; hook plugins: configured = true;
    dynamic store: the configured `store.module`) and `None` where it is a per-pool concern not
    summarized here (compiled-in ranking policies). Additive-only.

        Attributes:
            name (str):
            type_ (str): Plugin kind: `auth`, `hooks`/`hook`, `store`, `secret`, `export`, `plane`, or `transport`.
            loader (str): `"compiled-in"` or `"plugin"` (a dlopen'd dynamic-library plugin: auth, hook, and store
                kinds alike as of 1.5.0's signed plugin ABI).
            active (bool | None): Whether the plugin is currently active, where tracked; `None` when activation is not
                summarized
                at this level.
            target (None | str): For a dynamic-library plugin, its NAME (not a socket path or URL, the retired 1.4.x
                transport target). `None` for compiled-in.
            has_schema (bool): Whether the plugin publishes a schema at `schema_url`. The canonical Statement schema
                takes precedence over the legacy manifest field. Linked plugins can publish schemas too.
                Malformed legacy schema text reports `schema_error`; an unreadable installed archive
                instead reports unavailable and cannot publish a verifiable URL.
            file (None | str | Unset): The artifact FILENAME in `plugins.dir`: the `{file}` path segment `DELETE
                /plugins/{file}` and `GET /plugins/{file}/schema` key off (a list row previously
                carried no field a client could feed straight back into either sibling endpoint; `target`
                is documented as the manifest NAME, not necessarily the on-disk filename, and is not a
                reliable substitute). `None` for compiled-in/external rows, which have no backing artifact
                to name. Additive; existing consumers reading only the pre-1.5.1 fields are unaffected.
            archive_sha256 (None | str | Unset): SHA-256 of the complete on-disk archive bytes, not the library inside it.
                Absent for rows without a readable backing archive. Use as an optional mutation preimage.
            version (None | str | Unset): The registered plugin version, or the signed manifest version for a dropped-in
                artifact.
            publisher (None | str | Unset): The manifest's declared publisher (dynamic-library plugins with a manifest).
            interface_version (int | None | Unset): The store C-ABI (`interface_version`) the manifest declares (dynamic-
                library plugins with a
                manifest). Operator-facing name for the "ABI" the engine speaks.
            trust (None | str | Unset): The server-side trust verdict for a dynamic-library plugin, re-evaluated against the
                running
                `plugins.trust` posture: `"trusted"` (signed by an allowlisted publisher), `"unverified"`
                (loaded but not verified, the posture permits it), or `"rejected"` (the `halt` posture would
                refuse it). `None` for compiled-in/external.
            valid (bool | None | Unset): For a dynamic-library plugin: whether the library validated as a busbar store
                plugin the engine
                can load (ABI handshake). `None` for compiled-in/external.
            error (None | str | Unset): Why a dynamic-library plugin did not validate (`valid: false`): a short, secret-free
                reason.
            schema_url (None | str | Unset): Relative schema URL under the admin origin. Artifact URLs include
                source=installed_archive
                and expected_archive_sha256 to inspect the exact disk bytes, not an older loaded generation.
                A malformed legacy schema keeps a URL and reports schema_error. Absent when no schema
                is published, or the archive cannot be read within the admission cap (an unavailable error).
                Linked rows use their registered name and do not need a backing file. Cached linked
                plane/transport URLs specify source=linked_statement to avoid archive/name shadowing.
            configuration (None | PluginConfiguration | Unset): Configuration ownership and declaration availability; no
                plugin settings values.
            schema_error (None | str | Unset): A malformed legacy schema, or an unavailable installed-archive schema.
                Distinct from
                an absent schema. Malformed legacy schema text keeps its URL; an unreadable archive
                omits the URL because the engine cannot bind a schema lookup to its bytes.
    """

    name: str
    type_: str
    loader: str
    active: bool | None
    target: None | str
    has_schema: bool
    file: None | str | Unset = UNSET
    archive_sha256: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    publisher: None | str | Unset = UNSET
    interface_version: int | None | Unset = UNSET
    trust: None | str | Unset = UNSET
    valid: bool | None | Unset = UNSET
    error: None | str | Unset = UNSET
    schema_url: None | str | Unset = UNSET
    configuration: None | PluginConfiguration | Unset = UNSET
    schema_error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.plugin_configuration import PluginConfiguration  # noqa: PLC0415

        name = self.name

        type_ = self.type_

        loader = self.loader

        active: bool | None
        active = self.active

        target: None | str
        target = self.target

        has_schema = self.has_schema

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

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        publisher: None | str | Unset
        if isinstance(self.publisher, Unset):
            publisher = UNSET
        else:
            publisher = self.publisher

        interface_version: int | None | Unset
        if isinstance(self.interface_version, Unset):
            interface_version = UNSET
        else:
            interface_version = self.interface_version

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

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        schema_url: None | str | Unset
        if isinstance(self.schema_url, Unset):
            schema_url = UNSET
        else:
            schema_url = self.schema_url

        configuration: dict[str, Any] | None | Unset
        if isinstance(self.configuration, Unset):
            configuration = UNSET
        elif isinstance(self.configuration, PluginConfiguration):
            configuration = self.configuration.to_dict()
        else:
            configuration = self.configuration

        schema_error: None | str | Unset
        if isinstance(self.schema_error, Unset):
            schema_error = UNSET
        else:
            schema_error = self.schema_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "loader": loader,
                "active": active,
                "target": target,
                "has_schema": has_schema,
            }
        )
        if file is not UNSET:
            field_dict["file"] = file
        if archive_sha256 is not UNSET:
            field_dict["archive_sha256"] = archive_sha256
        if version is not UNSET:
            field_dict["version"] = version
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if interface_version is not UNSET:
            field_dict["interface_version"] = interface_version
        if trust is not UNSET:
            field_dict["trust"] = trust
        if valid is not UNSET:
            field_dict["valid"] = valid
        if error is not UNSET:
            field_dict["error"] = error
        if schema_url is not UNSET:
            field_dict["schema_url"] = schema_url
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if schema_error is not UNSET:
            field_dict["schema_error"] = schema_error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_configuration import PluginConfiguration  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        loader = d.pop("loader")

        def _parse_active(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        active = _parse_active(d.pop("active"))

        def _parse_target(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target = _parse_target(d.pop("target"))

        has_schema = d.pop("has_schema")

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

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_publisher(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publisher = _parse_publisher(d.pop("publisher", UNSET))

        def _parse_interface_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        interface_version = _parse_interface_version(d.pop("interface_version", UNSET))

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

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_schema_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema_url = _parse_schema_url(d.pop("schema_url", UNSET))

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

        def _parse_schema_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema_error = _parse_schema_error(d.pop("schema_error", UNSET))

        plugin_view = cls(
            name=name,
            type_=type_,
            loader=loader,
            active=active,
            target=target,
            has_schema=has_schema,
            file=file,
            archive_sha256=archive_sha256,
            version=version,
            publisher=publisher,
            interface_version=interface_version,
            trust=trust,
            valid=valid,
            error=error,
            schema_url=schema_url,
            configuration=configuration,
            schema_error=schema_error,
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
