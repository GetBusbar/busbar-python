from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_tools_name_settings_body_type_0_edit import PatchToolsNameSettingsBodyType0Edit
    from ..models.patch_tools_name_settings_body_type_0_settings import PatchToolsNameSettingsBodyType0Settings


T = TypeVar("T", bound="PatchToolsNameSettingsBodyType0")


@_attrs_define(repr=False)
class PatchToolsNameSettingsBodyType0:
    """
    Attributes:
        settings (PatchToolsNameSettingsBodyType0Settings):
        edit (PatchToolsNameSettingsBodyType0Edit | Unset):
    """

    settings: PatchToolsNameSettingsBodyType0Settings
    edit: PatchToolsNameSettingsBodyType0Edit | Unset = UNSET
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
        from ..models.patch_tools_name_settings_body_type_0_edit import PatchToolsNameSettingsBodyType0Edit  # noqa: PLC0415
        from ..models.patch_tools_name_settings_body_type_0_settings import PatchToolsNameSettingsBodyType0Settings  # noqa: PLC0415

        d = dict(src_dict)
        settings = PatchToolsNameSettingsBodyType0Settings.from_dict(d.pop("settings"))

        _edit = d.pop("edit", UNSET)
        edit: PatchToolsNameSettingsBodyType0Edit | Unset
        if isinstance(_edit, Unset):
            edit = UNSET
        else:
            edit = PatchToolsNameSettingsBodyType0Edit.from_dict(_edit)

        patch_tools_name_settings_body_type_0 = cls(
            settings=settings,
            edit=edit,
        )

        patch_tools_name_settings_body_type_0.additional_properties = d
        return patch_tools_name_settings_body_type_0

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
