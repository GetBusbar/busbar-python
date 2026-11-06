from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginRollbackReq")


@_attrs_define(repr=False)
class PluginRollbackReq:
    """The `POST /api/v1/admin/plugins/rollback` body: the target library FILENAME to roll DOWN to.

    Attributes:
        file (str): The plugin tarball FILENAME (in the plugins directory) carrying the prior version to pin to.
        expected_archive_sha256 (str | Unset): Optional exact SHA-256 of the complete archive reviewed by the caller.
            Stale/missing = 409.
    """

    file: str
    expected_archive_sha256: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file

        expected_archive_sha256 = self.expected_archive_sha256

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if expected_archive_sha256 is not UNSET:
            field_dict["expected_archive_sha256"] = expected_archive_sha256

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = d.pop("file")

        expected_archive_sha256 = d.pop("expected_archive_sha256", UNSET)

        plugin_rollback_req = cls(
            file=file,
            expected_archive_sha256=expected_archive_sha256,
        )

        plugin_rollback_req.additional_properties = d
        return plugin_rollback_req

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
