from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_usage_view_classes import ModelUsageViewClasses


T = TypeVar("T", bound="ModelUsageView")


@_attrs_define(repr=False)
class ModelUsageView:
    """One (model, provider) row of the per-model aggregation.

    Attributes:
        model (str):
        provider (str):
        tokens_input (float): Uncached input tokens (normalized additive-cache convention).
        tokens_output (float):
        tokens_cache_read (float):
        tokens_cache_creation (float):
        requests (int):
        spend_micros (int): Busbar's derived cost estimate in MICRO-units of the ABSTRACT cost unit (1e-6 unit -
            integer math, sub-cent precise, no float drift), recomputed at read time from the raw token
            split x the operator's CURRENT per-model rate card. Busbar attaches no currency - the rate
            card's numbers are whatever unit the operator priced in; display/denomination is entirely
            the consumer's concern. A consumer with its own per-model catalog recomputes from the raw
            token split instead.
        classes (ModelUsageViewClasses | Unset): Every ledgered class outside the reserved token split, keyed by class
            name ([`ClassUsage`]).
            Includes open classes from every provider and plane. Absent when the row carries none.
    """

    model: str
    provider: str
    tokens_input: float
    tokens_output: float
    tokens_cache_read: float
    tokens_cache_creation: float
    requests: int
    spend_micros: int
    classes: ModelUsageViewClasses | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        provider = self.provider

        tokens_input = self.tokens_input

        tokens_output = self.tokens_output

        tokens_cache_read = self.tokens_cache_read

        tokens_cache_creation = self.tokens_cache_creation

        requests = self.requests

        spend_micros = self.spend_micros

        classes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.classes, Unset):
            classes = self.classes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "provider": provider,
                "tokens_input": tokens_input,
                "tokens_output": tokens_output,
                "tokens_cache_read": tokens_cache_read,
                "tokens_cache_creation": tokens_cache_creation,
                "requests": requests,
                "spend_micros": spend_micros,
            }
        )
        if classes is not UNSET:
            field_dict["classes"] = classes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_usage_view_classes import ModelUsageViewClasses  # noqa: PLC0415

        d = dict(src_dict)
        model = d.pop("model")

        provider = d.pop("provider")

        tokens_input = d.pop("tokens_input")

        tokens_output = d.pop("tokens_output")

        tokens_cache_read = d.pop("tokens_cache_read")

        tokens_cache_creation = d.pop("tokens_cache_creation")

        requests = d.pop("requests")

        spend_micros = d.pop("spend_micros")

        _classes = d.pop("classes", UNSET)
        classes: ModelUsageViewClasses | Unset
        if isinstance(_classes, Unset):
            classes = UNSET
        else:
            classes = ModelUsageViewClasses.from_dict(_classes)

        model_usage_view = cls(
            model=model,
            provider=provider,
            tokens_input=tokens_input,
            tokens_output=tokens_output,
            tokens_cache_read=tokens_cache_read,
            tokens_cache_creation=tokens_cache_creation,
            requests=requests,
            spend_micros=spend_micros,
            classes=classes,
        )

        model_usage_view.additional_properties = d
        return model_usage_view

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
