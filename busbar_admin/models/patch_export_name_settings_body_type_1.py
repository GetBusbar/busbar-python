from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_export_name_settings_body_type_1_edit import PatchExportNameSettingsBodyType1Edit
    from ..models.patch_export_name_settings_body_type_1_settings import PatchExportNameSettingsBodyType1Settings


T = TypeVar("T", bound="PatchExportNameSettingsBodyType1")


@_attrs_define(repr=False)
class PatchExportNameSettingsBodyType1:
    """
    Attributes:
        edit (PatchExportNameSettingsBodyType1Edit):
        settings (PatchExportNameSettingsBodyType1Settings | Unset):
    """

    edit: PatchExportNameSettingsBodyType1Edit
    settings: PatchExportNameSettingsBodyType1Settings | Unset = UNSET
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
        from ..models.patch_export_name_settings_body_type_1_edit import PatchExportNameSettingsBodyType1Edit  # noqa: PLC0415
        from ..models.patch_export_name_settings_body_type_1_settings import PatchExportNameSettingsBodyType1Settings  # noqa: PLC0415

        d = dict(src_dict)
        edit = PatchExportNameSettingsBodyType1Edit.from_dict(d.pop("edit"))

        _settings = d.pop("settings", UNSET)
        settings: PatchExportNameSettingsBodyType1Settings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = PatchExportNameSettingsBodyType1Settings.from_dict(_settings)

        patch_export_name_settings_body_type_1 = cls(
            edit=edit,
            settings=settings,
        )

        patch_export_name_settings_body_type_1.additional_properties = d
        return patch_export_name_settings_body_type_1

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
