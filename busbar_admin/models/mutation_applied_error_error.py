from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MutationAppliedErrorError")


@_attrs_define(repr=False)
class MutationAppliedErrorError:
    """
    Attributes:
        code (Literal['mutation_applied']):
        message (str):
    """

    code: Literal["mutation_applied"]
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
        code = cast(Literal["mutation_applied"], d.pop("code"))
        if code != "mutation_applied":
            raise ValueError(f"code must match const 'mutation_applied', got '{code}'")

        message = d.pop("message")

        mutation_applied_error_error = cls(
            code=code,
            message=message,
        )

        mutation_applied_error_error.additional_properties = d
        return mutation_applied_error_error

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
