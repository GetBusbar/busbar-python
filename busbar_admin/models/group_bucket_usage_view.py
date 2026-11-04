from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupBucketUsageView")


@_attrs_define(repr=False)
class GroupBucketUsageView:
    """One `(window, pool?)` enforcement bucket's usage vs caps inside a [`GroupUsageView`].

    Attributes:
        requests (int): Requests admitted this window (the requests-limit truth: failures are not refunded).
        spend_cents (int): Spend derived at read time (tokens x current rate card), abstract cents.
        tokens (int): Total tokens ledgered this window (all tiers).
        window (str): The accounting window: `minute` | `hour` | `day` | `month` | `total`.
        budget_cap (int | None | Unset):
        budget_remaining_cents (int | None | Unset): Cents left under `budget_cap` (floored at 0); absent when no budget
            cap is set.
        pool (None | str | Unset): The pool scope for a pool-qualified bucket; absent for a group-wide bucket.
        requests_cap (int | None | Unset): The bucket's caps, when configured (absent = uncapped on that metric).
        tokens_cache_read_cap (int | None | Unset):
        tokens_cache_write_cap (int | None | Unset):
        tokens_cap (int | None | Unset):
        tokens_input_cap (int | None | Unset): Per-tier token caps mirroring the cost tiers, when configured (absent =
            uncapped on that
            tier): `tokens_input` = uncached input, `tokens_output` = output, `tokens_cache_read`,
            `tokens_cache_write` = cache creation.
        tokens_output_cap (int | None | Unset):
    """

    requests: int
    spend_cents: int
    tokens: int
    window: str
    budget_cap: int | None | Unset = UNSET
    budget_remaining_cents: int | None | Unset = UNSET
    pool: None | str | Unset = UNSET
    requests_cap: int | None | Unset = UNSET
    tokens_cache_read_cap: int | None | Unset = UNSET
    tokens_cache_write_cap: int | None | Unset = UNSET
    tokens_cap: int | None | Unset = UNSET
    tokens_input_cap: int | None | Unset = UNSET
    tokens_output_cap: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requests = self.requests

        spend_cents = self.spend_cents

        tokens = self.tokens

        window = self.window

        budget_cap: int | None | Unset
        if isinstance(self.budget_cap, Unset):
            budget_cap = UNSET
        else:
            budget_cap = self.budget_cap

        budget_remaining_cents: int | None | Unset
        if isinstance(self.budget_remaining_cents, Unset):
            budget_remaining_cents = UNSET
        else:
            budget_remaining_cents = self.budget_remaining_cents

        pool: None | str | Unset
        if isinstance(self.pool, Unset):
            pool = UNSET
        else:
            pool = self.pool

        requests_cap: int | None | Unset
        if isinstance(self.requests_cap, Unset):
            requests_cap = UNSET
        else:
            requests_cap = self.requests_cap

        tokens_cache_read_cap: int | None | Unset
        if isinstance(self.tokens_cache_read_cap, Unset):
            tokens_cache_read_cap = UNSET
        else:
            tokens_cache_read_cap = self.tokens_cache_read_cap

        tokens_cache_write_cap: int | None | Unset
        if isinstance(self.tokens_cache_write_cap, Unset):
            tokens_cache_write_cap = UNSET
        else:
            tokens_cache_write_cap = self.tokens_cache_write_cap

        tokens_cap: int | None | Unset
        if isinstance(self.tokens_cap, Unset):
            tokens_cap = UNSET
        else:
            tokens_cap = self.tokens_cap

        tokens_input_cap: int | None | Unset
        if isinstance(self.tokens_input_cap, Unset):
            tokens_input_cap = UNSET
        else:
            tokens_input_cap = self.tokens_input_cap

        tokens_output_cap: int | None | Unset
        if isinstance(self.tokens_output_cap, Unset):
            tokens_output_cap = UNSET
        else:
            tokens_output_cap = self.tokens_output_cap

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requests": requests,
                "spend_cents": spend_cents,
                "tokens": tokens,
                "window": window,
            }
        )
        if budget_cap is not UNSET:
            field_dict["budget_cap"] = budget_cap
        if budget_remaining_cents is not UNSET:
            field_dict["budget_remaining_cents"] = budget_remaining_cents
        if pool is not UNSET:
            field_dict["pool"] = pool
        if requests_cap is not UNSET:
            field_dict["requests_cap"] = requests_cap
        if tokens_cache_read_cap is not UNSET:
            field_dict["tokens_cache_read_cap"] = tokens_cache_read_cap
        if tokens_cache_write_cap is not UNSET:
            field_dict["tokens_cache_write_cap"] = tokens_cache_write_cap
        if tokens_cap is not UNSET:
            field_dict["tokens_cap"] = tokens_cap
        if tokens_input_cap is not UNSET:
            field_dict["tokens_input_cap"] = tokens_input_cap
        if tokens_output_cap is not UNSET:
            field_dict["tokens_output_cap"] = tokens_output_cap

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        requests = d.pop("requests")

        spend_cents = d.pop("spend_cents")

        tokens = d.pop("tokens")

        window = d.pop("window")

        def _parse_budget_cap(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        budget_cap = _parse_budget_cap(d.pop("budget_cap", UNSET))

        def _parse_budget_remaining_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        budget_remaining_cents = _parse_budget_remaining_cents(d.pop("budget_remaining_cents", UNSET))

        def _parse_pool(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pool = _parse_pool(d.pop("pool", UNSET))

        def _parse_requests_cap(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        requests_cap = _parse_requests_cap(d.pop("requests_cap", UNSET))

        def _parse_tokens_cache_read_cap(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tokens_cache_read_cap = _parse_tokens_cache_read_cap(d.pop("tokens_cache_read_cap", UNSET))

        def _parse_tokens_cache_write_cap(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tokens_cache_write_cap = _parse_tokens_cache_write_cap(d.pop("tokens_cache_write_cap", UNSET))

        def _parse_tokens_cap(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tokens_cap = _parse_tokens_cap(d.pop("tokens_cap", UNSET))

        def _parse_tokens_input_cap(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tokens_input_cap = _parse_tokens_input_cap(d.pop("tokens_input_cap", UNSET))

        def _parse_tokens_output_cap(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tokens_output_cap = _parse_tokens_output_cap(d.pop("tokens_output_cap", UNSET))

        group_bucket_usage_view = cls(
            requests=requests,
            spend_cents=spend_cents,
            tokens=tokens,
            window=window,
            budget_cap=budget_cap,
            budget_remaining_cents=budget_remaining_cents,
            pool=pool,
            requests_cap=requests_cap,
            tokens_cache_read_cap=tokens_cache_read_cap,
            tokens_cache_write_cap=tokens_cache_write_cap,
            tokens_cap=tokens_cap,
            tokens_input_cap=tokens_input_cap,
            tokens_output_cap=tokens_output_cap,
        )

        group_bucket_usage_view.additional_properties = d
        return group_bucket_usage_view

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
