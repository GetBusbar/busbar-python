from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="McpCapabilityView")


@_attrs_define(repr=False)
class McpCapabilityView:
    """ONE CAPABILITY'S STANDING STATUS, the three-way answer a trust view has to render.

    Three and not two: `approved at a digest`, `rejected`, and `allowed but never ruled on`. The
    third is `pending` and it is the one a queue exists to drain, so collapsing it into "not
    approved" would hide the operator's whole worklist.

        Attributes:
            approved_digest (None | str): The digest held by the kernel, when there is one. Rejection or pending status does
                not imply
                that this historical or configured approval currently permits serving.
            status (str): `approved`, `rejected` or `pending`.
            tool (str): The bare tool name, as the upstream spells it.
    """

    approved_digest: None | str
    status: str
    tool: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approved_digest: None | str
        approved_digest = self.approved_digest

        status = self.status

        tool = self.tool

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "approved_digest": approved_digest,
                "status": status,
                "tool": tool,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_approved_digest(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        approved_digest = _parse_approved_digest(d.pop("approved_digest"))

        status = d.pop("status")

        tool = d.pop("tool")

        mcp_capability_view = cls(
            approved_digest=approved_digest,
            status=status,
            tool=tool,
        )

        mcp_capability_view.additional_properties = d
        return mcp_capability_view

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
