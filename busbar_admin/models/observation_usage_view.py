from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.observation_usage_view_counts import ObservationUsageViewCounts


T = TypeVar("T", bound="ObservationUsageView")


@_attrs_define(repr=False)
class ObservationUsageView:
    """An authoritative dated observation total. Decimal strings preserve exact numeric values
    in clients whose JSON number representation cannot represent every integer or decimal.

        Attributes:
            key_id (str):
            group (str):
            instance (str):
            destination (str):
            serving_subject (str):
            rated_subject (str):
            accounting_time (str): Original accounting time, as an exact epoch-seconds integer string.
            counts (ObservationUsageViewCounts): Disjoint raw class counts, as canonical decimal strings. No derived parents
                are inserted.
            spend_micros (str): Committed spend in micro-units, as an exact decimal string (up to three fractional places).
    """

    key_id: str
    group: str
    instance: str
    destination: str
    serving_subject: str
    rated_subject: str
    accounting_time: str
    counts: ObservationUsageViewCounts
    spend_micros: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key_id = self.key_id

        group = self.group

        instance = self.instance

        destination = self.destination

        serving_subject = self.serving_subject

        rated_subject = self.rated_subject

        accounting_time = self.accounting_time

        counts = self.counts.to_dict()

        spend_micros = self.spend_micros

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key_id": key_id,
                "group": group,
                "instance": instance,
                "destination": destination,
                "serving_subject": serving_subject,
                "rated_subject": rated_subject,
                "accounting_time": accounting_time,
                "counts": counts,
                "spend_micros": spend_micros,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.observation_usage_view_counts import ObservationUsageViewCounts  # noqa: PLC0415

        d = dict(src_dict)
        key_id = d.pop("key_id")

        group = d.pop("group")

        instance = d.pop("instance")

        destination = d.pop("destination")

        serving_subject = d.pop("serving_subject")

        rated_subject = d.pop("rated_subject")

        accounting_time = d.pop("accounting_time")

        counts = ObservationUsageViewCounts.from_dict(d.pop("counts"))

        spend_micros = d.pop("spend_micros")

        observation_usage_view = cls(
            key_id=key_id,
            group=group,
            instance=instance,
            destination=destination,
            serving_subject=serving_subject,
            rated_subject=rated_subject,
            accounting_time=accounting_time,
            counts=counts,
            spend_micros=spend_micros,
        )

        observation_usage_view.additional_properties = d
        return observation_usage_view

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
