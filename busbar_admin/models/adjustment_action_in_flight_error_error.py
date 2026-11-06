from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdjustmentActionInFlightErrorError")


@_attrs_define(repr=False)
class AdjustmentActionInFlightErrorError:
    """
    Attributes:
        code (Literal['action_in_flight']):
        message (str):
    """

    code: Literal["action_in_flight"]
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = cast(Literal["action_in_flight"], d.pop("code"))
        if code != "action_in_flight":
            raise ValueError(f"code must match const 'action_in_flight', got '{code}'")

        message = d.pop("message")

        adjustment_action_in_flight_error_error = cls(
            code=code,
            message=message,
        )

        adjustment_action_in_flight_error_error.additional_properties = d
        return adjustment_action_in_flight_error_error

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
