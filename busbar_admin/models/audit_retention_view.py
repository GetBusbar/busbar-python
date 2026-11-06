from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditRetentionView")


@_attrs_define(repr=False)
class AuditRetentionView:
    """
    Attributes:
        ring_from (None | str):
        ring_to (None | str):
        durable_from (None | str): Unknown: the Store does not expose an audit retention floor.
        durable_from_known (bool):
    """

    ring_from: None | str
    ring_to: None | str
    durable_from: None | str
    durable_from_known: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ring_from: None | str
        ring_from = self.ring_from

        ring_to: None | str
        ring_to = self.ring_to

        durable_from: None | str
        durable_from = self.durable_from

        durable_from_known = self.durable_from_known

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ring_from": ring_from,
                "ring_to": ring_to,
                "durable_from": durable_from,
                "durable_from_known": durable_from_known,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_ring_from(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ring_from = _parse_ring_from(d.pop("ring_from"))

        def _parse_ring_to(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ring_to = _parse_ring_to(d.pop("ring_to"))

        def _parse_durable_from(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        durable_from = _parse_durable_from(d.pop("durable_from"))

        durable_from_known = d.pop("durable_from_known")

        audit_retention_view = cls(
            ring_from=ring_from,
            ring_to=ring_to,
            durable_from=durable_from,
            durable_from_known=durable_from_known,
        )

        audit_retention_view.additional_properties = d
        return audit_retention_view

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
