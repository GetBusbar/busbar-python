from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amend_rate_row import AmendRateRow


T = TypeVar("T", bound="AmendRateHistoryReq")


@_attrs_define(repr=False)
class AmendRateHistoryReq:
    """`POST /ledger/amend-rate-history`: a back-dated correction to the dated rate-card
    history. It out-ranks the entry it corrects and rewrites nothing.

        Attributes:
            effective_from (int): The start of the corrected window, in the history's instant scale (milliseconds).
            reason (str): Why. Required and non-empty; the record keeps its SHA-256, not the text.
            effective_until (int | None | Unset): The end of the corrected window; when present it must lie strictly after
                `effective_from`. Absent or null: open-ended.
            per_request_fee (int | None | Unset): The corrected flat per-request fee. Never negative.
            rates (list[AmendRateRow] | Unset): The corrected rates. A correction must move at least one figure: a rate here
                or the fee.
    """

    effective_from: int
    reason: str
    effective_until: int | None | Unset = UNSET
    per_request_fee: int | None | Unset = UNSET
    rates: list[AmendRateRow] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        effective_from = self.effective_from

        reason = self.reason

        effective_until: int | None | Unset
        if isinstance(self.effective_until, Unset):
            effective_until = UNSET
        else:
            effective_until = self.effective_until

        per_request_fee: int | None | Unset
        if isinstance(self.per_request_fee, Unset):
            per_request_fee = UNSET
        else:
            per_request_fee = self.per_request_fee

        rates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rates, Unset):
            rates = []
            for rates_item_data in self.rates:
                rates_item = rates_item_data.to_dict()
                rates.append(rates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "effective_from": effective_from,
                "reason": reason,
            }
        )
        if effective_until is not UNSET:
            field_dict["effective_until"] = effective_until
        if per_request_fee is not UNSET:
            field_dict["per_request_fee"] = per_request_fee
        if rates is not UNSET:
            field_dict["rates"] = rates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amend_rate_row import AmendRateRow  # noqa: PLC0415

        d = dict(src_dict)
        effective_from = d.pop("effective_from")

        reason = d.pop("reason")

        def _parse_effective_until(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        effective_until = _parse_effective_until(d.pop("effective_until", UNSET))

        def _parse_per_request_fee(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        per_request_fee = _parse_per_request_fee(d.pop("per_request_fee", UNSET))

        _rates = d.pop("rates", UNSET)
        rates: list[AmendRateRow] | Unset = UNSET
        if _rates is not UNSET:
            rates = []
            for rates_item_data in _rates:
                rates_item = AmendRateRow.from_dict(rates_item_data)

                rates.append(rates_item)

        amend_rate_history_req = cls(
            effective_from=effective_from,
            reason=reason,
            effective_until=effective_until,
            per_request_fee=per_request_fee,
            rates=rates,
        )

        amend_rate_history_req.additional_properties = d
        return amend_rate_history_req

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
