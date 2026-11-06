from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.config_input_limit_type_2_per import ConfigInputLimitType2Per
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigInputLimitType2")


@_attrs_define(repr=False)
class ConfigInputLimitType2:
    """
    Attributes:
        tokens_input (int):
        per (ConfigInputLimitType2Per):
        pool (str | Unset):
    """

    tokens_input: int
    per: ConfigInputLimitType2Per
    pool: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tokens_input = self.tokens_input

        per = self.per.value

        pool = self.pool

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tokens_input": tokens_input,
                "per": per,
            }
        )
        if pool is not UNSET:
            field_dict["pool"] = pool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tokens_input = d.pop("tokens_input")

        per = ConfigInputLimitType2Per(d.pop("per"))

        pool = d.pop("pool", UNSET)

        if d:
            raise ValueError("Unexpected fields for ConfigInputLimitType2")
        config_input_limit_type_2 = cls(
            tokens_input=tokens_input,
            per=per,
            pool=pool,
        )

        return config_input_limit_type_2
