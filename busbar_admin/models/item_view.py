from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kind_view import KindView
from ..models.state_view import StateView
from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemView")


@_attrs_define(repr=False)
class ItemView:
    """A safe observation of custody. The raw payload and operator evidence stay in the Store.

    Attributes:
        operation_id (str):
        body_fingerprint (str):
        recovery_version (int):
        kind (KindView):
        state (StateView):
        first_sent_at_ms (int | None):
        can_resolve (bool):
        owner_node (None | str | Unset): The foreign sender's node as exact lower-case hex; omitted for this node's own
            work.
    """

    operation_id: str
    body_fingerprint: str
    recovery_version: int
    kind: KindView
    state: StateView
    first_sent_at_ms: int | None
    can_resolve: bool
    owner_node: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation_id = self.operation_id

        body_fingerprint = self.body_fingerprint

        recovery_version = self.recovery_version

        kind = self.kind.value

        state = self.state.value

        first_sent_at_ms: int | None
        first_sent_at_ms = self.first_sent_at_ms

        can_resolve = self.can_resolve

        owner_node: None | str | Unset
        if isinstance(self.owner_node, Unset):
            owner_node = UNSET
        else:
            owner_node = self.owner_node

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation_id": operation_id,
                "body_fingerprint": body_fingerprint,
                "recovery_version": recovery_version,
                "kind": kind,
                "state": state,
                "first_sent_at_ms": first_sent_at_ms,
                "can_resolve": can_resolve,
            }
        )
        if owner_node is not UNSET:
            field_dict["owner_node"] = owner_node

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation_id = d.pop("operation_id")

        body_fingerprint = d.pop("body_fingerprint")

        recovery_version = d.pop("recovery_version")

        kind = KindView(d.pop("kind"))

        state = StateView(d.pop("state"))

        def _parse_first_sent_at_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        first_sent_at_ms = _parse_first_sent_at_ms(d.pop("first_sent_at_ms"))

        can_resolve = d.pop("can_resolve")

        def _parse_owner_node(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_node = _parse_owner_node(d.pop("owner_node", UNSET))

        item_view = cls(
            operation_id=operation_id,
            body_fingerprint=body_fingerprint,
            recovery_version=recovery_version,
            kind=kind,
            state=state,
            first_sent_at_ms=first_sent_at_ms,
            can_resolve=can_resolve,
            owner_node=owner_node,
        )

        item_view.additional_properties = d
        return item_view

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
