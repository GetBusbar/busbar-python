from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ApproveReq")


@_attrs_define(repr=False)
class ApproveReq:
    """The `approve` request body. ONE required field, and it is required because it is the operator's
    evidence that they looked.

        Attributes:
            fingerprint (str): The canonical card fingerprint EXACTLY as `connect` reported it.
    """

    fingerprint: str

    def to_dict(self) -> dict[str, Any]:
        fingerprint = self.fingerprint

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "fingerprint": fingerprint,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fingerprint = d.pop("fingerprint")

        if d:
            raise ValueError("Unexpected fields for ApproveReq")
        approve_req = cls(
            fingerprint=fingerprint,
        )

        return approve_req
