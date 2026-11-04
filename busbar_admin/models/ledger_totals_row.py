from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LedgerTotalsRow")


@_attrs_define(repr=False)
class LedgerTotalsRow:
    """One row of `GET /ledger/totals`. The row width is the reconciliation's, so a discrepancy found
    on one endpoint is looked up on the other by the same four-part name.

        Attributes:
            bucket (str): Whose budget the usage was attributed to.
            day (int): The UTC-day bucket, as the unix second it opens at.
            fee_count (int): One per billable client request on this row.
            lane (str): The serving lane's configured model name (empty where the node keeps no finer width).
            priced_micros (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit
                integers and
                JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
                figure that silently lost its last digits would still look like money.
            priced_nanos (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit
                integers and
                JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
                figure that silently lost its last digits would still look like money.
            provider (str): The serving lane's provider (empty where the node keeps no finer width).
    """

    bucket: str
    day: int
    fee_count: int
    lane: str
    priced_micros: str
    priced_nanos: str
    provider: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        day = self.day

        fee_count = self.fee_count

        lane = self.lane

        priced_micros = self.priced_micros

        priced_nanos = self.priced_nanos

        provider = self.provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket": bucket,
                "day": day,
                "fee_count": fee_count,
                "lane": lane,
                "priced_micros": priced_micros,
                "priced_nanos": priced_nanos,
                "provider": provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket = d.pop("bucket")

        day = d.pop("day")

        fee_count = d.pop("fee_count")

        lane = d.pop("lane")

        priced_micros = d.pop("priced_micros")

        priced_nanos = d.pop("priced_nanos")

        provider = d.pop("provider")

        ledger_totals_row = cls(
            bucket=bucket,
            day=day,
            fee_count=fee_count,
            lane=lane,
            priced_micros=priced_micros,
            priced_nanos=priced_nanos,
            provider=provider,
        )

        ledger_totals_row.additional_properties = d
        return ledger_totals_row

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
