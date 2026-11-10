from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_agents_name_settings_body_type_1_edit import PatchAgentsNameSettingsBodyType1Edit
    from ..models.patch_agents_name_settings_body_type_1_settings import PatchAgentsNameSettingsBodyType1Settings


T = TypeVar("T", bound="PatchAgentsNameSettingsBodyType1")


@_attrs_define(repr=False)
class PatchAgentsNameSettingsBodyType1:
    """
    Attributes:
        edit (PatchAgentsNameSettingsBodyType1Edit):
        settings (PatchAgentsNameSettingsBodyType1Settings | Unset):
    """

    edit: PatchAgentsNameSettingsBodyType1Edit
    settings: PatchAgentsNameSettingsBodyType1Settings | Unset = UNSET
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
        from ..models.patch_agents_name_settings_body_type_1_edit import PatchAgentsNameSettingsBodyType1Edit  # noqa: PLC0415
        from ..models.patch_agents_name_settings_body_type_1_settings import PatchAgentsNameSettingsBodyType1Settings  # noqa: PLC0415

        d = dict(src_dict)
        edit = PatchAgentsNameSettingsBodyType1Edit.from_dict(d.pop("edit"))

        _settings = d.pop("settings", UNSET)
        settings: PatchAgentsNameSettingsBodyType1Settings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = PatchAgentsNameSettingsBodyType1Settings.from_dict(_settings)

        patch_agents_name_settings_body_type_1 = cls(
            edit=edit,
            settings=settings,
        )

        patch_agents_name_settings_body_type_1.additional_properties = d
        return patch_agents_name_settings_body_type_1

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
