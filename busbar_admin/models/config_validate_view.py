from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConfigValidateView")


@_attrs_define
class ConfigValidateView:
    """The result of `POST /api/v1/admin/config/validate` — a DRY-RUN: does a proposed config resolve +
    validate, WITHOUT applying anything. `ok` is the verdict; `errors` lists every structural/resolution
    failure at once (empty when `ok`). A well-formed request always returns 200 with this view (a valid
    request that describes an INVALID config is `ok: false`, not an HTTP error); only a MALFORMED request
    body is an `invalid_request`. Env-var interpolation is out of scope — this checks structure and
    cross-reference resolution, not runtime secret presence.

        Attributes:
            errors (list[str]):
            ok (bool):
    """

    errors: list[str]
    ok: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors = self.errors

        ok = self.ok

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errors": errors,
                "ok": ok,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        errors = cast(list[str], d.pop("errors"))

        ok = d.pop("ok")

        config_validate_view = cls(
            errors=errors,
            ok=ok,
        )

        config_validate_view.additional_properties = d
        return config_validate_view

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
