from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.named_settings_req_settings import NamedSettingsReqSettings


T = TypeVar("T", bound="NamedSettingsReq")


@_attrs_define
class NamedSettingsReq:
    """The `PATCH /api/v1/admin/<section>/{name}/settings` body: the whole replacement settings bag.
    A sibling of the hooks surface's `PatchSettingsReq` (same shape, same semantics: `settings:` is
    REPLACED, not deep-merged, so the stored bag is always exactly what the caller sent).

        Attributes:
            settings (NamedSettingsReqSettings):
    """

    settings: NamedSettingsReqSettings
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "settings": settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.named_settings_req_settings import NamedSettingsReqSettings

        d = dict(src_dict)
        settings = NamedSettingsReqSettings.from_dict(d.pop("settings"))

        named_settings_req = cls(
            settings=settings,
        )

        named_settings_req.additional_properties = d
        return named_settings_req

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
