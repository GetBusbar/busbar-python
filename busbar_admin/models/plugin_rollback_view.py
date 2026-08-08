from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PluginRollbackView")


@_attrs_define
class PluginRollbackView:
    """The result of an EXPLICIT plugin ROLLBACK (`POST /api/v1/admin/plugins/rollback`, 1.5.0
    rollback-friendly versioning): the operator deliberately pinned a plugin DOWN to a prior version and
    the engine hot-swapped to that artifact. The pin is persisted (survives restart) and the trust
    floor was lowered to EXACTLY the pinned version for THIS plugin; a lower artifact still cannot
    load, and an automatic/silent replay of an old artifact is still refused (only this explicit,
    audited action lowered the floor). Additive-only; never a secret.

        Attributes:
            config_version (int): The now-live config version after the hot swap (the ETag the response also carries).
            file (str): The library FILENAME the rollback selected in the plugins directory.
            name (str): The plugin's canonical manifest name that was pinned.
            note (str): A human note on the rollback's semantics + durability.
            publisher (str): The manifest publisher of the pinned artifact (`busbar` = first-party).
            version (str): The version the plugin was pinned DOWN to (now serving), from the target artifact's manifest.
    """

    config_version: int
    file: str
    name: str
    note: str
    publisher: str
    version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config_version = self.config_version

        file = self.file

        name = self.name

        note = self.note

        publisher = self.publisher

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config_version": config_version,
                "file": file,
                "name": name,
                "note": note,
                "publisher": publisher,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        config_version = d.pop("config_version")

        file = d.pop("file")

        name = d.pop("name")

        note = d.pop("note")

        publisher = d.pop("publisher")

        version = d.pop("version")

        plugin_rollback_view = cls(
            config_version=config_version,
            file=file,
            name=name,
            note=note,
            publisher=publisher,
            version=version,
        )

        plugin_rollback_view.additional_properties = d
        return plugin_rollback_view

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
