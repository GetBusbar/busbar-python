from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.put_config_settings_config_settings_replacement_rate_card_type_0_additional_property_type_0 import (
        PutConfigSettingsConfigSettingsReplacementRateCardType0AdditionalPropertyType0,
    )


T = TypeVar("T", bound="PutConfigSettingsConfigSettingsReplacementRateCardType0")


@_attrs_define(repr=False)
class PutConfigSettingsConfigSettingsReplacementRateCardType0:
    additional_properties: dict[
        str, list[Any] | PutConfigSettingsConfigSettingsReplacementRateCardType0AdditionalPropertyType0
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.put_config_settings_config_settings_replacement_rate_card_type_0_additional_property_type_0 import (
            PutConfigSettingsConfigSettingsReplacementRateCardType0AdditionalPropertyType0,  # noqa: PLC0415
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, PutConfigSettingsConfigSettingsReplacementRateCardType0AdditionalPropertyType0):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_config_settings_config_settings_replacement_rate_card_type_0_additional_property_type_0 import (
            PutConfigSettingsConfigSettingsReplacementRateCardType0AdditionalPropertyType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        put_config_settings_config_settings_replacement_rate_card_type_0 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> list[Any] | PutConfigSettingsConfigSettingsReplacementRateCardType0AdditionalPropertyType0:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = (
                        PutConfigSettingsConfigSettingsReplacementRateCardType0AdditionalPropertyType0.from_dict(data)
                    )

                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, list):
                    raise TypeError()
                additional_property_type_1 = cast(list[Any], data)

                return additional_property_type_1
                raise ValueError("Invalid value for additional_property")

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        put_config_settings_config_settings_replacement_rate_card_type_0.additional_properties = additional_properties
        return put_config_settings_config_settings_replacement_rate_card_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> list[Any] | PutConfigSettingsConfigSettingsReplacementRateCardType0AdditionalPropertyType0:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: list[Any] | PutConfigSettingsConfigSettingsReplacementRateCardType0AdditionalPropertyType0,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
