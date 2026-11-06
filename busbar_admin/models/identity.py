from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Identity")


@_attrs_define(repr=False)
class Identity:
    """
    Attributes:
        plane (str):
        phase (Literal['LlmProducerDrive'] | Literal['MountedResponseReady']):
        pool (str):
        ingress_protocol (str):
        count (str): Unsigned 64-bit integer as an exact decimal string.
        errors (str): Unsigned 64-bit integer as an exact decimal string.
        client_errors (str): Unsigned 64-bit integer as an exact decimal string.
        sum_us (str): Unsigned 64-bit integer as an exact decimal string.
        bins (list[str]): Exclusive bins corresponding to `upper_bounds_ms`; their sum equals `count`.
    """

    plane: str
    phase: Literal["LlmProducerDrive"] | Literal["MountedResponseReady"]
    pool: str
    ingress_protocol: str
    count: str
    errors: str
    client_errors: str
    sum_us: str
    bins: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plane = self.plane

        phase: Literal["LlmProducerDrive"] | Literal["MountedResponseReady"]
        phase = self.phase

        pool = self.pool

        ingress_protocol = self.ingress_protocol

        count = self.count

        errors = self.errors

        client_errors = self.client_errors

        sum_us = self.sum_us

        bins = self.bins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plane": plane,
                "phase": phase,
                "pool": pool,
                "ingress_protocol": ingress_protocol,
                "count": count,
                "errors": errors,
                "client_errors": client_errors,
                "sum_us": sum_us,
                "bins": bins,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        plane = d.pop("plane")

        def _parse_phase(data: object) -> Literal["LlmProducerDrive"] | Literal["MountedResponseReady"]:
            componentsschemas_phase_type_0 = cast(Literal["LlmProducerDrive"], data)
            if componentsschemas_phase_type_0 != "LlmProducerDrive":
                raise ValueError(
                    f"/components/schemas/Phase_type_0 must match const 'LlmProducerDrive', got '{componentsschemas_phase_type_0}'"
                )
            return componentsschemas_phase_type_0
            componentsschemas_phase_type_1 = cast(Literal["MountedResponseReady"], data)
            if componentsschemas_phase_type_1 != "MountedResponseReady":
                raise ValueError(
                    f"/components/schemas/Phase_type_1 must match const 'MountedResponseReady', got '{componentsschemas_phase_type_1}'"
                )
            return componentsschemas_phase_type_1
            raise ValueError("Invalid value for phase")

        phase = _parse_phase(d.pop("phase"))

        pool = d.pop("pool")

        ingress_protocol = d.pop("ingress_protocol")

        count = d.pop("count")

        errors = d.pop("errors")

        client_errors = d.pop("client_errors")

        sum_us = d.pop("sum_us")

        bins = cast(list[str], d.pop("bins"))

        identity = cls(
            plane=plane,
            phase=phase,
            pool=pool,
            ingress_protocol=ingress_protocol,
            count=count,
            errors=errors,
            client_errors=client_errors,
            sum_us=sum_us,
            bins=bins,
        )

        identity.additional_properties = d
        return identity

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
