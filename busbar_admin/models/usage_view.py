from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_usage_view import KeyUsageView
    from ..models.model_usage_view import ModelUsageView
    from ..models.usage_breakdown import UsageBreakdown
    from ..models.usage_window import UsageWindow


T = TypeVar("T", bound="UsageView")


@_attrs_define
class UsageView:
    """
    Attributes:
        as_of (int): Freshness marker: the epoch this read was computed at (counters accumulate live).
        by_key (list[KeyUsageView]): Per-key aggregation (same raw-split shape). CAPPED at the top 1000 rows by spend
            (the
            FinOps-relevant ordering); `by_key_truncated` says the cap fired — never a silent cut.
        by_key_truncated (bool): True when `by_key` was truncated to the cap (a deployment with more active keys than
            the
            cap). `by_model` is never capped (bounded by the configured model fleet).
        by_model (list[ModelUsageView]): Per-(model, provider) aggregation — cost attribution by model (the FinOps
            unit).
        currency (str): The denomination of every `spend_micros` in this response (`USAGE_CURRENCY`, currently
            `"USD"`). A single-const source of truth so removal is one line. Emitted only here.
        total (UsageBreakdown): The raw consumption counts + the derived spend estimate — the one shape shared by
            `total`,
            `by_model` rows, and `by_key` rows, so a consumer writes ONE aggregation reader.
        window (UsageWindow): A metering window: `[start, end)` epoch seconds.
        others (None | Unset | UsageBreakdown): The summed remainder BEYOND the `by_key` cap — present exactly when
            `by_key_truncated`, so
            every unit of consumption is attributable at least to "others" (FinOps completeness:
            `total == sum(by_key) + others`).
    """

    as_of: int
    by_key: list[KeyUsageView]
    by_key_truncated: bool
    by_model: list[ModelUsageView]
    currency: str
    total: UsageBreakdown
    window: UsageWindow
    others: None | Unset | UsageBreakdown = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.usage_breakdown import UsageBreakdown

        as_of = self.as_of

        by_key = []
        for by_key_item_data in self.by_key:
            by_key_item = by_key_item_data.to_dict()
            by_key.append(by_key_item)

        by_key_truncated = self.by_key_truncated

        by_model = []
        for by_model_item_data in self.by_model:
            by_model_item = by_model_item_data.to_dict()
            by_model.append(by_model_item)

        currency = self.currency

        total = self.total.to_dict()

        window = self.window.to_dict()

        others: dict[str, Any] | None | Unset
        if isinstance(self.others, Unset):
            others = UNSET
        elif isinstance(self.others, UsageBreakdown):
            others = self.others.to_dict()
        else:
            others = self.others

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "as_of": as_of,
                "by_key": by_key,
                "by_key_truncated": by_key_truncated,
                "by_model": by_model,
                "currency": currency,
                "total": total,
                "window": window,
            }
        )
        if others is not UNSET:
            field_dict["others"] = others

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.key_usage_view import KeyUsageView
        from ..models.model_usage_view import ModelUsageView
        from ..models.usage_breakdown import UsageBreakdown
        from ..models.usage_window import UsageWindow

        d = dict(src_dict)
        as_of = d.pop("as_of")

        by_key = []
        _by_key = d.pop("by_key")
        for by_key_item_data in _by_key:
            by_key_item = KeyUsageView.from_dict(by_key_item_data)

            by_key.append(by_key_item)

        by_key_truncated = d.pop("by_key_truncated")

        by_model = []
        _by_model = d.pop("by_model")
        for by_model_item_data in _by_model:
            by_model_item = ModelUsageView.from_dict(by_model_item_data)

            by_model.append(by_model_item)

        currency = d.pop("currency")

        total = UsageBreakdown.from_dict(d.pop("total"))

        window = UsageWindow.from_dict(d.pop("window"))

        def _parse_others(data: object) -> None | Unset | UsageBreakdown:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                others_type_0 = UsageBreakdown.from_dict(data)

                return others_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UsageBreakdown, data)

        others = _parse_others(d.pop("others", UNSET))

        usage_view = cls(
            as_of=as_of,
            by_key=by_key,
            by_key_truncated=by_key_truncated,
            by_model=by_model,
            currency=currency,
            total=total,
            window=window,
            others=others,
        )

        usage_view.additional_properties = d
        return usage_view

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
