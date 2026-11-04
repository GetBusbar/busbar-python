from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ledger_residual import LedgerResidual


T = TypeVar("T", bound="LedgerDiscrepancy")


@_attrs_define(repr=False)
class LedgerDiscrepancy:
    """One row on which the identity does not hold. Spend and fee count are checked separately
    because they fail separately.

        Attributes:
            bucket (str):
            day (int):
            lane (str):
            ledger_fee_count (int): What the ledger's postings charged fees for on this row.
            legacy_billable_requests (int): What the previous release's row says was billable.
            provider (str):
            residual (LedgerResidual): The spend residual of one row.
    """

    bucket: str
    day: int
    lane: str
    ledger_fee_count: int
    legacy_billable_requests: int
    provider: str
    residual: LedgerResidual
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        day = self.day

        lane = self.lane

        ledger_fee_count = self.ledger_fee_count

        legacy_billable_requests = self.legacy_billable_requests

        provider = self.provider

        residual = self.residual.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket": bucket,
                "day": day,
                "lane": lane,
                "ledger_fee_count": ledger_fee_count,
                "legacy_billable_requests": legacy_billable_requests,
                "provider": provider,
                "residual": residual,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ledger_residual import LedgerResidual  # noqa: PLC0415

        d = dict(src_dict)
        bucket = d.pop("bucket")

        day = d.pop("day")

        lane = d.pop("lane")

        ledger_fee_count = d.pop("ledger_fee_count")

        legacy_billable_requests = d.pop("legacy_billable_requests")

        provider = d.pop("provider")

        residual = LedgerResidual.from_dict(d.pop("residual"))

        ledger_discrepancy = cls(
            bucket=bucket,
            day=day,
            lane=lane,
            ledger_fee_count=ledger_fee_count,
            legacy_billable_requests=legacy_billable_requests,
            provider=provider,
            residual=residual,
        )

        ledger_discrepancy.additional_properties = d
        return ledger_discrepancy

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
