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
            lane (str): The serving lane's configured model name (empty where the node keeps no finer width).
            provider (str): The serving lane's provider (empty where the node keeps no finer width).
            priced_nanos (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit
                integers and
                JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
                figure that silently lost its last digits would still look like money.
            priced_micros (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit
                integers and
                JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
                figure that silently lost its last digits would still look like money.
            fee_count (int): One per billable client request on this row.
    """

    bucket: str
    day: int
    lane: str
    provider: str
    priced_nanos: str
    priced_micros: str
    fee_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        day = self.day

        lane = self.lane

        provider = self.provider

        priced_nanos = self.priced_nanos

        priced_micros = self.priced_micros

        fee_count = self.fee_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket": bucket,
                "day": day,
                "lane": lane,
                "provider": provider,
                "priced_nanos": priced_nanos,
                "priced_micros": priced_micros,
                "fee_count": fee_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket = d.pop("bucket")

        day = d.pop("day")

        lane = d.pop("lane")

        provider = d.pop("provider")

        priced_nanos = d.pop("priced_nanos")

        priced_micros = d.pop("priced_micros")

        fee_count = d.pop("fee_count")

        ledger_totals_row = cls(
            bucket=bucket,
            day=day,
            lane=lane,
            provider=provider,
            priced_nanos=priced_nanos,
            priced_micros=priced_micros,
            fee_count=fee_count,
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
