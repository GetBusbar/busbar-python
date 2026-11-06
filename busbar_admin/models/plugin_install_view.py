from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginInstallView")


@_attrs_define(repr=False)
class PluginInstallView:
    """The result of installing a dynamic-library store plugin (`POST /api/v1/admin/plugins`). The
    engine RE-VERIFIED the uploaded bytes against the running trust posture (the client is never
    trusted), validated the ABI handshake, and atomically wrote the library (+ its manifest sidecar)
    into the plugins directory. `active` takes effect on the next store (re)load; a store change
    applies on restart / `store.module` apply, not as a hot swap (design: store install is
    boot-time/config-apply). Additive-only; never a secret.

        Attributes:
            file (str): The library FILENAME written into the plugins directory (the handle `DELETE` takes).
            name (str): The plugin name from its manifest (or the filename when unsigned).
            interface_version (int): The store C-ABI (`interface_version`) the engine validated the library against.
            trust (str): The server-side trust verdict from the RE-VERIFY: `"trusted"` | `"unverified"`. (A `"rejected"`
                verdict is an error, never a success body.)
            note (str): A human note: this install is durable in the folder but takes effect on the next store (re)load.
            version (None | str | Unset): The manifest version, when the upload carried a signed manifest.
            publisher (None | str | Unset): The manifest publisher, when signed.
    """

    file: str
    name: str
    interface_version: int
    trust: str
    note: str
    version: None | str | Unset = UNSET
    publisher: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file

        name = self.name

        interface_version = self.interface_version

        trust = self.trust

        note = self.note

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "name": name,
                "interface_version": interface_version,
                "trust": trust,
                "note": note,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if publisher is not UNSET:
            field_dict["publisher"] = publisher

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = d.pop("file")

        name = d.pop("name")

        interface_version = d.pop("interface_version")

        trust = d.pop("trust")

        note = d.pop("note")

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

        plugin_install_view = cls(
            file=file,
            name=name,
            interface_version=interface_version,
            trust=trust,
            note=note,
            version=version,
            publisher=publisher,
        )

        plugin_install_view.additional_properties = d
        return plugin_install_view

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
