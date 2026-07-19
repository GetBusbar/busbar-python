from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConfigRollbackView")


@_attrs_define
class ConfigRollbackView:
    """`POST /config/rollback` — restore-a-retained-version result (the restored version + the NEW
    config version the rollback produced).

        Attributes:
            config_version (int):
            restored_version (int):
    """

    config_version: int
    restored_version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config_version = self.config_version

        restored_version = self.restored_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config_version": config_version,
                "restored_version": restored_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        config_version = d.pop("config_version")

        restored_version = d.pop("restored_version")

        config_rollback_view = cls(
            config_version=config_version,
            restored_version=restored_version,
        )

        config_rollback_view.additional_properties = d
        return config_rollback_view

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
