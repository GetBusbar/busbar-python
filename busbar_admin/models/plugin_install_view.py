from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginInstallView")


@_attrs_define
class PluginInstallView:
    """The result of installing a dynamic-library store plugin (`POST /api/v1/admin/plugins`). The
    engine RE-VERIFIED the uploaded bytes against the running trust posture (the client is never
    trusted), validated the ABI handshake, and atomically wrote the library (+ its manifest sidecar)
    into the plugins directory. `active` takes effect on the next store (re)load; a store change
    applies on restart / `store.module` apply, not as a hot swap (design: store install is
    boot-time/config-apply). Additive-only; never a secret.

        Attributes:
            file (str): The library FILENAME written into the plugins directory (the handle `DELETE` takes).
            interface_version (int): The store C-ABI (`interface_version`) the engine validated the library against.
            name (str): The plugin name from its manifest (or the filename when unsigned).
            note (str): A human note: this install is durable in the folder but takes effect on the next store (re)load.
            trust (str): The server-side trust verdict from the RE-VERIFY: `"trusted"` | `"unverified"`. (A `"rejected"`
                verdict is an error, never a success body.)
            publisher (None | str | Unset): The manifest publisher, when signed.
            version (None | str | Unset): The manifest version, when the upload carried a signed manifest.
    """

    file: str
    interface_version: int
    name: str
    note: str
    trust: str
    publisher: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file

        interface_version = self.interface_version

        name = self.name

        note = self.note

        trust = self.trust

        publisher: None | str | Unset
        if isinstance(self.publisher, Unset):
            publisher = UNSET
        else:
            publisher = self.publisher

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "interface_version": interface_version,
                "name": name,
                "note": note,
                "trust": trust,
            }
        )
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = d.pop("file")

        interface_version = d.pop("interface_version")

        name = d.pop("name")

        note = d.pop("note")

        trust = d.pop("trust")

        def _parse_publisher(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publisher = _parse_publisher(d.pop("publisher", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        plugin_install_view = cls(
            file=file,
            interface_version=interface_version,
            name=name,
            note=note,
            trust=trust,
            publisher=publisher,
            version=version,
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
