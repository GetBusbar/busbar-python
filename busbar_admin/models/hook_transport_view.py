from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HookTransportView")


@_attrs_define
class HookTransportView:
    """The transport half of a `HookView`: which wire the hook speaks and its target (socket path or
    webhook URL — operator config, not a secret). Exactly one of `socket`/`webhook` is set.

        Attributes:
            kind (str): `"socket"` or `"webhook"` (or `"none"` for a misconfigured entry with neither).
            target (None | str): The socket path or webhook URL. `None` only if the definition set neither transport.
    """

    kind: str
    target: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        target: None | str
        target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "target": target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = d.pop("kind")

        def _parse_target(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target = _parse_target(d.pop("target"))

        hook_transport_view = cls(
            kind=kind,
            target=target,
        )

        hook_transport_view.additional_properties = d
        return hook_transport_view

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
