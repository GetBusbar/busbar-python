from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PluginSchemaView")


@_attrs_define
class PluginSchemaView:
    """`GET /plugins/{name}/schema` — the generalized, all-kinds sibling of [`HookSchemaView`]
    (plugin-settings-schema-SPEC.md). Carries `trust`/`source`/`schema_error` on top of
    `{name, schema}` so busbar-ui never has to infer trust state or the describe/manifest
    precedence rule from context — the server always picks exactly one source and reports which.

        Attributes:
            name (str):
            schema (Any): The plugin's settings JSON Schema verbatim, or `null` — either because the manifest never
                set `settings_schema`, or (distinctly, see `schema_error`) because it did but the value
                failed to parse.
            schema_error (None | str): Set only when the manifest's `settings_schema` was present but failed to parse as
                JSON —
                `null` for a manifest that genuinely never set the field. Never collapsed into a bare
                `schema: null` (question #3, round-4 correction): a present-but-corrupt schema is a real
                authoring/packaging bug, not "this plugin simply has none."
            source (str): `"describe"` when a currently-loaded `kind: hook` answered its live `describe` wire
                message (the existing describe-proxy behavior, unchanged); `"manifest"` otherwise. Lets
                busbar-ui explain "why does this form look different from what I expected" without
                implementing the describe/manifest precedence rule itself (question #3, round-4
                correction).
            trust (str): `"trusted" | "unverified" | "rejected"` — the same vocabulary the plugin catalog already
                uses (never `"verified"`; question #8, round-4 correction).
    """

    name: str
    schema: Any
    schema_error: None | str
    source: str
    trust: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        schema = self.schema

        schema_error: None | str
        schema_error = self.schema_error

        source = self.source

        trust = self.trust

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

        plugin_schema_view = cls(
            name=name,
            schema=schema,
            schema_error=schema_error,
            source=source,
            trust=trust,
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
