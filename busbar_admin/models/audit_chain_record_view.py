from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.audit_recipe_element_type_1 import AuditRecipeElementType1


T = TypeVar("T", bound="AuditChainRecordView")


@_attrs_define(repr=False)
class AuditChainRecordView:
    """One sealed record: the digest recipe's fields, in the recipe's order (every value a string: a
    text as its text, a number as its decimal text; each repeated group as an array under its own
    name), then the record's digest and signature.

        Attributes:
            hash_ (str):
            key_id (None | str):
            signature (None | str):
    """

    hash_: str
    key_id: None | str
    signature: None | str
    additional_properties: dict[str, list[AuditRecipeElementType1 | str] | str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_recipe_element_type_1 import AuditRecipeElementType1  # noqa: PLC0415

        hash_ = self.hash_

        key_id: None | str
        key_id = self.key_id

        signature: None | str
        signature = self.signature

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, list):
                field_dict[prop_name] = []
                for componentsschemas_audit_recipe_value_type_1_item_data in prop:
                    componentsschemas_audit_recipe_value_type_1_item: dict[str, Any] | str
                    if isinstance(componentsschemas_audit_recipe_value_type_1_item_data, AuditRecipeElementType1):
                        componentsschemas_audit_recipe_value_type_1_item = (
                            componentsschemas_audit_recipe_value_type_1_item_data.to_dict()
                        )
                    else:
                        componentsschemas_audit_recipe_value_type_1_item = (
                            componentsschemas_audit_recipe_value_type_1_item_data
                        )
                    field_dict[prop_name].append(componentsschemas_audit_recipe_value_type_1_item)

            else:
                field_dict[prop_name] = prop

        field_dict.update(
            {
                "hash": hash_,
                "key_id": key_id,
                "signature": signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_recipe_element_type_1 import AuditRecipeElementType1  # noqa: PLC0415

        d = dict(src_dict)
        hash_ = d.pop("hash")

        def _parse_key_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        key_id = _parse_key_id(d.pop("key_id"))

        def _parse_signature(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        signature = _parse_signature(d.pop("signature"))

        audit_chain_record_view = cls(
            hash_=hash_,
            key_id=key_id,
            signature=signature,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> list[AuditRecipeElementType1 | str] | str:
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    componentsschemas_audit_recipe_value_type_1 = []
                    _componentsschemas_audit_recipe_value_type_1 = data
                    for (
                        componentsschemas_audit_recipe_value_type_1_item_data
                    ) in _componentsschemas_audit_recipe_value_type_1:

                        def _parse_componentsschemas_audit_recipe_value_type_1_item(
                            data: object,
                        ) -> AuditRecipeElementType1 | str:
                            try:
                                if not isinstance(data, dict):
                                    raise TypeError()
                                componentsschemas_audit_recipe_element_type_1 = AuditRecipeElementType1.from_dict(data)

                                return componentsschemas_audit_recipe_element_type_1
                            except (TypeError, ValueError, AttributeError, KeyError):
                                pass
                            return cast(AuditRecipeElementType1 | str, data)

                        componentsschemas_audit_recipe_value_type_1_item = (
                            _parse_componentsschemas_audit_recipe_value_type_1_item(
                                componentsschemas_audit_recipe_value_type_1_item_data
                            )
                        )

                        componentsschemas_audit_recipe_value_type_1.append(
                            componentsschemas_audit_recipe_value_type_1_item
                        )

                    return componentsschemas_audit_recipe_value_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(list[AuditRecipeElementType1 | str] | str, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        audit_chain_record_view.additional_properties = additional_properties
        return audit_chain_record_view

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[AuditRecipeElementType1 | str] | str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[AuditRecipeElementType1 | str] | str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
