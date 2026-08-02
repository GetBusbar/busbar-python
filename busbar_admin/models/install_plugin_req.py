from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InstallPluginReq")


@_attrs_define
class InstallPluginReq:
    """The `POST /api/v1/admin/plugins` request body: install a SIGNED plugin tarball. The tarball
    bytes ride as base64 (`tarball_b64`) — a plugin artifact is opaque binary, so base64 keeps it a
    clean JSON field. The engine RE-VERIFIES the contained signed manifest server-side against the
    running `plugins.*` trust posture (the client is never trusted). `file` is the bare `.tar.gz`
    filename to store it under (storage only — identity comes from the signed manifest inside).

        Attributes:
            file (str):
            tarball_b64 (str):
    """

    file: str
    tarball_b64: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file

        tarball_b64 = self.tarball_b64

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "tarball_b64": tarball_b64,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = d.pop("file")

        tarball_b64 = d.pop("tarball_b64")

        install_plugin_req = cls(
            file=file,
            tarball_b64=tarball_b64,
        )

        install_plugin_req.additional_properties = d
        return install_plugin_req

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
