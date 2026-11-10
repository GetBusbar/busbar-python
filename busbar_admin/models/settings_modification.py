from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.settings_modification_edit import SettingsModificationEdit
    from ..models.settings_modification_settings import SettingsModificationSettings


T = TypeVar("T", bound="SettingsModification")


@_attrs_define(repr=False)
class SettingsModification:
    """
    Attributes:
        edit (SettingsModificationEdit):
        settings (SettingsModificationSettings | Unset):
    """

    edit: SettingsModificationEdit
    settings: SettingsModificationSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edit = self.edit.to_dict()

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "edit": edit,
            }
        )
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.settings_modification_edit import SettingsModificationEdit  # noqa: PLC0415
        from ..models.settings_modification_settings import SettingsModificationSettings  # noqa: PLC0415

        d = dict(src_dict)
        edit = SettingsModificationEdit.from_dict(d.pop("edit"))

        _settings = d.pop("settings", UNSET)
        settings: SettingsModificationSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = SettingsModificationSettings.from_dict(_settings)

        settings_modification = cls(
            edit=edit,
            settings=settings,
        )

        settings_modification.additional_properties = d
        return settings_modification

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
