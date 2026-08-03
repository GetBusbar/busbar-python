from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InspectPluginReq")


@_attrs_define
class InspectPluginReq:
    """`POST /api/v1/admin/plugins/inspect` request body. SAME shape as [`InstallPluginReq`] (question
    #7 — "same request body shape as `POST /plugins`") — `file` is accepted for shape parity with
    the install flow a UI composes around the same upload, but is otherwise UNUSED here: inspect
    never writes anything to disk, so there is no filename to bind an install would need.

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

        inspect_plugin_req = cls(
            file=file,
            tarball_b64=tarball_b64,
        )

        inspect_plugin_req.additional_properties = d
        return inspect_plugin_req

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
