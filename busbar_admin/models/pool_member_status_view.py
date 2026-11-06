from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PoolMemberStatusView")


@_attrs_define(repr=False)
class PoolMemberStatusView:
    """One member's live status within a pool. The breaker signal is the release-exposed
    `usable`/`cooldown_remaining_seconds` pair (a lane in breaker cooldown reports `usable: false` with the
    seconds remaining), the same summary `/stats` surfaces.

        Attributes:
            model (str):
            weight (int):
            usable (bool): Whether the lane can currently take dispatch (breaker closed / recovered). `false` while a
                tripped breaker cools down or the lane is dead.
            cooldown_remaining_seconds (int): Seconds until a tripped breaker's cooldown elapses; `0` when not cooling down.
                (`_seconds`
                suffix: the one unit-suffix spelling across the surface, like `uptime_seconds`.)
            available_concurrency (int): Free concurrency slots on this lane right now (lane-global; permits are shared
                across pools).
            inflight (int): In-flight requests on this lane right now.
            latency_ms (float | None): Latency EWMA in milliseconds, or `None` if no sample yet.
            ok (int): Successful and errored request tallies for this lane.
            err (int):
            dead (bool): Whether the lane is hard-down/dead (distinct from a transiently-tripped breaker).
            trip_count (int): MONOTONIC count of Closed→Open breaker trips on this lane. Breaker episodes are transient
                and can open+close entirely between two polls, so a consumer alerting on trips diffs this
                count instead of trying to catch the live edge. Carried across config apply and
                restart with the rest of the learned health.
            last_trip_at (int | None): Epoch seconds of the most recent trip; `None` = never tripped.
    """

    model: str
    weight: int
    usable: bool
    cooldown_remaining_seconds: int
    available_concurrency: int
    inflight: int
    latency_ms: float | None
    ok: int
    err: int
    dead: bool
    trip_count: int
    last_trip_at: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        weight = self.weight

        usable = self.usable

        cooldown_remaining_seconds = self.cooldown_remaining_seconds

        available_concurrency = self.available_concurrency

        inflight = self.inflight

        latency_ms: float | None
        latency_ms = self.latency_ms

        ok = self.ok

        err = self.err

        dead = self.dead

        trip_count = self.trip_count

        last_trip_at: int | None
        last_trip_at = self.last_trip_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "weight": weight,
                "usable": usable,
                "cooldown_remaining_seconds": cooldown_remaining_seconds,
                "available_concurrency": available_concurrency,
                "inflight": inflight,
                "latency_ms": latency_ms,
                "ok": ok,
                "err": err,
                "dead": dead,
                "trip_count": trip_count,
                "last_trip_at": last_trip_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model")

        weight = d.pop("weight")

        usable = d.pop("usable")

        cooldown_remaining_seconds = d.pop("cooldown_remaining_seconds")

        available_concurrency = d.pop("available_concurrency")

        inflight = d.pop("inflight")

        def _parse_latency_ms(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        latency_ms = _parse_latency_ms(d.pop("latency_ms"))

        ok = d.pop("ok")

        err = d.pop("err")

        dead = d.pop("dead")

        trip_count = d.pop("trip_count")

        def _parse_last_trip_at(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        last_trip_at = _parse_last_trip_at(d.pop("last_trip_at"))

        pool_member_status_view = cls(
            model=model,
            weight=weight,
            usable=usable,
            cooldown_remaining_seconds=cooldown_remaining_seconds,
            available_concurrency=available_concurrency,
            inflight=inflight,
            latency_ms=latency_ms,
            ok=ok,
            err=err,
            dead=dead,
            trip_count=trip_count,
            last_trip_at=last_trip_at,
        )

        pool_member_status_view.additional_properties = d
        return pool_member_status_view

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
