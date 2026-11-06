from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.config_input_limit_type_1_per import ConfigInputLimitType1Per
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigInputLimitType1")


@_attrs_define(repr=False)
class ConfigInputLimitType1:
    """
    Attributes:
        tokens (int):
        per (ConfigInputLimitType1Per):
        pool (str | Unset):
    """

    tokens: int
    per: ConfigInputLimitType1Per
    pool: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tokens = self.tokens

        per = self.per.value

        pool = self.pool

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tokens": tokens,
                "per": per,
            }
        )
        if pool is not UNSET:
            field_dict["pool"] = pool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tokens = d.pop("tokens")

        per = ConfigInputLimitType1Per(d.pop("per"))

        pool = d.pop("pool", UNSET)

        if d:
            raise ValueError("Unexpected fields for ConfigInputLimitType1")
        config_input_limit_type_1 = cls(
            tokens=tokens,
            per=per,
            pool=pool,
        )

        return config_input_limit_type_1
