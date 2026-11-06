from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.plugin_configuration_section import PluginConfigurationSection


T = TypeVar("T", bound="PluginConfiguration")


@_attrs_define(repr=False)
class PluginConfiguration:
    """Configuration ownership, not a replacement for the declaring parser's input grammar.

    Attributes:
        root_keys (list[str]): Kind::verb for non-planes; the declaring and other non-consumed Statement sections for
            planes.
        root_source (str): kind_verb, statement, or unavailable. A missing declaration never guesses a plane root.
        declaration_source (str): linked_statement, loaded_manifest, installed_archive, manifest, or unavailable.
        declaration_availability (str): present, absent (legacy/no Statement), or unavailable
            (unreadable/refused/unresolved).
        sections (list[PluginConfigurationSection]): Statement sections, including consumed sections which are not owned
            config roots.
        claims (list[str]): Transport URL schemes from the Statement; empty is never inferred from a module name.
        settings_schema_scope (str): Lifecycle settings only. Host-reserved fields and SecretRef transformations still
            apply.
        input_schema_complete (bool): False: the lifecycle schema alone is not the complete authored configuration
            grammar.
        configuration_shape (str): Transport uses provider_catalog_and_deployment; other kinds use kind_root or
            declared_sections.
        host_policy_paths (list[str]): Existing host inputs to TransportSettings, not arbitrary per-transport settings.
    """

    root_keys: list[str]
    root_source: str
    declaration_source: str
    declaration_availability: str
    sections: list[PluginConfigurationSection]
    claims: list[str]
    settings_schema_scope: str
    input_schema_complete: bool
    configuration_shape: str
    host_policy_paths: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        root_keys = self.root_keys

        root_source = self.root_source

        declaration_source = self.declaration_source

        declaration_availability = self.declaration_availability

        sections = []
        for sections_item_data in self.sections:
            sections_item = sections_item_data.to_dict()
            sections.append(sections_item)

        claims = self.claims

        settings_schema_scope = self.settings_schema_scope

        input_schema_complete = self.input_schema_complete

        configuration_shape = self.configuration_shape

        host_policy_paths = self.host_policy_paths

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "root_keys": root_keys,
                "root_source": root_source,
                "declaration_source": declaration_source,
                "declaration_availability": declaration_availability,
                "sections": sections,
                "claims": claims,
                "settings_schema_scope": settings_schema_scope,
                "input_schema_complete": input_schema_complete,
                "configuration_shape": configuration_shape,
                "host_policy_paths": host_policy_paths,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_configuration_section import PluginConfigurationSection  # noqa: PLC0415

        d = dict(src_dict)
        root_keys = cast(list[str], d.pop("root_keys"))

        root_source = d.pop("root_source")

        declaration_source = d.pop("declaration_source")

        declaration_availability = d.pop("declaration_availability")

        sections = []
        _sections = d.pop("sections")
        for sections_item_data in _sections:
            sections_item = PluginConfigurationSection.from_dict(sections_item_data)

            sections.append(sections_item)

        claims = cast(list[str], d.pop("claims"))

        settings_schema_scope = d.pop("settings_schema_scope")

        input_schema_complete = d.pop("input_schema_complete")

        configuration_shape = d.pop("configuration_shape")

        host_policy_paths = cast(list[str], d.pop("host_policy_paths"))

        plugin_configuration = cls(
            root_keys=root_keys,
            root_source=root_source,
            declaration_source=declaration_source,
            declaration_availability=declaration_availability,
            sections=sections,
            claims=claims,
            settings_schema_scope=settings_schema_scope,
            input_schema_complete=input_schema_complete,
            configuration_shape=configuration_shape,
            host_policy_paths=host_policy_paths,
        )

        plugin_configuration.additional_properties = d
        return plugin_configuration

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
