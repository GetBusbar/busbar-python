from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RestartView")


@_attrs_define(repr=False)
class RestartView:
    """`POST /restart`: accepted-and-draining result.

    Attributes:
        restarting (bool):
        supervisor_detected (bool): Whether a process supervisor was detected. False means the caller confirmed
            explicitly.
        note (str):
    """

    restarting: bool
    supervisor_detected: bool
    note: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restarting = self.restarting

        supervisor_detected = self.supervisor_detected

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "restarting": restarting,
                "supervisor_detected": supervisor_detected,
                "note": note,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        restarting = d.pop("restarting")

        supervisor_detected = d.pop("supervisor_detected")

        note = d.pop("note")

        restart_view = cls(
            restarting=restarting,
            supervisor_detected=supervisor_detected,
            note=note,
        )

        restart_view.additional_properties = d
        return restart_view

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
