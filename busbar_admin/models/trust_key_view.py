from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TrustKeyView")


@_attrs_define(repr=False)
class TrustKeyView:
    """One trust key of the kernel's trust book and its state.

    Attributes:
        approved (None | str): What it is approved at: the catalogue hash, or the item's digest.
        counterparty (str): The counterparty, as the instance's configuration names it.
        instance (str): The plane instance label.
        item (None | str): The item at the counterparty, for an item key.
        key (str): The key, `<instance>/<counterparty>[/<item>]`: what `POST /trust/approve` and `/revoke` name.
        seen (None | str): What it was last sighted at.
        state (str): `new` (sighted and never approved, or revoked: refused), `approved` (approved, not sighted
            since), `same` (sighted as approved), `drifted` (sighted other than approved: refused until
            re-approved) or `quarantined` (the counterparty's catalogue moved: refused until re-approved).
    """

    approved: None | str
    counterparty: str
    instance: str
    item: None | str
    key: str
    seen: None | str
    state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approved: None | str
        approved = self.approved

        counterparty = self.counterparty

        instance = self.instance

        item: None | str
        item = self.item

        key = self.key

        seen: None | str
        seen = self.seen

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "approved": approved,
                "counterparty": counterparty,
                "instance": instance,
                "item": item,
                "key": key,
                "seen": seen,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_approved(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        approved = _parse_approved(d.pop("approved"))

        counterparty = d.pop("counterparty")

        instance = d.pop("instance")

        def _parse_item(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        item = _parse_item(d.pop("item"))

        key = d.pop("key")

        def _parse_seen(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        seen = _parse_seen(d.pop("seen"))

        state = d.pop("state")

        trust_key_view = cls(
            approved=approved,
            counterparty=counterparty,
            instance=instance,
            item=item,
            key=key,
            seen=seen,
            state=state,
        )

        trust_key_view.additional_properties = d
        return trust_key_view

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
