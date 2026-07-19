from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PoolMemberStatusView")


@_attrs_define
class PoolMemberStatusView:
    """One member's live status within a pool. The breaker signal is the release-exposed
    `usable`/`cooldown_remaining_seconds` pair (a lane in breaker cooldown reports `usable: false` with the
    seconds remaining) — the same summary `/stats` surfaces.

        Attributes:
            available_concurrency (int): Free concurrency slots on this lane right now (lane-global; permits are shared
                across pools).
            cooldown_remaining_seconds (int): Seconds until a tripped breaker's cooldown elapses; `0` when not cooling down.
                (`_seconds`
                suffix — the one unit-suffix spelling across the surface, like `uptime_seconds`.)
            dead (bool): Whether the lane is hard-down/dead (distinct from a transiently-tripped breaker).
            err (int):
            inflight (int): In-flight requests on this lane right now.
            last_trip_at (int | None): Epoch seconds of the most recent trip; `None` = never tripped.
            latency_ms (float | None): Latency EWMA in milliseconds, or `None` if no sample yet.
            model (str):
            ok (int): Successful and errored request tallies for this lane.
            trip_count (int): MONOTONIC count of Closed→Open breaker trips on this lane. Breaker episodes are transient
                and can open+close entirely between two polls — a consumer alerting on trips diffs this
                count instead of trying to catch the live edge (audit #5). Carried across config apply and
                restart with the rest of the learned health.
            usable (bool): Whether the lane can currently take dispatch (breaker closed / recovered). `false` while a
                tripped breaker cools down or the lane is dead.
            weight (int):
    """

    available_concurrency: int
    cooldown_remaining_seconds: int
    dead: bool
    err: int
    inflight: int
    last_trip_at: int | None
    latency_ms: float | None
    model: str
    ok: int
    trip_count: int
    usable: bool
    weight: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_concurrency = self.available_concurrency

        cooldown_remaining_seconds = self.cooldown_remaining_seconds

        dead = self.dead

        err = self.err

        inflight = self.inflight

        last_trip_at: int | None
        last_trip_at = self.last_trip_at

        latency_ms: float | None
        latency_ms = self.latency_ms

        model = self.model

        ok = self.ok

        trip_count = self.trip_count

        usable = self.usable

        weight = self.weight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "available_concurrency": available_concurrency,
                "cooldown_remaining_seconds": cooldown_remaining_seconds,
                "dead": dead,
                "err": err,
                "inflight": inflight,
                "last_trip_at": last_trip_at,
                "latency_ms": latency_ms,
                "model": model,
                "ok": ok,
                "trip_count": trip_count,
                "usable": usable,
                "weight": weight,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available_concurrency = d.pop("available_concurrency")

        cooldown_remaining_seconds = d.pop("cooldown_remaining_seconds")

        dead = d.pop("dead")

        err = d.pop("err")

        inflight = d.pop("inflight")

        def _parse_last_trip_at(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        last_trip_at = _parse_last_trip_at(d.pop("last_trip_at"))

        def _parse_latency_ms(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        latency_ms = _parse_latency_ms(d.pop("latency_ms"))

        model = d.pop("model")

        ok = d.pop("ok")

        trip_count = d.pop("trip_count")

        usable = d.pop("usable")

        weight = d.pop("weight")

        pool_member_status_view = cls(
            available_concurrency=available_concurrency,
            cooldown_remaining_seconds=cooldown_remaining_seconds,
            dead=dead,
            err=err,
            inflight=inflight,
            last_trip_at=last_trip_at,
            latency_ms=latency_ms,
            model=model,
            ok=ok,
            trip_count=trip_count,
            usable=usable,
            weight=weight,
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
