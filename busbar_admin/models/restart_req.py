from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestartReq")


@_attrs_define
class RestartReq:
    """The `POST /api/v1/admin/restart` body. Absent is the same as `{}`.

    Attributes:
        confirm (bool | Unset): Proceed even though no supervisor was detected. Exiting only restarts busbar if
            something
            restarts it; without this an undetected supervisor is refused rather than risking the
            gateway staying down. Default: False.
    """

    confirm: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        confirm = self.confirm

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if confirm is not UNSET:
            field_dict["confirm"] = confirm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confirm = d.pop("confirm", UNSET)

        restart_req = cls(
            confirm=confirm,
        )

        return restart_req
