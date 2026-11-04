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
        adjustments (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit integers
            and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        bucket (str):
        budget (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit integers and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        cross_window_transfers (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in
            128-bit integers and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        dimension (str):
        disputed (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit integers
            and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        drawn (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit integers and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        oldest_dispute_age_secs (int):
        oldest_open_hold_age_secs (int):
        open_dispute_count (int):
        open_holds (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit integers
            and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        open_slice_remainders (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in
            128-bit integers and
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
        released (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit integers
            and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        scope (str):
        settled (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit integers and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        unreconciled (str): A money figure: a decimal integer carried as TEXT. The ledger keeps money in 128-bit
            integers and
            JSON's number is a double, exact only to 2^53; a nano-unit total passes that on a busy day, and a
            figure that silently lost its last digits would still look like money.
        window (int): The window's opening instant, in whole seconds.
    """

    adjustments: str
    bucket: str
    budget: str
    cross_window_transfers: str
    dimension: str
    disputed: str
    drawn: str
    oldest_dispute_age_secs: int
    oldest_open_hold_age_secs: int
    open_dispute_count: int
    open_holds: str
    open_slice_remainders: str
    overdraft_carried_in: str
    overdraft_carried_out: str
    released: str
    scope: str
    settled: str
    unreconciled: str
    window: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adjustments = self.adjustments

        bucket = self.bucket

        budget = self.budget

        cross_window_transfers = self.cross_window_transfers

        dimension = self.dimension

        disputed = self.disputed

        drawn = self.drawn

        oldest_dispute_age_secs = self.oldest_dispute_age_secs

        oldest_open_hold_age_secs = self.oldest_open_hold_age_secs

        open_dispute_count = self.open_dispute_count

        open_holds = self.open_holds

        open_slice_remainders = self.open_slice_remainders

        overdraft_carried_in = self.overdraft_carried_in

        overdraft_carried_out = self.overdraft_carried_out

        released = self.released

        scope = self.scope

        settled = self.settled

        unreconciled = self.unreconciled

        window = self.window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "adjustments": adjustments,
                "bucket": bucket,
                "budget": budget,
                "cross_window_transfers": cross_window_transfers,
                "dimension": dimension,
                "disputed": disputed,
                "drawn": drawn,
                "oldest_dispute_age_secs": oldest_dispute_age_secs,
                "oldest_open_hold_age_secs": oldest_open_hold_age_secs,
                "open_dispute_count": open_dispute_count,
                "open_holds": open_holds,
                "open_slice_remainders": open_slice_remainders,
                "overdraft_carried_in": overdraft_carried_in,
                "overdraft_carried_out": overdraft_carried_out,
                "released": released,
                "scope": scope,
                "settled": settled,
                "unreconciled": unreconciled,
                "window": window,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        adjustments = d.pop("adjustments")

        bucket = d.pop("bucket")

        budget = d.pop("budget")

        cross_window_transfers = d.pop("cross_window_transfers")

        dimension = d.pop("dimension")

        disputed = d.pop("disputed")

        drawn = d.pop("drawn")

        oldest_dispute_age_secs = d.pop("oldest_dispute_age_secs")

        oldest_open_hold_age_secs = d.pop("oldest_open_hold_age_secs")

        open_dispute_count = d.pop("open_dispute_count")

        open_holds = d.pop("open_holds")

        open_slice_remainders = d.pop("open_slice_remainders")

        overdraft_carried_in = d.pop("overdraft_carried_in")

        overdraft_carried_out = d.pop("overdraft_carried_out")

        released = d.pop("released")

        scope = d.pop("scope")

        settled = d.pop("settled")

        unreconciled = d.pop("unreconciled")

        window = d.pop("window")

        ledger_totals_cell = cls(
            adjustments=adjustments,
            bucket=bucket,
            budget=budget,
            cross_window_transfers=cross_window_transfers,
            dimension=dimension,
            disputed=disputed,
            drawn=drawn,
            oldest_dispute_age_secs=oldest_dispute_age_secs,
            oldest_open_hold_age_secs=oldest_open_hold_age_secs,
            open_dispute_count=open_dispute_count,
            open_holds=open_holds,
            open_slice_remainders=open_slice_remainders,
            overdraft_carried_in=overdraft_carried_in,
            overdraft_carried_out=overdraft_carried_out,
            released=released,
            scope=scope,
            settled=settled,
            unreconciled=unreconciled,
            window=window,
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
