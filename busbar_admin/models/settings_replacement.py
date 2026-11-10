from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.settings_replacement_edit import SettingsReplacementEdit
    from ..models.settings_replacement_settings import SettingsReplacementSettings


T = TypeVar("T", bound="SettingsReplacement")


@_attrs_define(repr=False)
class SettingsReplacement:
    """
    Attributes:
        settings (SettingsReplacementSettings):
        edit (SettingsReplacementEdit | Unset):
    """

    settings: SettingsReplacementSettings
    edit: SettingsReplacementEdit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        settings = self.settings.to_dict()

        edit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.edit, Unset):
            edit = self.edit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "settings": settings,
            }
        )
        if edit is not UNSET:
            field_dict["edit"] = edit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.settings_replacement_edit import SettingsReplacementEdit  # noqa: PLC0415
        from ..models.settings_replacement_settings import SettingsReplacementSettings  # noqa: PLC0415

        d = dict(src_dict)
        settings = SettingsReplacementSettings.from_dict(d.pop("settings"))

        _edit = d.pop("edit", UNSET)
        edit: SettingsReplacementEdit | Unset
        if isinstance(_edit, Unset):
            edit = UNSET
        else:
            edit = SettingsReplacementEdit.from_dict(_edit)

        settings_replacement = cls(
            settings=settings,
            edit=edit,
        )

        settings_replacement.additional_properties = d
        return settings_replacement

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
