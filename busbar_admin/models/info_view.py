from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.build_info import BuildInfo
    from ..models.topology_info import TopologyInfo


T = TypeVar("T", bound="InfoView")


@_attrs_define
class InfoView:
    """The compiled-in plugin catalog + topology + uptime returned by `GET /api/v1/admin/info`. Powers
    version negotiation for tooling AND the compliance-by-compilation proof: `auth_modules`/`hook_plugins` reflect
    the ACTUAL binary (feature-gated at compile time), not config, so `--no-default-features` shows a
    provably smaller surface. No LLM content, ever.

        Attributes:
            build (BuildInfo): The compiled-in feature proof (`InfoView.build`).
            config_persistence (bool): Whether config-overlay persistence is enabled, i.e. the config is MUTABLE with a
                writable
                `config.overlay` backend: `true` = API-applied config changes are durable across restarts;
                `false` = the config is LOCKED (`config.locked: true`) and admin-API config mutations are
                refused. Lets tooling tell an operator whether runtime changes are accepted and durable.
            config_version (int): Monotonic config version: `0` at boot, +1 per API config apply. Drift-detection: re-read
                and
                compare to tell whether the running config changed. Process-local (resets on restart).
            started_at (int | None): Epoch seconds of process start, the BOOT EPOCH marker: `config_version` (and any
                process-local counter) resets on restart, so a consumer that sees `started_at` change knows
                to read a counter reset as "new epoch", never as "reverted".
            topology (TopologyInfo): Pool/model/provider counts (`InfoView.topology`).
            uptime_seconds (int | None): Seconds since process start, or `None` if the start instant was never stamped.
            version (str): busbar semantic version (`CARGO_PKG_VERSION`).
    """

    build: BuildInfo
    config_persistence: bool
    config_version: int
    started_at: int | None
    topology: TopologyInfo
    uptime_seconds: int | None
    version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        build = self.build.to_dict()

        config_persistence = self.config_persistence

        config_version = self.config_version

        started_at: int | None
        started_at = self.started_at

        topology = self.topology.to_dict()

        uptime_seconds: int | None
        uptime_seconds = self.uptime_seconds

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "build": build,
                "config_persistence": config_persistence,
                "config_version": config_version,
                "started_at": started_at,
                "topology": topology,
                "uptime_seconds": uptime_seconds,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.build_info import BuildInfo
        from ..models.topology_info import TopologyInfo

        d = dict(src_dict)
        build = BuildInfo.from_dict(d.pop("build"))

        config_persistence = d.pop("config_persistence")

        config_version = d.pop("config_version")

        def _parse_started_at(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        started_at = _parse_started_at(d.pop("started_at"))

        topology = TopologyInfo.from_dict(d.pop("topology"))

        def _parse_uptime_seconds(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        uptime_seconds = _parse_uptime_seconds(d.pop("uptime_seconds"))

        version = d.pop("version")

        info_view = cls(
            build=build,
            config_persistence=config_persistence,
            config_version=config_version,
            started_at=started_at,
            topology=topology,
            uptime_seconds=uptime_seconds,
            version=version,
        )

        info_view.additional_properties = d
        return info_view

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
