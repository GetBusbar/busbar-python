from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.config_input_limit_type_3_per import ConfigInputLimitType3Per
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigInputLimitType3")


@_attrs_define(repr=False)
class ConfigInputLimitType3:
    """
    Attributes:
        tokens_output (int):
        per (ConfigInputLimitType3Per):
        pool (str | Unset):
    """

    tokens_output: int
    per: ConfigInputLimitType3Per
    pool: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tokens_output = self.tokens_output

        per = self.per.value

        pool = self.pool

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tokens_output": tokens_output,
                "per": per,
            }
        )
        if pool is not UNSET:
            field_dict["pool"] = pool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tokens_output = d.pop("tokens_output")

        per = ConfigInputLimitType3Per(d.pop("per"))

        pool = d.pop("pool", UNSET)

        if d:
            raise ValueError("Unexpected fields for ConfigInputLimitType3")
        config_input_limit_type_3 = cls(
            tokens_output=tokens_output,
            per=per,
            pool=pool,
        )

        return config_input_limit_type_3
