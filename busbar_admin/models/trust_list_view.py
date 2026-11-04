from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.trust_key_view import TrustKeyView


T = TypeVar("T", bound="TrustListView")


@_attrs_define(repr=False)
class TrustListView:
    """`GET /trust`: every trust key and its state.

    Attributes:
        keys (list[TrustKeyView]): Ordered by instance, counterparty and item, each counterparty before its items.
    """

    keys: list[TrustKeyView]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keys = []
        for keys_item_data in self.keys:
            keys_item = keys_item_data.to_dict()
            keys.append(keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keys": keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trust_key_view import TrustKeyView  # noqa: PLC0415

        d = dict(src_dict)
        keys = []
        _keys = d.pop("keys")
        for keys_item_data in _keys:
            keys_item = TrustKeyView.from_dict(keys_item_data)

            keys.append(keys_item)

        trust_list_view = cls(
            keys=keys,
        )

        trust_list_view.additional_properties = d
        return trust_list_view

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
