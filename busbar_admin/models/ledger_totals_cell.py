from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LedgerTotalsCell")


@_attrs_define(repr=False)
class LedgerTotalsCell:
    """One sealed balance, as the checkpoint holds it. Every money figure is an [`Amount`].

    Attributes:
        bucket (str):
        dimension (str):
        scope (str):
        window (int): The window's opening instant, in whole seconds.
        budget (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit integers and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        drawn (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit integers and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        released (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit integers
            and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        settled (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit integers and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        open_holds (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit integers
            and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        open_slice_remainders (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in
            128-bit integers and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        adjustments (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit integers
            and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        unreconciled (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit
            integers and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        overdraft_carried_in (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit
            integers and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        overdraft_carried_out (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in
            128-bit integers and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        cross_window_transfers (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in
            128-bit integers and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        disputed (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit integers
            and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        oldest_open_hold_age_secs (int):
        open_dispute_count (int):
        oldest_dispute_age_secs (int):
    """

    bucket: str
    dimension: str
    scope: str
    window: int
    budget: str
    drawn: str
    released: str
    settled: str
    open_holds: str
    open_slice_remainders: str
    adjustments: str
    unreconciled: str
    overdraft_carried_in: str
    overdraft_carried_out: str
    cross_window_transfers: str
    disputed: str
    oldest_open_hold_age_secs: int
    open_dispute_count: int
    oldest_dispute_age_secs: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        dimension = self.dimension

        scope = self.scope

        window = self.window

        budget = self.budget

        drawn = self.drawn

        released = self.released

        settled = self.settled

        open_holds = self.open_holds

        open_slice_remainders = self.open_slice_remainders

        adjustments = self.adjustments

        unreconciled = self.unreconciled

        overdraft_carried_in = self.overdraft_carried_in

        overdraft_carried_out = self.overdraft_carried_out

        cross_window_transfers = self.cross_window_transfers

        disputed = self.disputed

        oldest_open_hold_age_secs = self.oldest_open_hold_age_secs

        open_dispute_count = self.open_dispute_count

        oldest_dispute_age_secs = self.oldest_dispute_age_secs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket": bucket,
                "dimension": dimension,
                "scope": scope,
                "window": window,
                "budget": budget,
                "drawn": drawn,
                "released": released,
                "settled": settled,
                "open_holds": open_holds,
                "open_slice_remainders": open_slice_remainders,
                "adjustments": adjustments,
                "unreconciled": unreconciled,
                "overdraft_carried_in": overdraft_carried_in,
                "overdraft_carried_out": overdraft_carried_out,
                "cross_window_transfers": cross_window_transfers,
                "disputed": disputed,
                "oldest_open_hold_age_secs": oldest_open_hold_age_secs,
                "open_dispute_count": open_dispute_count,
                "oldest_dispute_age_secs": oldest_dispute_age_secs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket = d.pop("bucket")

        dimension = d.pop("dimension")

        scope = d.pop("scope")

        window = d.pop("window")

        budget = d.pop("budget")

        drawn = d.pop("drawn")

        released = d.pop("released")

        settled = d.pop("settled")

        open_holds = d.pop("open_holds")

        open_slice_remainders = d.pop("open_slice_remainders")

        adjustments = d.pop("adjustments")

        unreconciled = d.pop("unreconciled")

        overdraft_carried_in = d.pop("overdraft_carried_in")

        overdraft_carried_out = d.pop("overdraft_carried_out")

        cross_window_transfers = d.pop("cross_window_transfers")

        disputed = d.pop("disputed")

        oldest_open_hold_age_secs = d.pop("oldest_open_hold_age_secs")

        open_dispute_count = d.pop("open_dispute_count")

        oldest_dispute_age_secs = d.pop("oldest_dispute_age_secs")

        ledger_totals_cell = cls(
            bucket=bucket,
            dimension=dimension,
            scope=scope,
            window=window,
            budget=budget,
            drawn=drawn,
            released=released,
            settled=settled,
            open_holds=open_holds,
            open_slice_remainders=open_slice_remainders,
            adjustments=adjustments,
            unreconciled=unreconciled,
            overdraft_carried_in=overdraft_carried_in,
            overdraft_carried_out=overdraft_carried_out,
            cross_window_transfers=cross_window_transfers,
            disputed=disputed,
            oldest_open_hold_age_secs=oldest_open_hold_age_secs,
            open_dispute_count=open_dispute_count,
            oldest_dispute_age_secs=oldest_dispute_age_secs,
        )

        ledger_totals_cell.additional_properties = d
        return ledger_totals_cell

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
