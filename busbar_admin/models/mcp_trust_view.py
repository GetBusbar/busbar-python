from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mcp_capability_view import McpCapabilityView


T = TypeVar("T", bound="McpTrustView")


@_attrs_define(repr=False)
class McpTrustView:
    """THE TRUST VIEW of one registered MCP server — `POST /tools/{name}/connect` and
    `GET /tools/{name}/changes` answer with this.

        Attributes:
            added (list[str]): Offered now, never ruled on.
            capabilities (list[McpCapabilityView]): Every capability's standing status, in name order.
            changed (list[str]): Approved, but offered at a DIFFERENT digest. THIS IS THE RUG-PULL ROW.
            failure (None | str): Why the last contact failed, when it did.
            name (str):
            observed_tools (int): How many tools the last successful observation carried.
            pin_changed (bool): The presented identity is not the locked one. Its own axis: adopting a new identity is a
                different act from adopting new content.
            pin_mechanism (str): The operator's word for the authenticity root. Never interpreted by the machine.
            removed (list[str]): Approved, and no longer offered.
            state (str): `pending`, `approved`, `quarantined`, `suspended` or `error`. DERIVED from the approval and
                the last sighting on every read, so there is no stored state to go stale.
    """

    added: list[str]
    capabilities: list[McpCapabilityView]
    changed: list[str]
    failure: None | str
    name: str
    observed_tools: int
    pin_changed: bool
    pin_mechanism: str
    removed: list[str]
    state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        added = self.added

        capabilities = []
        for capabilities_item_data in self.capabilities:
            capabilities_item = capabilities_item_data.to_dict()
            capabilities.append(capabilities_item)

        changed = self.changed

        failure: None | str
        failure = self.failure

        name = self.name

        observed_tools = self.observed_tools

        pin_changed = self.pin_changed

        pin_mechanism = self.pin_mechanism

        removed = self.removed

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "added": added,
                "capabilities": capabilities,
                "changed": changed,
                "failure": failure,
                "name": name,
                "observed_tools": observed_tools,
                "pin_changed": pin_changed,
                "pin_mechanism": pin_mechanism,
                "removed": removed,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_capability_view import McpCapabilityView  # noqa: PLC0415

        d = dict(src_dict)
        added = cast(list[str], d.pop("added"))

        capabilities = []
        _capabilities = d.pop("capabilities")
        for capabilities_item_data in _capabilities:
            capabilities_item = McpCapabilityView.from_dict(capabilities_item_data)

            capabilities.append(capabilities_item)

        changed = cast(list[str], d.pop("changed"))

        def _parse_failure(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        failure = _parse_failure(d.pop("failure"))

        name = d.pop("name")

        observed_tools = d.pop("observed_tools")

        pin_changed = d.pop("pin_changed")

        pin_mechanism = d.pop("pin_mechanism")

        removed = cast(list[str], d.pop("removed"))

        state = d.pop("state")

        mcp_trust_view = cls(
            added=added,
            capabilities=capabilities,
            changed=changed,
            failure=failure,
            name=name,
            observed_tools=observed_tools,
            pin_changed=pin_changed,
            pin_mechanism=pin_mechanism,
            removed=removed,
            state=state,
        )

        mcp_trust_view.additional_properties = d
        return mcp_trust_view

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
