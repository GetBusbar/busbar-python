from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UsageBreakdown")


@_attrs_define
class UsageBreakdown:
    """The raw consumption counts + the derived spend estimate — the one shape shared by `total`,
    `by_model` rows, and `by_key` rows, so a consumer writes ONE aggregation reader.

        Attributes:
            requests (int):
            spend_micros (int): Busbar's derived cost estimate in MICRO-units of `currency` (1e-6 USD — integer math,
                sub-cent precise, no float drift), from the operator's configured global prices. A consumer
                with its own per-model catalog recomputes from the raw token split instead.
            tokens_cache_creation (int):
            tokens_cache_read (int):
            tokens_input (int): Uncached input tokens (normalized additive-cache convention).
            tokens_output (int):
    """

    requests: int
    spend_micros: int
    tokens_cache_creation: int
    tokens_cache_read: int
    tokens_input: int
    tokens_output: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requests = self.requests

        spend_micros = self.spend_micros

        tokens_cache_creation = self.tokens_cache_creation

        tokens_cache_read = self.tokens_cache_read

        tokens_input = self.tokens_input

        tokens_output = self.tokens_output

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requests": requests,
                "spend_micros": spend_micros,
                "tokens_cache_creation": tokens_cache_creation,
                "tokens_cache_read": tokens_cache_read,
                "tokens_input": tokens_input,
                "tokens_output": tokens_output,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        requests = d.pop("requests")

        spend_micros = d.pop("spend_micros")

        tokens_cache_creation = d.pop("tokens_cache_creation")

        tokens_cache_read = d.pop("tokens_cache_read")

        tokens_input = d.pop("tokens_input")

        tokens_output = d.pop("tokens_output")

        usage_breakdown = cls(
            requests=requests,
            spend_micros=spend_micros,
            tokens_cache_creation=tokens_cache_creation,
            tokens_cache_read=tokens_cache_read,
            tokens_input=tokens_input,
            tokens_output=tokens_output,
        )

        usage_breakdown.additional_properties = d
        return usage_breakdown

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
