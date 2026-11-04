from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="McpHealthView")


@_attrs_define(repr=False)
class McpHealthView:
    """THE HEALTH VIEW — `GET /tools/{name}/health`. Deliberately smaller than the trust view: health
    answers "can busbar use this server right now, and if not why", and a dashboard polling it should
    not be re-rendering the whole changes queue to find out.

        Attributes:
            contacted (bool): `false` until a refresh has ever landed. A server that has never been contacted is not
                unhealthy, and reporting it as such would page somebody for a declarative deployment.
            failure (None | str):
            name (str):
            observed_tools (int):
            serving (bool): Whether this server currently SERVES: `state == approved`. Named separately from `state`
                because it is the one bit a caller usually wants and deriving it from a word is how a client
                ends up hard-coding a spelling.
            state (str):
    """

    contacted: bool
    failure: None | str
    name: str
    observed_tools: int
    serving: bool
    state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contacted = self.contacted

        failure: None | str
        failure = self.failure

        name = self.name

        observed_tools = self.observed_tools

        serving = self.serving

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contacted": contacted,
                "failure": failure,
                "name": name,
                "observed_tools": observed_tools,
                "serving": serving,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contacted = d.pop("contacted")

        def _parse_failure(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        failure = _parse_failure(d.pop("failure"))

        name = d.pop("name")

        observed_tools = d.pop("observed_tools")

        serving = d.pop("serving")

        state = d.pop("state")

        mcp_health_view = cls(
            contacted=contacted,
            failure=failure,
            name=name,
            observed_tools=observed_tools,
            serving=serving,
            state=state,
        )

        mcp_health_view.additional_properties = d
        return mcp_health_view

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
