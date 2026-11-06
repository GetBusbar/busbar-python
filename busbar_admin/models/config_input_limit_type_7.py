from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ConfigInputLimitType7")


@_attrs_define(repr=False)
class ConfigInputLimitType7:
    """
    Attributes:
        concurrent (int):
    """

    concurrent: int

    def to_dict(self) -> dict[str, Any]:
        concurrent = self.concurrent

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "concurrent": concurrent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        concurrent = d.pop("concurrent")

        if d:
            raise ValueError("Unexpected fields for ConfigInputLimitType7")
        config_input_limit_type_7 = cls(
            concurrent=concurrent,
        )

        return config_input_limit_type_7
