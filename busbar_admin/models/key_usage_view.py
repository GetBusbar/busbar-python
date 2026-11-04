from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_usage_view_classes import KeyUsageViewClasses


T = TypeVar("T", bound="KeyUsageView")


@_attrs_define(repr=False)
class KeyUsageView:
    """One key's row of the per-key aggregation: the key id/name (never the secret) + its counts.

    Attributes:
        id (str):
        name (None | str): The key's display name; `None` when the key was deleted after metering accumulated (history
            outlives the key; the id still attributes it).
        requests (int):
        spend_micros (int): Busbar's derived cost estimate in MICRO-units of the ABSTRACT cost unit (1e-6 unit -
            integer math, sub-cent precise, no float drift), recomputed at read time from the raw token
            split x the operator's CURRENT per-model rate card. Busbar attaches no currency - the rate
            card's numbers are whatever unit the operator priced in; display/denomination is entirely
            the consumer's concern. A consumer with its own per-model catalog recomputes from the raw
            token split instead.
        tokens_cache_creation (int):
        tokens_cache_read (int):
        tokens_input (int): Uncached input tokens (normalized additive-cache convention).
        tokens_output (int):
        classes (KeyUsageViewClasses | Unset): THE PLANE-DECLARED CLASSES the row's ledger lines counted outside the
            token split, keyed by
            the class name the plane declares (new in 1.6.0, [`ClassUsage`]). Absent when the row carries
            none, so a token-only row reads exactly as 1.5.5's.
    """

    id: str
    name: None | str
    requests: int
    spend_micros: int
    tokens_cache_creation: int
    tokens_cache_read: int
    tokens_input: int
    tokens_output: int
    classes: KeyUsageViewClasses | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: None | str
        name = self.name

        requests = self.requests

        spend_micros = self.spend_micros

        tokens_cache_creation = self.tokens_cache_creation

        tokens_cache_read = self.tokens_cache_read

        tokens_input = self.tokens_input

        tokens_output = self.tokens_output

        classes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.classes, Unset):
            classes = self.classes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "requests": requests,
                "spend_micros": spend_micros,
                "tokens_cache_creation": tokens_cache_creation,
                "tokens_cache_read": tokens_cache_read,
                "tokens_input": tokens_input,
                "tokens_output": tokens_output,
            }
        )
        if classes is not UNSET:
            field_dict["classes"] = classes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.key_usage_view_classes import KeyUsageViewClasses  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        requests = d.pop("requests")

        spend_micros = d.pop("spend_micros")

        tokens_cache_creation = d.pop("tokens_cache_creation")

        tokens_cache_read = d.pop("tokens_cache_read")

        tokens_input = d.pop("tokens_input")

        tokens_output = d.pop("tokens_output")

        _classes = d.pop("classes", UNSET)
        classes: KeyUsageViewClasses | Unset
        if isinstance(_classes, Unset):
            classes = UNSET
        else:
            classes = KeyUsageViewClasses.from_dict(_classes)

        key_usage_view = cls(
            id=id,
            name=name,
            requests=requests,
            spend_micros=spend_micros,
            tokens_cache_creation=tokens_cache_creation,
            tokens_cache_read=tokens_cache_read,
            tokens_input=tokens_input,
            tokens_output=tokens_output,
            classes=classes,
        )

        key_usage_view.additional_properties = d
        return key_usage_view

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
