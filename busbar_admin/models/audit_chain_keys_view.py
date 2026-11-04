from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.audit_chain_key_view import AuditChainKeyView


T = TypeVar("T", bound="AuditChainKeysView")


@_attrs_define(repr=False)
class AuditChainKeysView:
    """`GET /audit/keys`: the public keys the chain is signed with.

    Attributes:
        algorithm (str):
        keys (list[AuditChainKeyView]): Every public key this node signs records under; empty when it signs none.
        recipe (str):
        signature_domain (str):
    """

    algorithm: str
    keys: list[AuditChainKeyView]
    recipe: str
    signature_domain: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        algorithm = self.algorithm

        keys = []
        for keys_item_data in self.keys:
            keys_item = keys_item_data.to_dict()
            keys.append(keys_item)

        recipe = self.recipe

        signature_domain = self.signature_domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "algorithm": algorithm,
                "keys": keys,
                "recipe": recipe,
                "signature_domain": signature_domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_chain_key_view import AuditChainKeyView  # noqa: PLC0415

        d = dict(src_dict)
        algorithm = d.pop("algorithm")

        keys = []
        _keys = d.pop("keys")
        for keys_item_data in _keys:
            keys_item = AuditChainKeyView.from_dict(keys_item_data)

            keys.append(keys_item)

        recipe = d.pop("recipe")

        signature_domain = d.pop("signature_domain")

        audit_chain_keys_view = cls(
            algorithm=algorithm,
            keys=keys,
            recipe=recipe,
            signature_domain=signature_domain,
        )

        audit_chain_keys_view.additional_properties = d
        return audit_chain_keys_view

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
