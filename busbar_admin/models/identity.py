from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.phase import Phase

T = TypeVar("T", bound="Identity")


@_attrs_define(repr=False)
class Identity:
    """
    Attributes:
        plane (str):
        phase (Phase): LlmProducerDrive: producer drive returned; buffered response bytes may still be draining.
            MountedResponseReady: mounted handler returned its response; its body may still be streaming.
        pool (str):
        ingress_protocol (str):
        count (str): Unsigned 64-bit integer as an exact decimal string.
        errors (str): Unsigned 64-bit integer as an exact decimal string.
        client_errors (str): Unsigned 64-bit integer as an exact decimal string.
        sum_us (str): Unsigned 64-bit integer as an exact decimal string.
        bins (list[str]): Exclusive bins corresponding to `upper_bounds_ms`; their sum equals `count`.
    """

    plane: str
    phase: Phase
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

        phase = self.phase.value

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

        phase = Phase(d.pop("phase"))

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
